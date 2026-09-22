import json
import shutil
import subprocess
import time
import urllib.error
import urllib.request


MODEL = "ggml-org/gemma-3-4b-it-GGUF:Q4_K_M"

HOST = "127.0.0.1"
PORT = 8101

URL = f"http://{HOST}:{PORT}/v1/chat/completions"


def start_server():
    llama_server = shutil.which("llama-server")

    if llama_server is None:
        raise RuntimeError("llama-server wurde nicht gefunden.")

    command = [
        llama_server,
        "--hf-repo", MODEL,
        "--offline",
        "--host", HOST,
        "--port", str(PORT),
        "--n-gpu-layers", "0",
        "--log-disable",
    ]

    return subprocess.Popen(
        command,
        stdout=None,
        stderr=None,
    )

    return subprocess.Popen(
        command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,    
    )



def wait_for_server():

    for _ in range(60):

        try:
            urllib.request.urlopen(
                f"http://{HOST}:{PORT}/health",
                timeout=1
            ).close()

            return True

        except (urllib.error.URLError, TimeoutError):

            time.sleep(0.5)

    return False


def chat(messages):
    #print("\n[ENGINE: chat() wurde aufgerufen]")

    prompt_text = json.dumps(messages, ensure_ascii=False)
   # print(f"[ENGINE] Nachrichten: {len(messages)}")
   # print(f"[ENGINE] Prompt-Größe: {len(prompt_text):,} Zeichen")

    start = time.time()
    erstes_token = None

    payload = {
        "model": "gemma-3-4b",
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 130,
        "stream": True,
    }

    request = urllib.request.Request(
        URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    antwort = []

    #print("[ENGINE] Anfrage wird gesendet...")

    with urllib.request.urlopen(request, timeout=120) as response:
        for raw_line in response:
            line = raw_line.decode("utf-8").strip()

            if not line.startswith("data: "):
                continue

            data = line[6:]

            if data == "[DONE]":
                break

            delta = json.loads(data)["choices"][0].get("delta", {})
            text = delta.get("content", "")

            if text:
                if erstes_token is None:
                    erstes_token = time.time()
                    #print(
                     #   f"\n[ENGINE] Erstes Token nach "
                      #  f"{erstes_token - start:.1f} Sekunden:"
                    #)

                print(text, end="", flush=True)
                antwort.append(text)

    ende = time.time()

   # print(
    #    f"\n[ENGINE] Antwort fertig nach "
     #   f"{ende - start:.1f} Sekunden"
    #)

    return "".join(antwort).strip()

def chat_once(messages):

    payload = {
        "model": "gemma-3-4b",
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 130,
        "stream": False,
    }

    request = urllib.request.Request(
        URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    with urllib.request.urlopen(request, timeout=120) as response:

        data = json.loads(response.read().decode("utf-8"))

    return data["choices"][0]["message"]["content"].strip()



    
def stop_server(server):

    if server is not None:

        server.terminate()

        try:
            server.wait(timeout=5)

        except subprocess.TimeoutExpired:

            server.kill()
            server.wait()
