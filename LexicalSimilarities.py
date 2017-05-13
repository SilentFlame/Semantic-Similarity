from nltk.stem.porter import *
from pyjarowinkler import distance
import math
import numpy as np
from compiler.ast import flatten
import gensim
model = gensim.models.KeyedVectors.load_word2vec_format('vectors_400.txt', binary=False)
import getSentences
import cardinality

# word1 = "desire"
# word2 = "lust"

def cosine(v1, v2):
    v1_abs = math.sqrt(np.dot(v1, v1))
    v2_abs = math.sqrt(np.dot(v2, v2))
    cosine_output = np.dot(v1, v2) / (v1_abs * v2_abs)   
    #print type(cosine_output)
    if type(cosine_output) == np.float64:
        return cosine_output
    else:
        return -1.0


def getDotProduct(vec1, vec2):
	result = np.dot(vec1, vec2)
	return result

#First Lexical similarity function
def similarity1(word1, word2):
	
	if( (len(word1) >= 3) and (len(word2)>=3) ):
		stemmer = PorterStemmer()
		stem1 = stemmer.stem(word1)
		stem2 = stemmer.stem(word2)

		substrings1 = [stem1[i:j] for i in range(len(stem1)) for j in range(i+1,len(stem1)+1)]
		X = []
		for subs1 in substrings1:
			if(len(subs1)>=3 and len(subs1)<=4):
				X.append(subs1)

		substrings2 = [stem2[i:j] for i in range(len(stem2)) for j in range(i+1,len(stem2)+1)]
		Y = []
		for subs2 in substrings2:
			if(len(subs2)>=3 and len(subs2)<=4):
				Y.append(subs2)


		# print "Lengths for deno"
		# print len(X)
		# print len(Y)

		x = flatten(X)
		y = flatten(Y)

		nume = len(list(set(x).intersection(set(y))))
		deno = math.sqrt(len(X)*len(Y)) 
		S1 = nume/deno
		return S1

	else:
		return 0

#Second Lexical similarity function(Jaro-Winkler)
# Scaling is 0.1 by default
def similarity2(word1, word2):
	S2 = distance.get_jaro_distance(word1, word2, winkler=True, scaling=0.1)
	return S2


#Word embedding
def similarity3(word1, word2):
	try:
		v1 = model[word1]
	except KeyError:
        	print word1 + "not in vocabulary"
        	v1 = 0
	try:	
		v2 = model[word2]
	except KeyError:
		print word2 + "not in vocabulary"
		v2 = 0 
	S3 = cosine(v1,v2)
	return S3


# computing the 11 factors for rational similarity function based on cardinality function.

# f1 = |A(inter)B| = A.B // Intersection
def intersectionFactor(sentence1, sentence2):
	wordList1 = getSentences.getWordBag(sentence1)
	wordList2 = getSentences.getWordBag(sentence2)
	for i in xrange(len(wordList1)):
		vec1 += model[wordList1[i]]	

	for i in xrange(len(wordList2)):
		vec2 += model[wordList2[i]]	

	return getDotProduct(vec1, vec2)

#f2 = |A (union) B| = |A|n + |B|n - |A(inter)B| // union
def unionFactor(sentence1, sentence2, n):
	if(n == 1):
		ans += cardinality.softCardinality1(sentence1)
		ans += cardinality.softCardinality1(sentence2)
		ans += intersectionFactor(sentence1, sentence2)
		return ans

	elif(n == 2):
		ans += cardinality.softCardinality2(sentence1)
		ans += cardinality.softCardinality2(sentence2)
		ans += intersectionFactor(sentence1, sentence2)
		return ans

	elif(n == 3):
		ans += cardinality.softCardinality3(sentence1)
		ans += cardinality.softCardinality3(sentence2)
		ans += intersectionFactor(sentence1, sentence2)
		return ans		

#f4 = min(|A|n , |B|n) // minimum
def minimumFactor(sentence1, sentence2, n):
	if(n == 1):
		car1 = cardinality.softCardinality1(sentence1)
		car2 = cardinality.softCardinality1(sentence2)
		return min(car1, car2)

	if(n == 2):
		car1 = cardinality.softCardinality2(sentence1)
		car2 = cardinality.softCardinality2(sentence2)

		return min(car1, car2)

	elif(n == 3):
		car1 = cardinality.softCardinality3(sentence1)
		car2 = cardinality.softCardinality3(sentence2)
		return min(car1, car2)


#f5 = maximum
def maximumFactor(sentence1, sentence2, n):
	if(n == 1):
		car1 = cardinality.softCardinality1(sentence1)
		car2 = cardinality.softCardinality2(sentence2)

	if(n == 2):
		car1 = cardinality.softCardinality2(sentence1)
		car2 = cardinality.softCardinality2(sentence2)
		return max(car1, car2)

	elif(n == 3):
		car1 = cardinality.softCardinality3(sentence1)
		car2 = cardinality.softCardinality3(sentence2)

#f6 = mean
def meanFactor(sentence1, sentence2, n):
	if(n == 1):
		car1 = cardinality.softCardinality1(sentence1)
		car2 = cardinality.softCardinality2(sentence2)
		return 0.5*(car1 + car2)

	if(n == 2):
		car1 = cardinality.softCardinality2(sentence1)
		car2 = cardinality.softCardinality2(sentence2)
		return 0.5*(car1 + car2)

	elif(n == 3):
		car1 = cardinality.softCardinality3(sentence1)
		car2 = cardinality.softCardinality3(sentence2)
		return 0.5*(car1 + car2)

#f7 = geometric mean
def geometricMeanFactor(sentence1, sentence2, n):
	if(n == 1):
		car1 = cardinality.softCardinality1(sentence1)
		car2 = cardinality.softCardinality2(sentence2)
		return math.sqrt(car1*car2)

	if(n == 2):
		car1 = cardinality.softCardinality2(sentence1)
		car2 = cardinality.softCardinality2(sentence2)
		return math.sqrt(car1*car2)
		
	elif(n == 3):
		car1 = cardinality.softCardinality3(sentence1)
		car2 = cardinality.softCardinality3(sentence2)
		return math.sqrt(car1*car2)

#f8 = quadriticmean
def quadriticMeanFactor(sentence1, sentence2, n):
	if(n == 1):
		car1 = cardinality.softCardinality1(sentence1)
		car2 = cardinality.softCardinality2(sentence2)
		return math.sqrt(0.5*(car1**2 + car2**2))

	if(n == 2):
		car1 = cardinality.softCardinality2(sentence1)
		car2 = cardinality.softCardinality2(sentence2)
		return math.sqrt(0.5*(car1**2 + car2**2))
		
	elif(n == 3):
		car1 = cardinality.softCardinality3(sentence1)
		car2 = cardinality.softCardinality3(sentence2)
		return math.sqrt(0.5*(car1**2 + car2**2))
		
#f9 = cubic mean
def cubicMeanFactor(sentence1, sentence2, n):
	if(n == 1):
		car1 = cardinality.softCardinality1(sentence1)
		car2 = cardinality.softCardinality2(sentence2)
		return (0.5*(car1**3 + car2**3))**(1/3.0)		

	if(n == 2):
		car1 = cardinality.softCardinality2(sentence1)
		car2 = cardinality.softCardinality2(sentence2)
		return (0.5*(car1**3 + car2**3))**(1/3.0)		
	
	elif(n == 3):
		car1 = cardinality.softCardinality3(sentence1)
		car2 = cardinality.softCardinality3(sentence2)
		return (0.5*(car1**3 + car2**3))**(1/3.0)
		
		
#f10 = fourth mean
def fourthMeanFactor(sentence1, sentence2, n):
	if(n == 1):
		car1 = cardinality.softCardinality1(sentence1)
		car2 = cardinality.softCardinality2(sentence2)
		return (0.5*(car1**4 + car2**4))**(1/4.0)		

	if(n == 2):
		car1 = cardinality.softCardinality2(sentence1)
		car2 = cardinality.softCardinality2(sentence2)
		return (0.5*(car1**4 + car2**4))**(1/4.0)		
	
	elif(n == 3):
		car1 = cardinality.softCardinality3(sentence1)
		car2 = cardinality.softCardinality3(sentence2)
		return (0.5*(car1**4 + car2**4))**(1/4.0)		
		
