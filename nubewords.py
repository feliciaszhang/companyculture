
import matplotlib.pyplot as pPlot
from wordcloud import WordCloud, STOPWORDS
import numpy as npy
from PIL import Image

def main():
    dataset = open("text_review.txt", "r").read()
    dataset = dataset.lower()
    create_word_cloud(dataset)


def create_word_cloud(string):
    maskArray = npy.array(Image.open("cloud.png"))
    cloud = WordCloud(background_color = "white", max_words = 10, mask = maskArray, stopwords = set(STOPWORDS))
    cloud.generate(string)
    cloud.to_file("wordCloud.png")

main()
