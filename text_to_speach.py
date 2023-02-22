import pyttsx3
import os
from tempfile import TemporaryDirectory
from pydub import AudioSegment

engine = pyttsx3.init()

engine.setProperty('rate', 160)  # Set the speed of speech in words per minute
engine.setProperty('volume', 0.7)  # Set the volume (min=0 and max=1)

def speak(text):
    engine.say(text)
    with TemporaryDirectory() as tmpdir:
        tmpfile = os.path.join(tmpdir, 'output.mp3')
        engine.save_to_file(text, tmpfile)
        engine.runAndWait()
        sound = AudioSegment.from_file(tmpfile, format='mp3')
        sound.export('output.mp3', format='mp3')
