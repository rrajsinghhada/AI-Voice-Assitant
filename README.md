# DEE-The-Assistant
## Running on native machine
### dependencies
* python3
* portaudio (for recording with pyaudio to work)
* [ctcdecode](https://github.com/parlance/ctcdecode) - for speechrecognition

If you're on mac you can install `portaudio` using `homebrew`

**NOTICE: If you are using windows, some things may not work. For example, torchaudio. I suggest trying this on linux or mac, or use wsl2 on windows**

### using virtualenv (recommend)
1. `virtualenv voiceassistant.venv`
2. `source voiceassistant.venv/bin/activate`

### pip packages
`pip install -r requirements.txt` 
