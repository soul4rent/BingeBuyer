from amazon.api import AmazonAPI
from nltk.corpus import wordnet

#FIRST TIME USAGE: MUST DOWNLOAD DICTIONARY
#import nltk
#nltk.download('wordnet')


nouns = {x.name().split('.', 1)[0] for x in wordnet.all_synsets('n')}
#create set of nouns

print("test" in nouns)
