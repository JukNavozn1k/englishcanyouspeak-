from gtts import gTTS
from playsound import playsound
import os
def ENplay_text(text="This is a test message! Don't Worry Be happy!"):
    tts = gTTS(text)
    tts.save("tmp.mp3")
    playsound("tmp.mp3")
    os.remove("tmp.mp3")
def RUplay_text(text="Это тестовое сообщение! Не вольнуйтесь, будьте счастливы!"):
    tts = gTTS(text,lang='ru')
    tts.save("tmp.mp3")
    playsound("tmp.mp3")
    os.remove("tmp.mp3")
if __name__ == "__main__":
    ENplay_text()
