import logging
import whisper

class STTModel():
    def __init__(self):
        self.model = whisper.load_model("turbo")
        logging.debug("STTModel initialized!")

    '''
    Transcribed input wave file that contains speech.

    Returns (str) the transcribed text.
    '''
    def __call__(self, filepath):
        logging.debug(f"Got transcription request.")
        result = self.model.transcribe(filepath, language='English')
        logging.debug(f"Got transcription result: {result}")
        return result["text"]