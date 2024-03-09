import os

# noinspection SpellCheckingInspection
browser = "msedge.exe"


def play(video_url):
    os.system(f"start {browser} --new-window {video_url}")


def close():
    os.system(f"taskkill /im {browser} /f > nul")
