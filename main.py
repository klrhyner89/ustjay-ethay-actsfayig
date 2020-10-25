import os

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup as bs

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")
    # response.content is the whole page in html format with \n and \r
    soup = bs(response.content, "html.parser")
    # soup is now the human readable format of the html doc
    facts = soup.find_all("div", id="content")
    # facts is now a list of the found items

    # alternatively coud do just a .find(); this does not make a list like .find_all()
    # fact = soup.find('div', id='content')
    return facts[0].getText()
    # return fact.getText().strip()

@app.route('/')
def home():
    return "FILL ME!"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

