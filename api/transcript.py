import json

def handler(request):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "debug": "VERCEL USES THIS CODE",
            "status": "ok"
        })
    }
