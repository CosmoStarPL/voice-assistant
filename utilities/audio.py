import requests
import sounddevice as sd
import soundfile as sf


def play(audio_path, is_url=True):
    if is_url:
        file_path = "assets/audio/downloaded_audio.mp3"
        response = requests.get(audio_path)
        with open(file_path, 'wb') as file:
            file.write(response.content)
        data, sample_rate = sf.read(file_path)
    else:
        data, sample_rate = sf.read(audio_path)

    sd.play(data, sample_rate)
    sd.wait()
