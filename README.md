# 🎬 YouTube Summarizer Skill

Una habilidad para Claude Code que resume, explica y genera preguntas interactivas sobre videos de YouTube en cualquier idioma.

## 📋 Características

- ✅ **Soporte multiidioma**: Funciona con videos en cualquier idioma
- 🔄 **Traducción automática**: Traduce automáticamente si el video no está en español/inglés
- 📊 **Resumen inteligente**: Genera resúmenes ejecutivos de conceptos clave
- ❓ **Preguntas interactivas**: 5 preguntas de comprensión (conceptual, detalle, análisis, aplicación, opinión)
- 💬 **Retroalimentación personalizada**: Evalúa respuestas basadas en el contenido del video
- 🔧 **Múltiples métodos**: Python API + yt-dlp fallback + opción manual

## 🚀 Instalación

### Requisitos previos
- Python 3.7+
- pip (gestor de paquetes de Python)
- Claude Code

### Pasos de instalación

1. **Clonar o descargar este repositorio**
   ```bash
   git clone https://github.com/neyderDev/skill-link19052026.git
   cd skill-link19052026
   ```

2. **Instalar la dependencia Python**
   ```bash
   pip install youtube-transcript-api
   ```

3. **Opcional: Instalar yt-dlp (para fallback)**
   ```bash
   pip install yt-dlp
   ```

4. **La skill está lista para usarse en Claude Code**

## 📖 Cómo usar

### En Claude Code (VSCode, Web o Desktop)

1. Invoca la skill escribiendo `/youtube-summarizer`
2. Pega un link de YouTube cuando se solicite
3. La skill generará:
   - 📝 Resumen ejecutivo del video
   - 💡 Explicación detallada de conceptos
   - ❓ 5 preguntas de comprensión
4. Responde las preguntas y recibe retroalimentación

### Formatos de URL soportados

```
https://www.youtube.com/watch?v=dQw4w9WgXcQ
https://youtu.be/dQw4w9WgXcQ
https://www.youtube.com/shorts/dQw4w9WgXcQ
https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=42s
```

## 🔧 Archivo de configuración

### `SKILL.md`
- Contiene instrucciones para Claude sobre cómo procesar videos
- Define el flujo de 6 pasos (extracción, traducción, resumen, preguntas, etc.)

### `get_transcript.py`
- Script Python que extrae transcripciones usando la API oficial de YouTube
- Soporta detección de idioma
- Manejo robusto de errores

## 💾 Estructura del proyecto

```
skill-link19052026/
├── README.md                          ← Este archivo
├── .claude/
│   └── skills/
│       └── youtube-summarizer/
│           ├── SKILL.md               ← Instrucciones para Claude
│           └── get_transcript.py      ← Script de extracción
└── .git/                              ← Repositorio Git
```

## 🌐 Idiomas soportados

La skill automáticamente detecta y traduce contenido en:
- 🇪🇸 Español
- 🇺🇸 Inglés
- 🇫🇷 Francés
- 🇩🇪 Alemán
- 🇵🇹 Portugués
- 🇯🇵 Japonés
- 🇨🇳 Chino
- 🇮🇹 Italiano
- Y muchos más...

## 🐛 Solución de problemas

### "No se encontró transcripción"
- ✅ Verifica que el video tenga subtítulos habilitados
- ✅ Algunos videos privados o restringidos no tienen transcripciones disponibles

### Error: "ModuleNotFoundError: No module named 'youtube_transcript_api'"
- ✅ Instala la dependencia: `pip install youtube-transcript-api`

### "Couldn't get subtitles. This video may not have any subtitles."
- ✅ La skill pasará al método alternativo (yt-dlp)
- ✅ Si eso falla, puedes proporcionar la transcripción manualmente

### El script Python no se ejecuta en Windows
- ✅ Asegúrate de que Python esté en tu PATH
- ✅ Intenta: `python -m pip install youtube-transcript-api`
- ✅ O ejecuta `pip install youtube-transcript-api` desde PowerShell como administrador

## 📚 Casos de uso

- 📚 **Estudiantes**: Aprende de videos educativos con resúmenes y preguntas de práctica
- 💼 **Profesionales**: Extrae rápidamente conceptos clave de videos de capacitación
- 🎓 **Maestros**: Crea cuestionarios de comprensión para evaluar estudiantes
- 🔍 **Investigadores**: Resume investigaciones en video y extrae información clave

## 🛠 Desarrollo futuro

Mejoras planeadas:
- [ ] Generación de notas en Markdown descargables
- [ ] Exportación de resúmenes a PDF
- [ ] Análisis de sentimientos del contenido
- [ ] Integración con sistemas de gestión de aprendizaje (LMS)
- [ ] Soporte para listas de reproducción completas
- [ ] Almacenamiento en caché de transcripciones

## 📝 Licencia

Este proyecto es de código abierto. Consulta LICENSE si existe.

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor:
1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/MiMejora`)
3. Commit tus cambios (`git commit -m 'Agrega MiMejora'`)
4. Push a la rama (`git push origin feature/MiMejora`)
5. Abre un Pull Request

## 📧 Contacto

Creado por: [@neyderDev](https://github.com/neyderDev)
Email: dev02@kreante.co

---

**¡Disfruta aprendiendo de videos en YouTube con resúmenes inteligentes! 🚀**
