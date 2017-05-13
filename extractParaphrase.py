import json



def dictionary():	
	f = open('ppdb_lexical', 'rb')
	text = f.read()
	lines = list(text.split('\n'))
	lines.pop()
	mydict = {}
	for line in lines:
		objects = line.split('|||')
		paraphrase1 = objects[1]
		paraphrase2 = objects[2]
		
		l = objects[3].split()
		para_score1 = l[5].split("=")[1]
		para_score2 = l[8].split("=")[1]
		if(para_score1 > para_score2) :
			#parahrase1 will be replaced by paraphrase2
			mydict[paraphrase1.strip()] = paraphrase2.strip()
		elif(para_score1 < para_score2) :
			mydict[paraphrase2.strip()] = paraphrase1.strip()
	# print len(mydict)
	#json.dump(mydict, open("phrasal_output.txt",'w'))
	return mydict
	f.close()