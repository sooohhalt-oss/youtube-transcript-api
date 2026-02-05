import json

def handler(request):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "debug": "OK",
            "source": "vercel-python-builds"
        })
    }
