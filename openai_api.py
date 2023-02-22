import openai
import config
print(openai.__version__)

openai.api_key = config.getConfig("open_ai_key")
model = config.getConfig("model")

def use_chatGPT(prompt):
        response = openai.Completion.create(
        prompt=prompt,
        model=model,
        temperature=0.9,
        max_tokens=600,
        n=1)
        return response.choices[0].text

def summarize(to_summarize, output_language):
        prompt="This text is a piece of a youtube video script. Please summarize this\
extract in less than 50 words. Fais en sorte que le resultat soit fluide quand les résumés de toutes les parties de la vidéos seront assemblées.\
Ta réponse devra être en langue de codes de langue ISO 639-1: """ + output_language +".\n" + to_summarize
        return use_chatGPT(prompt)