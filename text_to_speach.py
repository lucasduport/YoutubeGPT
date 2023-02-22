from gtts import gTTS
  
def save(text, language):
    myobj = gTTS(text=text, lang=language, slow=False)
    myobj.save("output.mp3")
