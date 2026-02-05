from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import json

def handler(request):
    video_id = request.args.get("videoId")

    if not video_id:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "success": False,
                "error": "Use: /api/transcript?videoId=VIDEO_ID"
            })
        }

    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

        transcript = transcript_list.find_transcript(['de', 'en'])
        transcript_data = transcript.fetch()

        formatter = TextFormatter()
        text = formatter.format_transcript(transcript_data)

        return {
            "statusCode": 200,
            "body": json.dumps({
                "success": True,
                "videoId": video_id,
                "transcript": text
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "success": False,
                "videoId": video_id,
                "error": str(e),
                "transcript": None
            })
        }
