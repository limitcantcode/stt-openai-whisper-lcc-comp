import numpy as np

TARGET_SR, TARGET_SW, TARGET_CH = 16000, 4, 1

def format_audio(str_bytes, src_sr, src_sw, src_channels):
    dtype = np.dtype(f'i{src_sw}')
    audio_array = np.frombuffer(str_bytes, dtype=dtype) # parse bytes
    audio_array = (audio_array.reshape([int(audio_array.shape[0]/src_channels), src_channels])/src_channels).sum(1) # average across channels into 1 channel
    audio_array = np.interp(np.arange(0, len(audio_array), float(src_sr)/TARGET_SR), np.arange(0, len(audio_array)), audio_array) # resample
    audio_array = audio_array.flatten().astype(np.float32)
    match src_sw: # Rescale volume
        case 1:
            audio_array = audio_array / 128.0
        case 2:
            audio_array = audio_array / 32768.0
        case 4:
            audio_array = audio_array / 2147483648.0
        case _:
            raise Exception("Invalid sample width given: {src_sw}")

    return audio_array