import sounddevice as sd
from vosk import Model, KaldiRecognizer, SetLogLevel
import numpy as np
import json

SetLogLevel(-1)

duration = 5
fs = 16000
channels = 1

model = Model("model_small")
rec = KaldiRecognizer(model, fs)

while True:
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=channels, dtype='int16')
    sd.wait()
    recording_np = np.array(recording)

    rec.AcceptWaveform(recording_np.tobytes())
    
    result = rec.PartialResult()
    if "здравствуйте" in result:
        pass

    if result:
        print(json.loads(result))
    
    if rec.FinalResult():
        print(json.loads(rec.FinalResult()))
