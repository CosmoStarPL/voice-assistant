import requests
import sounddevice as sd
from vosk import Model, KaldiRecognizer, SetLogLevel
import numpy as np

import json

import utilities.text
import utilities.audio
import utilities.video

SetLogLevel(-1)

duration = 5
fs = 16000
channels = 1

model = Model("model_small")
recognizer = KaldiRecognizer(model, fs)

default_phrase = "здравствуйте"

url = "https://webulu.uz/voice/source.json"
content = {}


def main_online():
    if content["prefer"] == 0:
        utilities.text.say(content["sources"]["text"])
    elif content["prefer"] == 1:
        utilities.audio.play(content["sources"]["audio"])
    elif content["prefer"] == 2:
        utilities.video.play(content["sources"]["video"])


def main_offline():
    utilities.audio.play("assets/audio/default_audio.mp3", False)


def check_internet():
    try:
        global content
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

    if "закрой браузер" in result:
        if content != {} and content["prefer"] == 2:
            utilities.video.quit()
        else:
            utilities.text.say("Нет запущенных окон браузера")

    if check_internet() and content["powered"] and content["phrase"] in result:
        main_online()
    elif default_phrase in result:
        main_offline()
