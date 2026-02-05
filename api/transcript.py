from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
from urllib.parse import parse_qs, urlparse
import json

def extract_video_id(url):
    query = urlparse(url)
    if query.hostname in ["www.youtube.com", "youtube.com"]:
        return parse_qs(query.query).get("v", [None])[0]
    if query.hostname == "youtu.be":
        return query.path[1:]
    return None

def handler(request):
    video_url = request.args.get("url")
    if not video_url:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Missing video URL"})
        }

    video_id = extract_video_id(video_url)
    if not video_id:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Invalid YouTube URL"})
        }

    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        formatter = TextFormatter()
        text = formatter.format_transcript(transcript)

        return {
            "statusCode": 200,
            "body": json.dumps({
                "video_id": video_id,
                "transcript": text
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
