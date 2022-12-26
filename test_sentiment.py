import requests


def test_run_server():
    text = "test"
    url = "http://127.0.0.1:5000?q={}".format(text)
    response = requests.request("GET", url, data=text)
    assert response.status_code == 200

def test_get_response():
    text = "test"
    url = "http://127.0.0.1:5000?q={}".format(text)
    response = requests.request("GET", url, data=text)
    assert response.text.isascii() is True

def test_get_response_NoArgs():
    text = ""
    url = "http://127.0.0.1:5000?q={}".format(text)
    response = requests.request("GET", url, data=text)
    assert response.text.isalnum() is False

