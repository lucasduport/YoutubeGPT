import config
from openai import OpenAI

client = OpenAI(
        api_key=config.getConfig('open_ai_key')
)

def summarize(to_summarize, output_language):
        prompt="This text is a piece of a youtube video script. Please summarize this\
extract in 500 words maximum. The result muste be a fluid presentation that will be spoken.\
You must answer in this language (IETF): """ + output_language +".\n" + to_summarize
        return use_chatGPT(prompt)


def use_chatGPT(prompt):
        response = client.chat.completions.create(
        model=config.getConfig('text_model'),
        messages=[
        {"role": "system", "content": prompt}
        ],
        temperature=0.9,
        max_tokens=5000,
        n=1
        )        
        return response.choices[0].message.content

def use_text_to_speech(text):
        print("Asking wishper form openAI to read the text.")
        response = client.audio.speech.create(
        model=config.getConfig('audio_model'),
        voice="alloy",
        input=text
        )
        return response
