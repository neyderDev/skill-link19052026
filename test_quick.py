#!/usr/bin/env python3
"""
Quick test script para YouTube Summarizer Skill
Instala dependencias automáticamente y prueba la skill
"""

import subprocess
import sys
import json
from pathlib import Path
import io

# Configurar stdout para UTF-8 en Windows
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def run_command(cmd, description=""):
    """Ejecuta un comando y retorna el resultado"""
    try:
        if description:
            print(f"⏳ {description}...", end=" ", flush=True)
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30, shell=True)
        if description:
            print("✅" if result.returncode == 0 else "❌")
        return result
    except subprocess.TimeoutExpired:
        if description:
            print("⏱️ TIMEOUT")
        return None
    except Exception as e:
        if description:
            print(f"❌ {e}")
        return None

def main():
    print("\n")
    print("="*60)
    print("🎬 YouTube Summarizer - Quick Test")
    print("="*60)
    print("")

    # Step 1: Verificar Python
    print("1️⃣  Verificando Python...")
    result = run_command(f"{sys.executable} --version", "  Versión de Python")
    if not result or result.returncode != 0:
        print("❌ Python no encontrado")
        sys.exit(1)
    print(f"  → {result.stdout.strip()}")
    print("")

    # Step 2: Instalar dependencias
    print("2️⃣  Instalando dependencias...")

    # Instalar youtube-transcript-api
    run_command(f"{sys.executable} -m pip install youtube-transcript-api --quiet",
                "  youtube-transcript-api")

    # Instalar yt-dlp (fallback)
    run_command(f"{sys.executable} -m pip install yt-dlp --quiet",
                "  yt-dlp (fallback)")
    print("")

    # Step 3: Verificar archivos
    print("3️⃣  Verificando archivos de la skill...")
    script_path = Path(".claude/skills/youtube-summarizer/get_transcript.py")
    if script_path.exists():
        print(f"  ✅ get_transcript.py encontrado")
    else:
        print(f"  ❌ get_transcript.py NO encontrado en {script_path}")
        sys.exit(1)
    print("")

    # Step 4: Prueba real
    print("4️⃣  Descargando transcripción de YouTube...")
    print("  Video: Rick Roll (https://youtu.be/dQw4w9WgXcQ)")

    result = run_command(
        f"{sys.executable} .claude/skills/youtube-summarizer/get_transcript.py dQw4w9WgXcQ",
        "  Extrayendo transcripción"
    )

    if result and result.returncode == 0:
        try:
            data = json.loads(result.stdout)
            print(f"  ✅ Éxito!")
            print(f"")
            print(f"  📊 Detalles:")
            print(f"     • Idioma: {data['language_name']} ({data['lang']})")
            print(f"     • Generado: {'Sí (Auto)' if data['is_generated'] else 'No (Manual)'}")
            print(f"     • Subtítulos: {data['entries_count']}")
            print(f"     • Texto (primeros 150 caracteres):")
            print(f"       '{data['text'][:150]}...'")
            print("")
            print("="*60)
            print("✅ ¡La skill funciona perfectamente!")
            print("="*60)
            print("")
            print("🚀 Próximos pasos:")
            print("")
            print("Opción 1: Usa la skill en Claude Code")
            print("  • Abre Claude Code en VSCode o en claude.ai/code")
            print("  • Escribe: /youtube-summarizer")
            print("  • Pasa un link de YouTube")
            print("")
            print("Opción 2: Prueba otro video diferente")
            print(f"  • Ejecuta: python .claude/skills/youtube-summarizer/get_transcript.py <VIDEO_ID>")
            print("")
            return 0
        except json.JSONDecodeError:
            print(f"  ❌ Error al parsear JSON")
            print(f"  Output: {result.stdout[:200]}")
            return 1
    else:
        print(f"  ❌ Error descargando transcripción")
        if result:
            print(f"  Error: {result.stderr[:200]}")
        print("")
        print("Posibles soluciones:")
        print("  • Verifica tu conexión a internet")
        print("  • El video podría no tener transcripción disponible")
        print("  • Intenta con otro video")
        return 1

if __name__ == "__main__":
    sys.exit(main())
