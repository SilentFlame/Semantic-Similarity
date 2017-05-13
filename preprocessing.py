import sys,string
import csv
import nltk.data
from nltk.tokenize import sent_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
punct = string.punctuation
stoplist = set(stopwords.words('english'))
stoplist.update(['should','now','\'s','something','would','also','\'t','\'ve'])

negation = ['not','n\'t','nor','null','neither','barely','scarcely',
'hardly','no','none','nobody','nowhere','nothing','never','without']


if __name__ == '__main__':
	fout = open('./TestData/English_GS/STS2016.input.headlines.txt')
	reader=csv.reader(fout,delimiter='\t') #Since sentences in files are tab separated.
	for line in reader:
		sent1 = line[0]
		sent2 = line[1]
		tokenizer = RegexpTokenizer(r'\w+')
		token1=tokenizer.tokenize(sent1)
		token2=tokenizer.tokenize(sent2)