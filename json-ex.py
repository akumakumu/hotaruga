import json

x = {
    "url": "https://x.com/2",
    "title": "Hello, two",
    "sentiment": True
}

print(json.dumps(x))