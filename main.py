import sys
import config
import youtube_api as yt
import openai_api as op

def __main__():
    youtube_link = sys.argv[1]
    output_language = sys.argv[2]
    if len(sys.argv) > 3:
        output_filename = sys.argv[3]
    else:
        output_filename = "output.mp3"

    print("Extracting the video id from the youtube link.")
    video_id = yt.getVideoId(youtube_link)
    
    print("Asking youtube for the transcript of the video.")
    transcript = yt.getTranscriptText(video_id)

    print(f"Asking {config.getConfig('text_model')} to summarize the video script.")
    summary = op.summarize(transcript, output_language)

    print(f"Asking {config.getConfig('audio_model')} to read the summary.")
    stream = op.use_text_to_speech(summary)
    stream.with_streaming_response.method(output_filename)

if __name__ == "__main__":
    __main__()