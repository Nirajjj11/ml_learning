import os 
import nltk
from nltk import sent_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

file = input("Enter the name of the File : ")
file += '.txt'
f = open(file ,'r')
content = f.read()          # read from begg. to end

s_tokenize = sent_tokenize(content)

print("Original Content in ", content)
print("Sentence tokenize")
print(s_tokenize)
print("No of sentences = ",len(s_tokenize))