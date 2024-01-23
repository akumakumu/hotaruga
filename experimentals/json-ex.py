import json

# Object to JSON
x = {
    "url": "https://x.com/2",
    "title": "Hello, two",
    "sentiment": True
}

y = json.dumps(x)

print(y)

# JSON to Object

z = json.loads(y)

print(z["url"])