import shutil
import subprocess
from pathlib import Path


# ============================================================
# MIMIR MODEL MANAGER
# ============================================================

MODEL = "ggml-org/gemma-3-4b-it-GGUF:Q4_K_M"


def find_llama_server():
    """Sucht llama-server im System."""
    llama_server = shutil.which("llama-server")

    if llama_server is None:
        raise RuntimeError(
            "llama-server wurde nicht gefunden."
        )

    return llama_server


def check_model():
    """
    Prüft, ob Gemma 3 4B im Hugging-Face-Cache
    von llama.cpp vorhanden ist.
    """

    print()
    print("==============================")
    print("MIMIR MODEL MANAGER")
    print("==============================")
    print()
    print("Prüfe Sprachmodell ...")
    print()

    cache_dir = (
        Path.home()
        / ".cache"
        / "huggingface"
        / "hub"
        / "models--ggml-org--gemma-3-4b-it-GGUF"
    )

    if not cache_dir.exists():
        print("✗ Gemma 3 4B Instruct Q4_K_M nicht gefunden.")
        return False

    # Nach GGUF-Dateien im Cache suchen
    gguf_files = list(cache_dir.rglob("*.gguf"))

    if not gguf_files:
        print("✗ Gemma 3 4B Instruct Q4_K_M nicht gefunden.")
        return False

    print("✓ Gemma 3 4B wurde gefunden.")
    print("\033[2J\033[H", end="")
    print()

    for file in gguf_files:
        print(f"  {file}")

    print()

    return True

def download_model():
    """
    Lädt Gemma 3 4B über llama-server aus Hugging Face.
    
    llama.cpp kümmert sich dabei selbst um:
    - den Download
    - den Hugging-Face-Cache
    - die benötigten Modell-Dateien
    
    Sobald das Modell geladen wurde, wird der Server wieder beendet.
    """

    print()
    print("Gemma 3 4B wird heruntergeladen ...")
    print()
    print("Downloadgröße: ungefähr 2,5 GB")
    print("Bitte etwas Geduld.")
    print()

    llama_server = find_llama_server()

    command = [
        llama_server,
        "--hf-repo",
        MODEL,
        "--host",
        "127.0.0.1",
        "--port",
        "8199",
        "--n-gpu-layers",
        "0",
    ]

    try:
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
        )

        model_loaded = False

        while True:
            line = process.stdout.readline()

            if not line:
                break

            print(line, end="")

            # llama.cpp meldet hier, dass das Modell
            # vollständig geladen wurde.
            if "model loaded" in line.lower():
                model_loaded = True
                break

        if model_loaded:
            print()
            print("✓ Gemma wurde erfolgreich heruntergeladen.")
            print()

            # Server wieder beenden.
            process.terminate()

            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()

            return True

        # Falls llama-server vorher beendet wurde
        process.terminate()

        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()

        print()
        print("✗ Das Modell konnte nicht geladen werden.")
        return False

    except KeyboardInterrupt:
        print()
        print()
        print("Download abgebrochen.")

        try:
            process.terminate()
        except Exception:
            pass

        return False

    except Exception as e:
        print()
        print("✗ Fehler beim Download:")
        print(e)
        return False
    
def ensure_model():
    """
    Hauptfunktion des Model Managers.

    Prüft zuerst, ob Gemma vorhanden ist.
    Falls nicht, wird der Benutzer gefragt.
    """

    if check_model():
        return True

    print()
    print("MIMIR benötigt dieses Sprachmodell.")
    print("Downloadgröße: ungefähr 2,5 GB")
    print()

    answer = input(
        "Gemma 3 4B jetzt herunterladen? (j/n): "
    ).strip().lower()

    if answer != "j":
        print()
        print("Gemma wurde nicht installiert.")
        print()
        print("✗ Kein Modell verfügbar.")
        return False

    if download_model():
        print()
        print("✓ Gemma ist installiert.")
        print()
        return True

    print()
    print("✗ Gemma konnte nicht installiert werden.")
    return False


# ============================================================
# TEST
# ============================================================

if __name__ == "__main__":
    ensure_model()
