from nltk.sentiment.vader import SentimentIntensityAnalyzer

sents = ["This is a good test!", "This is a bad test."]
sid = SentimentIntensityAnalyzer()
for sentence in sents:
    print(f"sentence = {sentence} \n")
    ss = sid.polarity_scores(sentence)
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]), end='')
    print('\n')
print("finished")
