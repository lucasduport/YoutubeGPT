import openai
import config

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

def summarize(to_summarize):
        prompt="This text is a piece of a youtube video script. Please summarize this\
extract in less than 50 words. Fais en sorte que  le resultat soit fluide quand les résumés de toutes les parties de la vidéos seront assemblées. \n" + to_summarize
        return use_chatGPT(prompt)