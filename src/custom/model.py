import logging
import whisper
from .audio import format_audio

class STTModel():
    def __init__(self, model, prompt, no_speech_threshold):
        self.model = whisper.load_model(model)
        self.prompt = prompt
        self.no_speech_threshold = no_speech_threshold
        logging.debug("STTModel initialized!")

    '''
    Transcribed input wave file that contains speech.

    Returns (str) the transcribed text.
    '''
    def __call__(self, audio, sample_rate, sample_width, channels):
        audio_array = format_audio(audio, sample_rate, sample_width, channels)

        logging.debug(f"Got transcription request.")
        result = self.model.transcribe(audio_array, language='English', initial_prompt=self.prompt, no_speech_threshold=self.no_speech_threshold)
        logging.debug(f"Got transcription result: {result}")
        return result["text"]