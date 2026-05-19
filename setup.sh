#!/bin/bash
# Setup script para YouTube Summarizer Skill
# Instala todas las dependencias necesarias

echo "🎬 YouTube Summarizer Skill - Setup"
echo "===================================="

# Detectar Python
if ! command -v python3 &> /dev/null; then
    if ! command -v python &> /dev/null; then
        echo "❌ Python no está instalado"
        echo "Por favor instala Python 3.7+ desde python.org"
        exit 1
    fi
    PYTHON="python"
else
    PYTHON="python3"
fi

echo "✅ Python encontrado: $PYTHON"
echo ""

# Instalar youtube-transcript-api
echo "📦 Instalando youtube-transcript-api..."
$PYTHON -m pip install youtube-transcript-api --quiet

if [ $? -eq 0 ]; then
    echo "✅ youtube-transcript-api instalado correctamente"
else
    echo "❌ Error instalando youtube-transcript-api"
    exit 1
fi

echo ""

# Opcionalmente instalar yt-dlp para fallback
echo "📦 Instalando yt-dlp (para fallback)..."
$PYTHON -m pip install yt-dlp --quiet

if [ $? -eq 0 ]; then
    echo "✅ yt-dlp instalado correctamente"
else
    echo "⚠️  yt-dlp no se instaló, pero la skill funcionará con youtube-transcript-api"
fi

echo ""
echo "===================================="
echo "✅ Setup completado!"
echo ""
echo "🚀 Ahora puedes probar la skill con:"
echo ""
echo "   python .claude/skills/youtube-summarizer/get_transcript.py dQw4w9WgXcQ"
echo ""
echo "O usar en Claude Code:"
echo "   /youtube-summarizer"
echo "   https://www.youtube.com/watch?v=dQw4w9WgXcQ"
echo ""
