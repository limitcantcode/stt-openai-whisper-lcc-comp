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

from custom.config import config
from .model import STTModel
stt_model = STTModel(config['model'], config['prompt'], config['no_speech_threshold'])

from jaison_grpc.common import STTComponentRequest, T2TComponentRequest, TTSGComponentRequest, TTSCComponentRequest
async def request_unpacker(request_iterator):
    async for request_o in request_iterator:
        match request_o:
            case STTComponentRequest():
                yield request_o.audio, request_o.sample_rate, request_o.sample_width, request_o.channels
            case T2TComponentRequest():
                yield request_o.system_input, request_o.user_input
            case TTSGComponentRequest():
                yield request_o.content
            case TTSCComponentRequest():
                yield request_o.audio, request_o.sample_rate, request_o.sample_width, request_o.channels
            case _:
                raise Exception(f"Unknown request type: {type(request_o)}")

# For speech-to-text models
async def start_stt(request_iterator) -> str:
    global stt_model
    audio, sample_rate, sample_width, channels = b'', 48000, 2, 2
    async for audio_chunk, sample_rate_chunk, sample_width_chunk, channels_chunk in request_unpacker(request_iterator): # receiving chunks of info through a stream
        audio += audio_chunk
        sample_rate = sample_rate_chunk
        sample_width = sample_width_chunk
        channels = channels_chunk
    yield stt_model(audio, sample_rate, sample_width, channels)

# For text generation models
def start_t2t(request_iterator) -> str:
    for system_input, user_input in request_unpacker(request_iterator): # receiving chunks of info through a stream
        raise NotImplementedError

# For text-to-speech generation
def start_ttsg(request_iterator) -> str:
    for text in request_unpacker(request_iterator): # receiving chunks of info through a stream
        raise NotImplementedError

# For voice changers
def start_ttsc(request_iterator) -> str:
    for audio, sample_rate, sample_width, channels in request_unpacker(request_iterator): # receiving chunks of info through a stream
        raise NotImplementedError