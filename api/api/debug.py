import json

def handler(request):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "debug": "THIS IS A NEW ROUTE",
            "status": "ok"
        })
    }
