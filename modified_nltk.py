from nltk.sentiment.vader import SentimentIntensityAnalyzer
import statistics
import numpy as np
import pandas as pd

sents = ["This is a good test!.",
         "This is a bad test. ", "bad, bad, hate bad awful, sucks",
         "love", "love lvoe love love love"]
sid = SentimentIntensityAnalyzer()


dataset = []
for sentence in sents:
    print(f"sentence = {sentence} \n")
    ss = sid.polarity_scores(sentence)
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]), end='')
    dataset.append(ss["compound"])
    print('\n')
#standard deviation
standev = statistics.stdev(dataset)
print(standev)
if (standev > 0 and standev <1):
    print("Reviews are very consistent")
elif(standev > 1 and standev < 2):
    print("Reviews are consistent with some variety")
else:
    print("Reviews are very mixed")

#remove outliers
print(dataset)
dataset= sorted(dataset)
q1, q3= np.percentile(dataset,[25,75])
iqr = q3 - q1
lower_bound = q1 -(1.5 * iqr) 
upper_bound = q3 +(1.5 * iqr)

for y in dataset:
    if(y>upper_bound or y<lower_bound):
        print(y)
        dataset.remove(y)
print(dataset)

    
#is overall score positive or negative?
overallscore = 0.0
for i in range(len(dataset)):
    overallscore += dataset[i]

print(overallscore)
print("Overall score = " + str(overallscore))
if(overallscore > 0):
    print("Overall review is positive")
else:
    print("Overall score is negative")
print("finished")
