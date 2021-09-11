import playsound
from gtts import gTTS
import os

location = os.path.dirname(os.path.abspath(__file__))

def speakLine(input_string):
    tts = gTTS(input_string, lang='fi')
    audio_file = location + "/s2t-audio.mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
    os.remove(audio_file)