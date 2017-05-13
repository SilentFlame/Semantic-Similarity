import cardinality
import getSentences
import extractParaphrase

sentence1 = getSentences.getSentence()
sentence2 =  getSentences.getSentence()
bagOfWords1 = getSentences.getPreprocessedBagOfWords(sentence1)
bagOfWords2 = getSentences.getPreprocessedBagOfWords(sentence2)


# bagOfWords1 = getWordBag(sentence1)
# bagOfWords2 = getWordBag(sentence2)


# preprocessedBagOfWords = getPreprocessedBagOfWords(sentence)

# car1 = softCardinality1(sentence)
car2 = cardinality.softCardinality2(sentence1)
car3 = cardinality.softCardinality3(sentence2)
# car2 = softCardinality2(sentence)
# car3 = softCardinality3(sentence)
# print "Car1 = " + str(car1)
print "Car2-1 = " + str(car2)
# print "Car2 = " + str(car2)
print "Car3-2 = " + str(car3)


# listA , negated = sentenceProcessing(sentence)

# print listA
# print negated


print "Printing factors values: "
print "Inter: " + str(LexicalSimilarities.intersectionFactor(sentence1, sentence2)) 
print "Uni_2: " + str(LexicalSimilarities.unionFactor(sentence1, sentence2, 2))
print "Uni_3: " + str(LexicalSimilarities.unionFactor(sentence1, sentence2, 3))

print "mean_2: " + str(LexicalSimilarities.meanFactor(sentence1, sentence2, 2)) 
print "mean_3: " + str(LexicalSimilarities.meanFactor(sentence1, sentence2, 3))

print "4th mean_ 2" + str(LexicalSimilarities.fourthMeanFactor(sentence1, sentence2, 2)) 
print "4th mean_ 3" + str(LexicalSimilarities.fourthMeanFactor(sentence1, sentence2, 3)) 
