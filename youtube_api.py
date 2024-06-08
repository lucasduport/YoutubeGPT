from youtube_transcript_api import YouTubeTranscriptApi
import config

def getTranscriptText(video_id):

    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=config.getConfig("languages"))
    if transcript is None:
        raise Exception("Unable to find transcript")
    maxNum = 10000

    content = ""
    for line in transcript:
        content += line['text'] + " "

    return content

def getVideoId(youtube_link):

    video_id = youtube_link.split("v=")
    if len(video_id) > 1:
        return video_id[1]
    video_id = youtube_link.split("youtu.be/")
    if len(video_id) > 1:
        return video_id[1]
    
    raise Exception("Unable to find video id")
