# Sentiment_API_Testing

The tested API is used to analyze the sentiment of a message and rate it as a Positive or Negative Message

## API Usage

Using GET method -

    http://127.0.0.1:5000?q="Text String to check Sentiment."
Using POST method -

    curl http://127.0.0.1:5000 -d "q='Text String to check Sentiment.'"
or use in a web based form and send POST request.

### Output

Output is JSON based which is as follows -

    {"sentiment":"Negative"}
or

    {"sentiment":"Positive"}

## Requirements

All resources needed can be installed via the requirements.txt file, that will also include flask and nltk

## Testing methods

- For all tests have been applied functional testing methodology.
- All test have been written with Pytest and a Html report have been generated.

## Utilities

All misc tasks such as generating reports or running the Flask server have been automated with powershell/batch scripts for ease of use

## To be implemented

- A new API demo that goes in depth with the capabilities
- a GUI for the demo to show the portability
