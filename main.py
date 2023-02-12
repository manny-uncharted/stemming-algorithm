import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

from py.tokenization import DummyTokenizer
from py.lemmatization import DictionaryLemmatizer
from py.stemming import PorterStemmer


def train_tokens(text):
    tokenizer = DummyTokenizer(text)
    tokens = tokenizer.tokens
    lemmatizer = DictionaryLemmatizer()
    lemmas = [lemmatizer.lemmatize(token, None) for token in tokens]
    stemmer = PorterStemmer()
    stems = [stemmer.stem(lemma) for lemma in lemmas]
    result = list(zip(tokens, stems))
    return result

def tokens(text):
    tokenizer = DummyTokenizer(text)
    tokens = tokenizer.tokens
    return tokens

def lovins_stemmer(word):
    # Vectorize the input word
    word = vectorizer.transform([word])
    # Use the trained classifier to predict the base form of the word
    prediction = classifier.predict(word)[0]
    print(prediction)


if __name__ == "__main__":
    print("Let's train our classifier on some list of words and their stems")
    # text = input("Enter a paragraph: ")
    # result = train_tokens(text)

    # Load a dataset of words and their base forms
    results = [("dance", "dance",), ("dancing", "dance"), ("danced", "dance"),("dancer", "dance"),]

    # # Split the dataset into input and output
    X, y = zip(*results)

    # Vectorize the input words using a bag-of-words model
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(X)
    # Train a Naive Bayes classifier on the dataset
    classifier = MultinomialNB()
    classifier.fit(X, y)

    # Test the classifier
    text = str(input("Enter a paragraph: "))
    # tokens = tokens(text)
    lovins_stemmer(text)