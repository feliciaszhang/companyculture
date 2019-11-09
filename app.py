from flask import Flask, render_template, redirect, request, url_for
import urllib2
from bs4 import BeautifulSoup
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
    soup = BeautifulSoup(page, 'html.parser')
    review_text = soup.find_all('div', attrs={'class':'cmp-Review-text'})
    data = []
    for x in review_text:
        data.append(x.text)
    return render_template("result.html", data=data, company=company)

if __name__ == "__main__":
    app.run()