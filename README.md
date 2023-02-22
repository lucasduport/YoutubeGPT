# YoutubeGPT
A youtube video summarizer using ChatGPT and Youtube APIs.
Generate a short mp3 file of the summarized video in ANY languages with *only a [Youtube](youtube.com) link*

## Config file
You have to create your own openAI api key [here](https://platform.openai.com/account/api-keys) and replace it in config.py file.

## Run the code

`pip install -r requirements.txt`

`python main.py <youtube_link> <language>`

## Example:

`python main.py https://youtu.be/AyOnug-3OKM sp`

Languages are given in format [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes)


