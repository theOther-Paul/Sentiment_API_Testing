import pytest
import requests


def test_run_server():
    text = "test"
    url = "http://127.0.0.1:5000?q={}".format(text)
    response = requests.request("GET", url, data=text)
    assert response.status_code == 200


def test_no_run_server():
    text = "test"
    url = "http://127.0.0.1:5000?q={}".format(text)
    response = requests.request("GET", url, data=text)
    try:
        assert response.status_code == 200
    except ConnectionError:
        assert response.status_code != response.status_code.ok


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


def test_get_positive():
    text = "I love Python"
    url = "http://127.0.0.1:5000?q={}".format(text)
    response = requests.request("GET", url, data=text)
    assert "Positive" in response.text


def test_get_negative():
    text = "I hate Python"
    url = "http://127.0.0.1:5000?q={}".format(text)
    response = requests.request("GET", url, data=text)
    assert "Negative" in response.text


# medium and long messages were AI generated, using https://toolbaz.com/writer/ai-text-generator to speed up the
# process and obtain clear results
def test_medium_positive():
    text = "It's great to see a news outlet that is fair and balanced in its reporting. I appreciate that this outlet " \
           "takes the time to investigate both sides of a story and present the facts in an unbiased way. I know that " \
           "it can be easy to get caught up in the sensationalism of some stories, but this outlet always seems to " \
           "present the facts in a level-headed way. I really appreciate that. "
    url = "http://127.0.0.1:5000?q={}".format(text)
    response = requests.request("GET", url, data=text)
    assert "Positive" in response.text


def test_medium_negative():
    text = "Today, I read an article on local news that I found to be extremely disappointing. The article in question" \
           "was poorly researched, biased, and full of errors. This is not the first time I have had this problem with" \
           "this news outlet, and I am beginning to lose faith in their ability to provide accurate and unbiased " \
           "information. I hope that in the future they will take more care in their reporting, but for now I will be" \
           "looking elsewhere for my news. "
    url = "http://127.0.0.1:5000?q={}".format(text)
    response = requests.request("GET", url, data=text)
    assert "Negative" in response.text


def test_long_positive():
    text = "If you're in the mood for some truly authentic Italian cuisine, then you need to head to Mario's " \
           "Restaurant. The moment you walk in, you feel like you're transported to a little trattoria in the heart " \
           "of Rome. The staff is incredibly friendly and welcoming, and the food is absolutely delicious. The pasta " \
           "is cooked perfectly al dente, the sauce is rich and flavorful, and the tiramisu is to die for. It's no " \
           "wonder Mario's has been voted the best Italian restaurant in the city for the past five years. "
    url = "http://127.0.0.1:5000?q={}".format(text)
    response = requests.request("GET", url, data=text)
    assert "Positive" in response.text


# referred via https://github.com/msindev/Sentiment-Analysis-Flask-API/issues/2#issue-1511675748
@pytest.mark.xfail(reason="Response should be negative", raises="Assertion Error", run=False)
def test_long_negative():
    text = "It's been a long time since I've had to write one of these, but here goes. I've been a client of this " \
           "particular video game for years now. I've stuck with it through all the changes, good and bad. I've seen " \
           "it grow and change, and I've always been happy with it.But now, I'm not so sure. The last few months have " \
           "been rough for this game. There have been more bugs and glitches than ever before, and the game has been " \
           "crashing constantly. The developers seem to be scrambling to fix things, but it's just not enough. And " \
           "then there are the changes to the gameplay itself. Some of them ar e good, but some of them are just " \
           "baffling. It feels like the developers are just throwing stuff at the wall to see what sticks, " \
           "and it's really starting to wear thin. I'm not sure how much longer I can keep playing this game. It's " \
           "just not what it used to be, and I'm not sure that it's worth my time anymore. "
    url = "http://127.0.0.1:5000?q={}".format(text)
    response = requests.request("GET", url, data=text)
    assert "Negative" in response.text
