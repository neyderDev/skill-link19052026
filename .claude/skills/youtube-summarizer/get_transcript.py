#!/usr/bin/env python3
"""
YouTube Transcript Extractor
Obtiene la transcripción de un video de YouTube en cualquier idioma disponible.
"""

import sys
import json
import io
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound

# Configurar stdout para UTF-8 en Windows
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def get_video_transcript(video_id):
    """
    Obtiene la transcripción de un video de YouTube.

    Args:
        video_id (str): El ID del video de YouTube

    Returns:
        dict: Contiene 'lang' (código de idioma) y 'text' (transcripción completa)
    """
    try:
        api = YouTubeTranscriptApi()

        # Preferencia de idiomas: SIEMPRE ESPAÑOL primero
        preferred_langs = ['es', 'es-ES', 'es-MX', 'en', 'en-US', 'en-GB', 'fr', 'de', 'pt', 'ja', 'zh', 'it']

        transcript_data = None
        lang_code = None
        is_generated = False

        # Intentar obtener en idiomas preferidos
        for lang in preferred_langs:
            try:
                transcript_data = api.fetch(video_id, languages=[lang])
                lang_code = lang
                break
            except (NoTranscriptFound, Exception):
                continue

        # Si no hay en idiomas preferidos, obtener primer disponible
        if transcript_data is None:
            try:
                transcript_data = api.fetch(video_id)
                lang_code = 'en'
                is_generated = False
            except TranscriptsDisabled:
                print("ERROR: Transcripts are disabled for this video", file=sys.stderr)
                sys.exit(1)
            except NoTranscriptFound:
                print("ERROR: No transcripts found in any language", file=sys.stderr)
                sys.exit(1)

        # Acceder a los snippets del objeto FetchedTranscript
        try:
            # Intentar acceder como dict (versión antigua)
            snippets = [entry['text'] for entry in transcript_data]
        except (TypeError, KeyError):
            # Acceder como atributo (versión nueva)
            snippets = [snippet.text for snippet in transcript_data]

        # Combinar todos los textos en un solo párrafo
        full_text = " ".join(snippets)

        # Obtener nombre del idioma
        lang_names = {
            'es': 'Español',
            'en': 'English',
            'fr': 'Français',
            'de': 'Deutsch',
            'pt': 'Português',
            'ja': '日本語',
            'zh': '中文',
            'it': 'Italiano',
            'auto': 'Auto-detected'
        }

        # Salida en formato JSON para fácil parsing
        result = {
            'lang': lang_code,
            'language_name': lang_names.get(lang_code, lang_code),
            'is_generated': is_generated,
            'text': full_text,
            'entries_count': len(transcript_data)
        }

        print(json.dumps(result, ensure_ascii=False, indent=2))

    except TranscriptsDisabled:
        print("ERROR: Transcripts are disabled for this video", file=sys.stderr)
        sys.exit(1)
    except NoTranscriptFound:
        print("ERROR: No transcripts found in any language", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python get_transcript.py <video_id>", file=sys.stderr)
        sys.exit(1)

    video_id = sys.argv[1]
    get_video_transcript(video_id)
