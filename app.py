from flask import Flask, render_template, redirect, url_for, request
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as pPlot
from wordcloud import WordCloud, STOPWORDS
import numpy as npy
from PIL import Image
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import numpy as np
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet



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
    filtered = filter(dataText)
    import os
    if os.path.isfile('static/company.png'):
        os.remove("static/company.png")
    create_word_cloud(filtered, company)
    result = analyze(data)
    values = value(dataText)
    return render_template("result.html", result=result, values=values, company=company)

def filter(dataText):
    result = ''
    listofwords = word_tokenize(dataText)
    listoftagged = nltk.pos_tag(listofwords)
    tags = set(['JJ', 'JJR', 'JJS'])
    for word in listoftagged:
        if word[1] in tags:
            result += word[0] + " "
    return result



def analyze(data):
    sid = SentimentIntensityAnalyzer()
    dataset = []
    endData = {}
    endReview = {}
    for sentence in data:
        ss = sid.polarity_scores(sentence)
        for k in sorted(ss):
            rev = '{}: {}, '.format(k, ss[k])
            endReview[sentence] = rev
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
    return [endData, endReview]



def create_word_cloud(string, company):
    maskArray = npy.array(Image.open("bg.png"))
    cloud = WordCloud(background_color = "white", max_words = 15, mask = maskArray, stopwords = set(STOPWORDS))
    cloud.generate(string)
    cloud.to_file("static/company.png")



def value(dataText):
    content = dataText


    company_values = ["integrity", "Boldness","Honesty", "Trust", "Accountability","Passion", "Fun", "Humility", "Learning", "Ownership","Growth","Leadership","Diversity", "Innovation", "Teamwork"]
    integrity_words = "integrity high-mindedness honor incorruptibility irreproachability right-mindedness scrupulosity scrupulousness appropriateness correctness decorousness decorum etiquette fitness ethics morals character decency goodness honesty morality probity rectitude righteousness rightness uprightness virtue virtuousness ".split()
    boldness_words = "boldness adventuresome adventurous audacious daring dashing emboldened enterprising free-swinging wild brave courageous dauntless fearless gallant greathearted heroic intrepid lionhearted stalwart stout stouthearted swashbuckling unafraid undaunted valiant valorous".split()
    honesty_words = "honesty probity truthfulness veracity verity honor honorableness incorruptibility rectitude righteousness right-mindedness scrupulosity scrupulousness uprightness artlessness candidness candor good faith sincerity  dependability reliability trustability trustiness trustworthiness accuracy authenticity correctness genuineness truth credibility".split()
    trust_words = "trust confidence credence faith stock acceptance assurance assuredness certainty certitude conviction positiveness sureness surety credit dependence hope reliance".split()
    acc_words = "accountability answerability liability responsibility reliable".split()
    passion_words = "passion affection attachment devotedness devotion love ardor eagerness enthusiasm fervor zeal appreciation esteem estimation regard respect adoration adulation deification idolatry idolization worship allegiance faithfulness fealty fidelity loyalty steadfastness".split()
    fun_words = "fun joke jolly josh kid quip wisecrack yuk jeer mock caricature lampoon parody amuse divert entertain".split()
    humility_words = "Humility demureness down-to-earthness humbleness lowliness meekness modesty acquiescence compliance deference directness".split()
    learning_words = "learning education erudition knowledge learnedness literacy scholarship culture edification enlightenment reading bookishness pedantry".split()
    ownership_words = "ownership control enjoyment hands keeping possession authority command dominion mastery power".split()
    growth_words = "growth development elaboration evolution expansion progress progression advancement betterment improvement perfection refinement enhancement evolvement".split()
    leadership_words = "leadership mentor mentorship direction generalship governance lead management guidance".split()
    diversity_words = "diversity inclusivity access inclusive diverse".split()
    innovation_words = "innovation picture vision conception imagining origination creative".split()
    teamwork_words = "teamwork collaboration cooperation coordination community mutualism reciprocity solidarity".split()

    counter = [0]*len(company_values)

    for word in content.split():
        if word in integrity_words:
            counter[0] += 1
        elif word in boldness_words:
            counter[1] += 1
        elif word in honesty_words:
            counter[2] += 1
        elif word in trust_words:
            counter[3] += 1
        elif word in acc_words:
            counter[4] += 1
        elif word in passion_words:
            counter[5] += 1
        elif word in fun_words:
            counter[6] += 1
        elif word in humility_words:
            counter[7] += 1
        elif word in learning_words:
            counter[8] += 1
        elif word in ownership_words:
            counter[9] += 1
        elif word in growth_words:
            counter[10] += 1
        elif word in leadership_words:
            counter[11] += 1
        elif word in diversity_words:
            counter[12] += 1
        elif word in innovation_words:
            counter[13] += 1
        elif word in teamwork_words:
            counter[14] +=1

    x = counter
    x.sort(reverse=True)
    ranking1 = company_values[counter.index(x[0])]
    ranking2 = company_values[counter.index(x[1])]
    ranking3 = company_values[counter.index(x[2])]
    return [ranking1, ranking2, ranking3]


    

if __name__ == "__main__":
    app.run(debug=True)