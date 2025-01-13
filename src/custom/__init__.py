'''
Supported component type entrypoints

- Implement the specific entrypoint associated with your component type
- You can leave the others unimplemented

To support streaming, your implementation should be a generator: https://wiki.python.org/moin/Generators
You may also simply return the final result
'''
'''
This class is responsible for transcribing audio
from wave files.
'''

from .model import STTModel
stt_model = STTModel()

# For speech-to-text models
def start_stt(audio: bytes) -> str:
    global stt_model
    return stt_model(audio)

# For text generation models
def start_t2t(system_prompt: str, user_input: str) -> str:
    raise NotImplementedError

# For text-to-speech generation
def start_ttsg(text: str) -> bytes:
    raise NotImplementedError

# For voice changers
def start_ttsc(audio: bytes) -> bytes:
    raise NotImplementedError