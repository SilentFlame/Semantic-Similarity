import nltk
import extractParaphrase
from nltk.corpus import stopwords


def getSentence():
	sentence = raw_input("Text snippet: ")
	return sentence

def getWordBag(sentence):
	return (nltk.word_tokenize(sentence))


def getPreprocessedBagOfWords(sentence):
	word_list = nltk.word_tokenize(sentence)
	wordList = [word for word in word_list if word not in stopwords.words('english')]
	
	mydict = extractParaphrase.dictionary()
	for i in xrange(len(wordList)):
		if(wordList[i] in mydict.keys()):
			wordList[i] = mydict[wordList[i]]	


def sentenceProcessing(sentence):

	wordList = nltk.word_tokenize(sentence)

	negation = ['not','n\'t','nor','null','neither','barely','scarcely','hardly','no','none','nobody','nowhere','nothing','never','without']
	
	negeted_tokens = [None]*(len(wordList))
	print wordList
# as first word will never have a negeted token in front of it.
	negeted_tokens[0] = 0
	
	for i in range(1,len(wordList)):
		if(wordList[i-1] in negation):
			negeted_tokens[i] = 1
		else:
			negeted_tokens[i] = 0


	mydict = extractParaphrase.dictionary()
	for i in xrange(len(wordList)):
		if(wordList[i] in mydict.keys()):
			wordList[i] = mydict[wordList[i]]


	return (wordList, negeted_tokens)

