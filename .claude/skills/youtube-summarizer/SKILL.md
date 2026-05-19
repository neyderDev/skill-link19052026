---
name: youtube-summarizer
description: Resume, explica y genera preguntas sobre un video de YouTube. Úsalo cuando el usuario pase un link de YouTube y quiera entender, aprender o ser evaluado sobre su contenido. Soporta videos en cualquier idioma.
---

Cuando el usuario proporciona un link de YouTube, sigue estos pasos:

## Paso 1: Extraer el ID del video
Obtén el `video_id` del link. Los formatos comunes son:
- `https://www.youtube.com/watch?v=XXXXX` → `XXXXX`
- `https://youtu.be/XXXXX` → `XXXXX`
- `https://www.youtube.com/shorts/XXXXX` → `XXXXX`

## Paso 2: Obtener la transcripción
Intenta estos métodos en orden:

1. **Opción A - Python con youtube-transcript-api (AUTOMÁTICO):**
   - Primero, instala automáticamente si no está disponible:
   ```bash
   python -m pip install youtube-transcript-api --quiet
   ```
   - Luego ejecuta:
   ```bash
   python .claude/skills/youtube-summarizer/get_transcript.py VIDEO_ID
   ```
   - Si falla por dependencia faltante, instala desde requirements.txt:
   ```bash
   python -m pip install -r requirements.txt --quiet
   ```

2. **Opción B - Fallback con yt-dlp (si Python falla):**
   ```bash
   pip install yt-dlp --quiet
   yt-dlp --write-auto-sub --sub-lang en,es,fr,de,pt,ja,zh --skip-download "https://www.youtube.com/watch?v=VIDEO_ID"
   ```

3. **Opción C - Manual (último recurso):**
   Si ambas opciones fallan, pide al usuario que:
   - Abra el video en YouTube
   - Active los subtítulos (CC)
   - Use las herramientas del navegador para copiar la transcripción
   - La pegue en el chat

## Paso 3: Detectar idioma y traducir
- Analiza el idioma de la transcripción obtenida
- Si el contenido NO está en español o inglés, tradúcelo automáticamente antes de continuar
- Menciona el idioma original en tu respuesta

## Paso 4: Generar el resumen estructurado
Produce una respuesta con esta estructura:

```
## 🎬 [Título del video]

## 📝 Resumen ejecutivo
[3-5 párrafos resumiendo los puntos principales del video]

## 💡 Explicación detallada
[Desglose de conceptos clave con contexto y ejemplos prácticos]

### Puntos principales:
- Punto 1
- Punto 2
- Punto 3
- Punto 4
- Punto 5

## 🌍 Contexto
[Información sobre dónde y cómo se aplica este contenido]

## ❓ Preguntas de comprensión
Responde las siguientes preguntas para demostrar tu comprensión:

1. **Pregunta conceptual**: [Pregunta sobre el tema principal]
2. **Pregunta de detalle**: [Pregunta sobre un concepto específico mencionado]
3. **Pregunta de análisis**: [Pregunta que requiera análisis o reflexión crítica]
4. **Pregunta aplicada**: [Pregunta sobre cómo aplicar lo aprendido]
5. **Pregunta de opinión**: [Pregunta que invite a reflexión personal basada en el video]
```

## Paso 5: Interacción con el usuario
Después de mostrar el resumen:
- Espera a que el usuario responda las 5 preguntas
- Lee cada respuesta cuidadosamente
- Proporciona retroalimentación detallada basada en el contenido del video
- Destaca qué respondió correctamente y qué puede mejorar
- Ofrece explicaciones adicionales si es necesario
- Si todas las respuestas son correctas, felicita al usuario y sugiere temas relacionados para aprender más

## Paso 6: Modo de profundización (opcional)
Si el usuario lo solicita:
- Aclara conceptos específicos del video
- Proporciona ejemplos adicionales
- Sugiere recursos relacionados
- Crea ejercicios o casos de estudio basados en el contenido

---

## Notas importantes

- **Idiomas múltiples**: Si el video tiene subtítulos en varios idiomas, usa el más disponible (preferencia: idioma original > inglés > otros)
- **Videos sin subtítulos**: Si el video no tiene transcripción disponible, avisa al usuario y ofrece alternativas
- **Errores de API**: Si hay problemas obteniendo la transcripción, sé transparente y sugiere el método manual
- **Privacidad**: No almacenes ni compartas datos personales del usuario o del video
- **Contenido sensible**: Si el video contiene contenido sensible, ofrece contexto apropiado en el resumen
