import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import module1 as m

# Download required NLTK resources
nltk.download('punkt')
nltk.download('punkt_tab')   # for newer NLTK
nltk.download('wordnet')
nltk.download('omw-1.4')

file = input("Enter the file name : ")
content = m.read_textfile(file)

words = word_tokenize(content)

lemma = WordNetLemmatizer()

print("Lemmatized Words:")
for w in words:
    print(lemma.lemmatize(w), end = ' ')
