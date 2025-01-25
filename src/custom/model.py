import logging
import whisper
import numpy as np

class STTModel():
    def __init__(self):
        self.model = whisper.load_model("turbo")
        logging.debug("STTModel initialized!")

    '''
    Transcribed input wave file that contains speech.

    Returns (str) the transcribed text.
    '''
    def __call__(self, audio, sample_rate, sample_width, channels):
        audio_array = None

        if sample_width == 1:
            audio_array = np.frombuffer(audio, dtype=np.int8)
        elif sample_width == 2:
            audio_array = np.frombuffer(audio, dtype=np.int16)

        if channels == 2:
            audio_array = (audio_array.reshape([int(audio_array.shape[0]/2), 2])/2).sum(1)

        audio_array = np.interp(np.arange(0, len(audio_array), float(sample_rate)/16000), np.arange(0, len(audio_array)), audio_array)
        audio_array = audio_array.flatten().astype(np.float32)

        if sample_width == 1:
            audio_array = audio_array / 64.0
        elif sample_width == 2:
            audio_array = audio_array / 32768.0

        logging.debug(f"Got transcription request.")
        # result = self.model.transcribe(working_filename, language='English')
        result = self.model.transcribe(audio_array, language='English')
        logging.debug(f"Got transcription result: {result}")
        return result["text"]