from youtube_transcript_api import YouTubeTranscriptApi
import config

def getTranscript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=config.getConfig("languages"))
    return transcript

def getTranscriptText(video_id):
    transcript = getTranscript(video_id)
    if transcript is None:
        raise Exception("Unable to find transcript")
    
    transcript_list = [""]
    nb_char = 0
    request_num = 0
    for line in transcript:
        nb_char += len(line['text']) + 1
        if nb_char > 1000:
            nb_char = 0
            request_num += 1
            transcript_list.append("")
        
        transcript_list[request_num] += line['text'] + " "
    if request_num > 10:
        raise Exception("Transcript is too long with length over " + str(request_num*1000) + " characters.")
    return transcript_list

def getVideoId(youtube_link):
    video_id = youtube_link.split("v=")
    if len(video_id) > 1:
        return video_id[1]
    video_id = youtube_link.split("youtu.be/")
    if len(video_id) > 1:
        return video_id[1]
    
    raise Exception("Unable to find video id")