import requests

text = "I love python"

url = "http://127.0.0.1:5000?q={}".format(text)

response = requests.request("GET", url, data=text)

print(response.text)

"""
To be implemented:
A method that extracts only the feedback from the sentiment analysis. 
Ex: Positive/Negative, without JSON format.
"""
