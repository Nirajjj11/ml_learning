# Q. WAP to read a textfile from the user and count no of words in the file.

from nltk import word_tokenize
import module1 as m
import nltk

nltk.download("punkt")
nltk.download("punkt_tab")

filename = input("Emter file name : ")
# filename += ".txt"
# f = open(filename,'r')

content = m.read_textfile(filename)

word = word_tokenize(content)

print("Orginal Text : \n",content)
print("-"*40)
print("Word Tokenize List : ", word)
print("Total no of words : ",len(word))