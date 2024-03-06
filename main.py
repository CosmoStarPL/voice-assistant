import requests
import sounddevice as sd
from vosk import Model, KaldiRecognizer, SetLogLevel
import numpy as np

import json

import utility_text
import utility_audio
import utility_video

SetLogLevel(-1)

duration = 5
fs = 16000
channels = 1

model = Model("model_small")
recognizer = KaldiRecognizer(model, fs)

default_phrase = "здравствуйте"
default_reply = "ну здравствуй"

url = "https://webulu.uz/voice/source.json"
content = {}


def main_online():
    if content["prefer"] == 0:
        utility_text.say(content["sources"]["text"])
    elif content["prefer"] == 1:
        utility_audio.play(content["sources"]["audio"])
    elif content["prefer"] == 2:
        utility_video.play(content["sources"]["video"])


def main_offline():
    utility_text.say(default_reply, False)


def check_internet():
    global content
    try:
        response = requests.get(url)
        content = json.loads(response.content)
        return True
    except requests.RequestException:
        return False


while True:
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=channels, dtype='int16')
    sd.wait()
    recording_np = np.array(recording)

    recognizer.AcceptWaveform(recording_np.tobytes())
    result = recognizer.FinalResult()

    if check_internet() and content["powered"] and content["phrase"] in result:
        main_online()
    elif default_phrase in result:
        main_offline()
