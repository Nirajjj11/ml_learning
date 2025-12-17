import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

sentence = input("Enter a sentence : ")

sia = SentimentIntensityAnalyzer()
score = sia.polarity_scores(sentence)

print("Your Score is : ",score)

if score['compound'] >= 0.5:
    print("Sentence is Positive :) ")
elif score['compound'] <= -0.5:
    print("Sentence is Negative :(")
else:
    print("Sentence is Neutral")