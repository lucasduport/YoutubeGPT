from gtts import gTTS

print(gTTS.__version__)
def save(text, language):
    myobj = gTTS(text=text, lang=language, slow=False)
    myobj.save("output.mp3")
