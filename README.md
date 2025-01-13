# OpenAI Whisper STT Component by LCC

## What is this for?
Uses [OpenAI Whisper](https://github.com/openai/whisper) to perform transcription on incoming audio bytes using their `turbo` model.

## Setup

For either setup, also ensure you have [ffmpeg](https://ffmpeg.org/) installed. Checkout [OpenAI's repo](https://github.com/openai/whisper) for more specific setup instructions.

Windows
```
conda create -n jaison-comp-stt-openai-whisper python=3.12
conda activate jaison-comp-stt-openai-whisper
pip install -r requirements.txt
```

Unix
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Testing
Assuming you are in the right virtual environment and are in the root directory:
```
python ./src/main.py --port=5000
```
If it runs, it should be fine.

## Configuration
There is no configuration.

## Related stuff
Project J.A.I.son: https://github.com/limitcantcode/jaison-core
Join the community Discord: https://discord.gg/Z8yyEzHsYM
