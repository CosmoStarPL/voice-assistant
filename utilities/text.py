from gtts import gTTS

import utilities.audio


def say(text):
    file_path = "assets/audio/generated_audio.mp3"
    language = 'ru'

    tts = gTTS(text=text, lang=language)
    tts.save(file_path)

    utilities.audio.play(file_path, False)
