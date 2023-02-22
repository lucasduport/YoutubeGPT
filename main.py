import youtube_api as yt
import openai_api as op
import text_to_speach as tts

def __main__():
    youtube_link = input("Enter a youtube link: ")
    video_id = yt.getVideoId(youtube_link)
    transcript = yt.getTranscriptText(video_id)

    summary = ""
    for text in transcript:
        summary_piece = "zizi" #op.summarize(text)
        summary += summary_piece

    tts.speak(summary_piece)

__main__()