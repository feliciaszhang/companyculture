from flask import Flask, render_template, redirect, url_for, request
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as pPlot
from wordcloud import WordCloud, STOPWORDS
import numpy as npy
from PIL import Image
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import numpy as np



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
    s = requests.session()
    review_page = "https://www.indeed.com/cmp/{}/reviews".format(company)
    page = s.get(review_page)
    soup = BeautifulSoup(page.text)
    data = []
    dataText = ""
    review_text = soup.find_all('span', class_='cmp-review-text')
    for x in review_text:
        data.append(x.text)
        dataText += x.text
    dataText = dataText.lower()
    create_word_cloud(dataText, company)
    endData = analyze(data)
    print(endData)
    return render_template("result.html", endData=endData, company=company)


def analyze(data):
    sid = SentimentIntensityAnalyzer()
    dataset = []
    endData = {}
    for sentence in data:
        ss = sid.polarity_scores(sentence)
        for k in sorted(ss):
            rev = '/n' + '{0}: {1}, '.format(k, ss[k])
            endData[sentence] = rev
        dataset.append(ss["compound"])
    #standard deviation
    standev = np.std(dataset)
    endData["standev"] = standev
    if (standev > 0 and standev <1):
        print("Reviews are very consistent")
    elif(standev > 1 and standev < 2):
        print("Reviews are consistent with some variety")
    else:
        print("Reviews are very mixed")
    #remove outliers
    dataset= sorted(dataset)
    q1, q3= np.percentile(dataset,[25,75])
    iqr = q3 - q1
    lower_bound = q1 -(1.5 * iqr) 
    upper_bound = q3 +(1.5 * iqr)
    outliers = 0
    for y in dataset:
        if(y>upper_bound or y<lower_bound):
            outliers += 1
            dataset.remove(y)
    endData["outlier"] = outliers
    #is overall score positive or negative?
    overallscore = 0.0
    for i in range(len(dataset)):
        overallscore += dataset[i]
    endData["overall"] = overallscore
    if(overallscore > 0):
        print("Overall review is positive")
    else:
        print("Overall score is negative")
    return endData



def create_word_cloud(string, company):
    maskArray = npy.array(Image.open("bg.png"))
    cloud = WordCloud(background_color = "white", max_words = 10, mask = maskArray, stopwords = set(STOPWORDS))
    cloud.generate(string)
    cloud.to_file("static/company.png")

    

if __name__ == "__main__":
    app.run(debug=True)