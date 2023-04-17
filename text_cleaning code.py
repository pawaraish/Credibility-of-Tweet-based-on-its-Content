
import numpy as np
from matplotlib import pyplot as plt

ys = 200 + np.random.randn(100)
x = [x for x in range(len(ys))]

plt.plot(x, ys, '-')
plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='g', alpha=0.6)

plt.title("Sample Visualization")
plt.show()


import nltk

from nltk.stem.porter import *
stemmer = PorterStemmer()
tokens = ['DIRECTS', 'COMPENSATION', 'PETITIONER', 'CLEANED','LAKHS']
for token in tokens:
    print(token + ' --> ' + stemmer.stem(token))

#Rule based pos tagging
patterns = [
     (r'.*ing$', 'VBG'),               # gerunds
     (r'.*ed$', 'VBD'),                # simple past
     (r'.*es$', 'VBZ'),                # 3rd singular present
     (r'.*ould$', 'MD'),               # modals
     (r'.*\'s$', 'NN$'),               # possessive nouns
     (r'.*s$', 'NNS'),                 # plural nouns
     (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),  # cardinal numbers
     (r'the', 'DT'),                   # Determiner
     (r'in','IN'),                     # preposition
     (r'.*', 'NN')                     # nouns (default)
]
from nltk import RegexpTagger
regexp_tagger = nltk.RegexpTagger(patterns)
#3.Tag a sentence. Note that the string, which contains the sentence must be segmented into words
regexp_tagger.tag("122346".split())

# import TweetTokenizer() method from nltk
from nltk.tokenize import TweetTokenizer
 
# Create a reference variable for Class TweetTokenizer
tk = TweetTokenizer()
 
# Create a string input
gfg = "(###this is me)"
 
# Use tokenize method
geek = tk.tokenize(gfg)
 
print(geek)

import nltk
nltk.download('stopwords')
  
from nltk.corpus import stopwords
sw_nltk = stopwords.words('english')
#print(sw_nltk)
text = "When I first met her she was very quiet. She remained quiet during the entire two hour long journey from Stony Brook to New York."
words = [word for word in text.split() if word.lower() not in sw_nltk]
new_text = " ".join(words)
print(new_text)
print("Old length: ", len(text))
print("New length: ", len(new_text))

def to_lowercase(text):
    return text.lower()
print("Learning NLP is Fun....")

import re 
def remove_url(text):
 return re.sub(r’https?:\S*’, ‘’, text)
print(remove_url('using https://www.google.com/ as an example'))

import contractions
def expand_contractions(text):
    expanded_words = [] 
    for word in text.split():
       expanded_words.append(contractions.fix(word)) 
    return ‘ '.join(expanded_words)
print(expand_contractions("Don't is same as do not"))

import re
def remove_mentions_and_tags(text):
    text = re.sub(r’@\S*’, ‘’, text)
    return re.sub(r’#\S*’, ‘’, text)
#testing the function on a single sample for explaination
print(remove_mentions_and_tags('Some random @abc and#def'))

import re
def remove_special_characters(text):
    # define the pattern to keep
    pat = r'[^a-zA-z0-9.,!?/:;\"\'\s]' 
    return re.sub(pat, '', text)
 
print(remove_special_characters(“007 Not sure@ if this % was #fun! 558923 What do# you think** of it.? $500USD!”))

# imports
import re 
def remove_numbers(text):
    pattern = r'[^a-zA-z.,!?/:;\"\'\s]' 
    return re.sub(pattern, '', text)
 
print(remove_numbers(You owe me 1000 Dollars))

import string
def remove_punctuation(text):
    return ''.join([c for c in text if c not in string.punctuation])
    
remove_punctuation('On 24th April, 2005, "Me at the zoo" became the first video ever uploaded to YouTube.')