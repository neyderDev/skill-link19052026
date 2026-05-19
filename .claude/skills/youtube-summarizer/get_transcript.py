#!/usr/bin/env python3
"""
YouTube Transcript Extractor
Obtiene la transcripción de un video de YouTube en cualquier idioma disponible.
"""

import sys
import json
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound

def get_video_transcript(video_id):
    """
    Obtiene la transcripción de un video de YouTube.

    Args:
        video_id (str): El ID del video de YouTube

    Returns:
        dict: Contiene 'lang' (código de idioma) y 'text' (transcripción completa)
    """
    try:
        # Obtener lista de transcripciones disponibles
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

        # Preferencia de idiomas: español > inglés > primer disponible > auto-generado
        preferred_langs = ['es', 'en', 'fr', 'de', 'pt', 'ja', 'zh', 'it']

        # Intentar transcripción manualmente creada primero
        transcript = None
        lang_code = None

        for lang in preferred_langs:
            try:
                transcript = transcript_list.find_transcript([lang])
                lang_code = lang
                break
            except NoTranscriptFound:
                continue

        # Si no hay transcripción manual en idiomas preferidos, usar auto-generada
        if transcript is None:
            try:
                # Obtener primer idioma disponible (manual o auto)
                if transcript_list.manually_created_transcripts:
                    transcript = transcript_list.manually_created_transcripts[0]
                    lang_code = transcript.language_code
                else:
                    transcript = transcript_list.generated_transcripts[0]
                    lang_code = transcript.language_code
            except (IndexError, AttributeError):
                print("ERROR: No transcripts found for this video", file=sys.stderr)
                sys.exit(1)

        # Obtener el contenido de la transcripción
        transcript_data = transcript.fetch()

        # Combinar todos los textos en un solo párrafo
        full_text = " ".join([entry['text'] for entry in transcript_data])

        # Salida en formato JSON para fácil parsing
        result = {
            'lang': lang_code,
            'language_name': transcript.language,
            'is_generated': transcript.is_generated,
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
