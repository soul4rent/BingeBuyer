from amazon.api import AmazonAPI
from nltk.corpus import wordnet
from pytube import YouTube

#FIRST TIME USAGE: MUST DOWNLOAD DICTIONARY
#import nltk
#nltk.download('wordnet')

ytlink = input("Youtube Link:")
yt = YouTube(ytlink)
caption = yt.captions.get_by_language_code('en')
print(caption.generate_srt_captions()) #youtube captions




nouns = {x.name().split('.', 1)[0] for x in wordnet.all_synsets('n')}
#create set of nouns

#TODO: LIST NOUNS IN CAPTIONS
print("test" in nouns)
