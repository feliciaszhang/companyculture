from flask import Flask, render_template, redirect, request, url_for
import urllib2
from bs4 import BeautifulSoup
import matplotlib.pyplot as pPlot
from wordcloud import WordCloud, STOPWORDS
import numpy as npy
from PIL import Image

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        company = request.form.get("company")
        return redirect(url_for('result', company=company))
    else:
        return render_template("input.html")

@app.route("/result/<company>")
def result(company):
    review_page = "https://www.indeed.com/cmp/{}/reviews".format(company)
    page = urllib2.urlopen(review_page)
    html = page.read()
    soup = BeautifulSoup(html, 'html.parser')
    review_text = soup.find_all('div', attrs={'class':'cmp-Review-text'})
    data = []
    dataText = ""
    for x in review_text:
        span = x.select('span')[0]
        data.append(span.text)
        dataText += x.text
    dataText = dataText.lower()
    create_word_cloud(dataText, company)
    return render_template("result.html", data=data, company=company)


def create_word_cloud(string, company):
    maskArray = npy.array(Image.open("bg.png"))
    cloud = WordCloud(background_color = "white", max_words = 10, mask = maskArray, stopwords = set(STOPWORDS))
    cloud.generate(string)
    cloud.to_file("{}.png".format(company))

    

if __name__ == "__main__":
    app.run(debug=True)