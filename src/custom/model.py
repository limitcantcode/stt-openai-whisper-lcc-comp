import logging
import whisper
from .audio import format_audio

class STTModel():
    def __init__(self):
        self.model = whisper.load_model("turbo")
        logging.debug("STTModel initialized!")

    '''
    Transcribed input wave file that contains speech.

    Returns (str) the transcribed text.
    '''
    def __call__(self, audio, sample_rate, sample_width, channels):
        audio_array = format_audio(audio, sample_rate, sample_width, channels)

        logging.debug(f"Got transcription request.")
        result = self.model.transcribe(audio_array, language='English')
        logging.debug(f"Got transcription result: {result}")
        return result["text"]