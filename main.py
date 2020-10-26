import os

import requests
from flask import Flask, send_file, Response, render_template
from bs4 import BeautifulSoup as bs

app = Flask(__name__)

# helpful docs
# https://www.w3schools.com/python/ref_requests_post.asp
# https://www.w3schools.com/python/ref_requests_response.asp

# to use
# cd C:/Users/swatm/Documents/Python230/assignment-05/ustjay-ethay-actsfayig/
# python main.py
# http://localhost:6787/

def get_fact()->str:
    '''collects fact from a website'''
    response = requests.get("http://unkno.com")
    # response.content is the whole page in html format with \n and \r
    soup = bs(response.content, "html.parser")
    # soup is now the human readable format of the html doc
    facts = soup.find_all("div", id="content")
    # facts is now a list of the found items

    # alternatively coud do just a .find() like below; this does not make a list like .find_all()
    # fact = soup.find('div', id='content')
    return facts[0].getText()
    # return fact.getText().strip()

def piggyize()->tuple:
    fact = get_fact()
    payload = {'input_text': fact}
    piggy_site = 'https://hidden-journey-62459.herokuapp.com/piglatinize/'
    response = requests.post(piggy_site, data=payload, allow_redirects=False)
    piggy_link = response.headers['Location']
    return fact, piggy_link

@app.route('/')
def home()->'html':
    data = piggyize()   #data = fact, piggy_link
    return render_template('base.jinja2', hyper_link=data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)
