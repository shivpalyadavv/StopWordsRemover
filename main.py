import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt')

text = "At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills)."
tokens = word_tokenize(text)
tokenization = [word for word in tokens if not word in stopwords.words('english')]
print(tokens)
print(tokenization)