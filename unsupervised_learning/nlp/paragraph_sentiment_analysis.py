import nltk
from nltk import word_tokenize
import module1 as m
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('vader_lexicon')

# filename = input("Enter file name : ")
# filename = 'sample_file'
filename = 'sad'

content = m.read_textfile(filename)

# words = word_tokenize(content)            # word tokenize

# print(words)

sia = SentimentIntensityAnalyzer()

score = sia.polarity_scores(content)
print("-"*60)
print("Word Score : ",score)
print("-"*60)
if score['compound'] >= 0.5:
    print("Sentence is Positive :) ")
elif score['compound'] <= -0.5:
    print("Sentence is Negative :(")
else:
    print("Sentence is Neutral")

print("-"*60)