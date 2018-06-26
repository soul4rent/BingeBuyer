from amazon.api import AmazonAPI
from nltk.corpus import wordnet
from pytube import YouTube
import re

#FIRST TIME USAGE: MUST DOWNLOAD DICTIONARY
#import nltk
#nltk.download('wordnet')

ytlink = input("Youtube Link:")
yt = YouTube(ytlink)
caption = yt.captions.get_by_language_code('en')
justTextCaption = re.sub("[<].*?[>]", " ", caption.generate_srt_captions())
#Because regex is easy to write and impossible to read sometimes:
#- Match a single character "<" ( [<] )
#- Match any character ( . ), 0-infinite times ( * ), lazily, AKA NOT GETTING EVERYTHING ( ? )
#- Match a single character ">" ( [>] )


#noTag Captions
print(justTextCaption) #youtube captions


print("-Generating list of nouns from dictionary")

nouns = {x.name().split('.', 1)[0] for x in wordnet.all_synsets('n')}
#create set of nouns

#TODO: LIST NOUNS IN CAPTIONS
print("-Generating caption list")
captionList = re.split('\n|[ ]',justTextCaption)
print(captionList)

for word in captionList:
    if (word in nouns):
        print(word + " ::: SUCCESS!")
