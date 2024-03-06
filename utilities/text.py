from gtts import gTTS
import sounddevice as sd
import soundfile as sf


def say(text, is_online=True):
    file_path = "../sounds/sound.mp3"
    language = 'ru'

    if is_online:
        tts = gTTS(text=text, lang=language, slow=False)
        tts.save(file_path)
    else:
        data, sample_rate = sf.read("../sounds/default_sound.mp3")
        sd.play(data, sample_rate)

    data, sample_rate = sf.read(file_path)
    sd.play(data, sample_rate)
    sd.wait()
