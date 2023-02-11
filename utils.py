# Imports
import nltk
from nltk.stem.porter import PorterStemmer

# Creating an instance of the Porter Stemmer
stemmer = PorterStemmer()

# Tokenizer
# Seperates a sentence into words and returns it in the form of a list


def tokenizer(sentence):
    return nltk.word_tokenize(sentence)

# Stemmer
# Cuts down a specific word to its root form after lowercasing it.


def wordStemmer(word):
    return stemmer.stem(word.lower())


def feature_vector_converter(tokenized_sentence, bag_of_words):
    pass
