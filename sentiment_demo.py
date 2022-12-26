import requests
import json


def simple_response(text):
    to_strip = '{}"sentiment":\n '
    new_text = text.translate({ord(i): None} for i in to_strip.split())
    return new_text


text = "I lovepython, I lovepython, I lovepython, I lovepython"

url = "http://127.0.0.1:5000?q={}".format(text)

response = requests.request("GET", url, data=text)

print(response.text)
print(simple_response(response.text))
