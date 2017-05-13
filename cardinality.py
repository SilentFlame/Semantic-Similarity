import LexicalSimilarities
import getSentences


#experimentally obtained
# p1 = 1.05
# p2 = 0.85
# p3 = 0.5
# p4 = 0.65

def neg(s,p):
	if(s < 0):
		return (-s)**p
	else:
		return 0


def pos(s,p):
	if (s >= 0):
		return (s)**p
	else:
		return 0


def softCardinality1(sentence):
	p = 1.05
	ans = 0
	bag = getSentences.getPreprocessedBagOfWords(sentence)
	# preprocessedBagOfWords = getPreprocessedBagOfWords(sentence)

	for i in xrange(len(bag)):
		temp_neg = 0
		temp_pos = 0
		for j in xrange(len(bag)):
			temp_neg += neg(LexicalSimilarities.similarity1(bag[i], bag[j]), p)
			temp_pos += pos(LexicalSimilarities.similarity1(bag[i], bag[j]), p)
		print "Temp_Vars: "
		print temp_pos, temp_neg
		ans += (2-(1/(1-temp_neg)))/(temp_pos)
	return ans

def softCardinality2(sentence):
	p = 0.85
	ans = 0
	bag = getSentences.getPreprocessedBagOfWords(sentence)
	for i in xrange(len(bag)):
		temp_neg = 0
		temp_pos = 0
		for j in xrange(len(bag)):
			temp_neg += neg(LexicalSimilarities.similarity2(bag[i], bag[j]), p)
			temp_pos += pos(LexicalSimilarities.similarity2(bag[i], bag[j]), p)
		ans += (2-(1/(1-temp_neg)))/(temp_pos)
	return ans



def softCardinality3(sentence):
	p = 0.50
	ans = 0
	bag = getSentences.getPreprocessedBagOfWords(sentence)
	for i in xrange(len(bag)):
		temp_neg = 0
		temp_pos = 0
		for j in xrange(len(bag)):
			temp_neg += neg(LexicalSimilarities.similarity3(bag[i], bag[j]), p)
			temp_pos += pos(LexicalSimilarities.similarity3(bag[i], bag[j]), p)
		ans += (2-(1/(1-temp_neg)))/(temp_pos)
	return ans



# def cardinality4():
# 	p = 0.65
# 	temp_neg = 0
# 	temp_pos = 0
# 	bagA, bagB = getWordBag()
# 	for i in xrange(len(bagA)):
# 		for j in xrange(len(bagB)):
# 			temp_neg += neg(LexicalSimilarities.similarity4(bagA[i], bagB[j]), p)
# 			temp_pos += pos(LexicalSimilarities.similarity4(bagA[i], bagB[j]), p)
# 		ans += (2-(1/(1-temp_neg)))/(temp_pos)
# 	return ans
	

