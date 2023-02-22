import youtube_api as yt
import openai_api as op
import text_to_speach as tts

def __main__(output_language):
    youtube_link = input("Enter a youtube link: ")
    video_id = yt.getVideoId(youtube_link)
    transcript = yt.getTranscriptText(video_id)

    summary = ""
    for text in transcript:
        summary_piece = op.summarize(text, output_language)
        summary += summary_piece

    tts.save(summary_piece, output_language)

__main__("fr")