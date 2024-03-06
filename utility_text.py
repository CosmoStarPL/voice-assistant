from gtts import gTTS
import soundfile as sf
import sounddevice as sd

def say(text, is_online=True):
    file_name = "sound.mp3"
    language = 'ru'

    if is_online:
        tts = gTTS(text=text, lang=language, slow=False)
        tts.save(file_name)
    else:
        data, sr = sf.read("default.mp3")
        sd.play(data, sr)

    data, sr = sf.read(file_name)
    sd.play(data, sr)
    sd.wait()
