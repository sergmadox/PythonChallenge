from flask import Flask
import url_from_habra
from flask import render_template
import requests
from bs4 import BeautifulSoup


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    posts = url_from_habra.get_topics()

    result = []
    for post in posts:
        request = requests.get(post)
        soup = BeautifulSoup(request.content)
        heads = soup.select('span.post__title-text')
        body = soup.select('div.post__text.post__text-html.js-mediator-article')
        result.append(heads[0].text)
        result.append(body[0].text)

    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run()
