import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# Define a function for preprocessing a tweet
def preprocess_tweet(tweet):
    # Convert to lowercase
    tweet = tweet.lower()

    # Remove URLs
    tweet = re.sub(r'http\S+', '', tweet)

    # Remove special characters and punctuation
    tweet = re.sub(r'[^\w\s]', '', tweet)

    # Tokenize the tweet
    tokens = word_tokenize(tweet)

    # Remove stop words
    stop_words = set(stopwords.words("english"))
    tokens = [word for word in tokens if word not in stop_words]

    return tokens


# Example tweet
tweet = "This is a sample tweet for #Preprocessing! Check out my blog: https://www.example.com"

# Preprocess the tweet
tokens = preprocess_tweet(tweet)

print(tokens)