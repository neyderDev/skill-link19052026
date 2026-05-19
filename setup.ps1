# Setup script para YouTube Summarizer Skill (Windows PowerShell)
# Instala todas las dependencias necesarias

Write-Host "🎬 YouTube Summarizer Skill - Setup" -ForegroundColor Green
Write-Host "====================================" -ForegroundColor Green
Write-Host ""

# Detectar Python
$python = $null
if (Get-Command python3 -ErrorAction SilentlyContinue) {
    $python = "python3"
}
elseif (Get-Command python -ErrorAction SilentlyContinue) {
    $python = "python"
}
else {
    Write-Host "❌ Python no está instalado" -ForegroundColor Red
    Write-Host "Por favor instala Python 3.7+ desde python.org" -ForegroundColor Yellow
    exit 1
}

Write-Host "✅ Python encontrado: $python" -ForegroundColor Green
Write-Host ""

# Instalar youtube-transcript-api
Write-Host "📦 Instalando youtube-transcript-api..." -ForegroundColor Cyan
& $python -m pip install youtube-transcript-api --quiet 2>$null

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ youtube-transcript-api instalado correctamente" -ForegroundColor Green
}
else {
    Write-Host "❌ Error instalando youtube-transcript-api" -ForegroundColor Red
    exit 1
}

Write-Host ""

# Opcionalmente instalar yt-dlp para fallback
Write-Host "📦 Instalando yt-dlp (para fallback)..." -ForegroundColor Cyan
& $python -m pip install yt-dlp --quiet 2>$null

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ yt-dlp instalado correctamente" -ForegroundColor Green
}
else {
    Write-Host "⚠️  yt-dlp no se instaló, pero la skill funcionará con youtube-transcript-api" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "====================================" -ForegroundColor Green
Write-Host "✅ Setup completado!" -ForegroundColor Green
Write-Host ""
Write-Host "🚀 Ahora puedes probar la skill con:" -ForegroundColor Cyan
Write-Host ""
Write-Host "   python .claude\skills\youtube-summarizer\get_transcript.py dQw4w9WgXcQ" -ForegroundColor White
Write-Host ""
Write-Host "O usar en Claude Code:" -ForegroundColor Cyan
Write-Host "   /youtube-summarizer" -ForegroundColor White
Write-Host "   https://www.youtube.com/watch?v=dQw4w9WgXcQ" -ForegroundColor White
Write-Host ""
