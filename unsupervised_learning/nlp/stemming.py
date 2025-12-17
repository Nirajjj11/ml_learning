# WAP to load a text file and use stemming over each word of located text file

import module1 as m
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import nltk

nltk.download("punkt")
print("-"*60)
filename = input("Enter file name : ")
content = m.read_textfile(filename)

word = word_tokenize(content)
print("-"*60)
print("Original text : ",content)
print("-"*60)
print("Word Tokenize List is : ",word)
print("-"*60)
print("Total no of words : ",len(word))
print("-"*60)

stem = PorterStemmer()
print("Steeming word List : ")
for w in word:
    print(stem.stem(w) , end=" ")

print("\n","-"*60)
