# OpenAI Whisper STT Component by LCC

## What is this for?
Uses [OpenAI Whisper](https://github.com/openai/whisper) to perform transcription on incoming audio bytes using their local models.

## Setup

Checkout [OpenAI's repo](https://github.com/openai/whisper) for more specific setup instructions. Make sure to install pytorch specific to your machine from [their official install page](https://pytorch.org/get-started/locally/)

Windows
```
conda create -n jaison-comp-stt-openai-whisper python=3.12 pytorch-cuda
conda activate jaison-comp-stt-openai-whisper
# pytorch install command like pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126
pip install -r requirements.txt
```

Unix
```
python -m venv venv
source venv/bin/activate
# pytorch install command like pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126
pip install -r requirements.txt
```

## Testing
Assuming you are in the right virtual environment and are in the root directory:
```
python ./src/main.py --port=5000
```
If it runs, it should be fine.

## Configuration
`model` refers to one of [OpenAI's Whisper](https://github.com/openai/whisper?tab=readme-ov-file#available-models-and-languages) models such as `turbo` or `tiny.en`. Default `turbo` is recommended if you have the specs.

`prompt` gives additional information to start. This can help with spelling complicated words or names like "J.A.I.son".

`no_speech_threshold` adjusts sensitivity of voice detection and transcription. Lower is more sensitive and thus more likely to produce a word on some noise.

## Related stuff

Project J.A.I.son: https://github.com/limitcantcode/jaison-core

Join the community Discord: https://discord.gg/Z8yyEzHsYM
