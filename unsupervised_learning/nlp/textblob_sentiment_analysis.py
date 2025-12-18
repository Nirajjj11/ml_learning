# Q. WAP to take a sentence and deside the positive , negative or neutral

from textblob import TextBlob

sent = input("Enter your text : ")
blob = TextBlob(sent)

polarity_score = blob.sentiment.polarity

print("Polarity Score : ",polarity_score)

if polarity_score >= 1:
    print("Positive Mood sentence :)")
elif polarity_score <1 :
    print("Negative mood Sentence :(")
else:
    print("Neural Mood Sentence ")