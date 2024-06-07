# YoutubeGPT

A youtube video summarizer using ChatGPT and Youtube APIs.
**Generate a short mp3 file of the summarized video in ANY languages with a [Youtube](youtube.com) link**

## Config file
You have to create your own OpenAI api key [here](https://platform.openai.com/account/api-keys) and replace it in `config.py` file.

## Run the code

`pip install -r requirements.txt`

`python3 main.py <youtube_link> <language> <output_filename='output.mp3'>`

## Example:

`python3 main.py https://youtu.be/AyOnug-3OKM es out.mp3`

Languages are given in format [IETF language tag](https://en.wikipedia.org/wiki/IETF_language_tag)

## Good to know

I used to split the transcript into several pieces because the context length of openAI api was not big enough to handle a whole video transcript.
No need to do it anymore thanks to massive gen ai improvements in less than a year !!!

## Improvements

I should have use JSON to store config and import API key form shell envrionment variable. I will do it sometime.
I could take an optional parameter of how long the output file should be.

## Changelog:
- *06/07/24:*
  - Removed gTTS library usage to use openAI text to speech model.
  - Now compatible with new version of openAI lib.
  - You can now set an output file, if not, it will be name "output.mp3"
  - Updated README
