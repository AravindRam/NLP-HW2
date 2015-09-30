import sys
from collections import OrderedDict

filename = sys.argv[2]
token = filename.split("/")
filetype = token[-1].split(".")[0]

if(filetype == "sentiment"):
	
	occurrence=OrderedDict()
	occurrence["POSITIVE"]=OrderedDict()
	occurrence["NEGATIVE"]=OrderedDict()
	positive_sum=0
	negative_sum=0
	positive_class=0
	negative_class=0

	# Compute the number of occurences of a key per class and build modelfile
	trainingData = open(sys.argv[1],"r")
	modelfile = open(sys.argv[2],"w")

	for line in trainingData.readlines():
		word = line.split(" ")
		if(word[0] == "POSITIVE"):
			positive_class+=1
		elif(word[0] == "NEGATIVE"):
			negative_class+=1
		for i in range(1,len(word)):	
			kv = word[i].split(":")
			if(kv[0] in occurrence[word[0]].keys()):		
				occurrence[word[0]][kv[0]]+=int(kv[1])
			else:
				occurrence[word[0]][kv[0]]=int(kv[1])	

	modelfile.write("POSITIVE")
	for key in occurrence["POSITIVE"].keys():
		modelfile.write(" "+str(key)+":"+str(occurrence["POSITIVE"][key]))
		positive_sum+=int(occurrence["POSITIVE"][key])

	modelfile.write("\nNEGATIVE")
	for key in occurrence["NEGATIVE"].keys():
		modelfile.write(" "+str(key)+":"+str(occurrence["NEGATIVE"][key]))
		negative_sum+=int(occurrence["NEGATIVE"][key])

	modelfile.write("\n"+str(positive_class))
	modelfile.write("\n"+str(negative_class))
	modelfile.write("\n"+str(positive_sum))
	modelfile.write("\n"+str(negative_sum))

	trainingData.close()
	modelfile.close()

elif(filetype == "spam"):

	occurrence=OrderedDict()
	occurrence["HAM"]=OrderedDict()
	occurrence["SPAM"]=OrderedDict()
	ham_sum=0
	spam_sum=0
	ham_class=0
	spam_class=0

	# Compute the number of occurences of a key per class and build modelfile

	trainingData = open(sys.argv[1],"r")
	modelfile = open(sys.argv[2],"w")

	for line in trainingData.readlines():
		word = line.split(" ")
		if(word[0] == "HAM"):
			ham_class+=1
		elif(word[0] == "SPAM"):
			spam_class+=1
		for i in range(1,len(word)):	
			kv = word[i].split(":")
			if(kv[0] in occurrence[word[0]].keys()):		
				occurrence[word[0]][kv[0]]+=int(kv[1])
			else:
				occurrence[word[0]][kv[0]]=int(kv[1])	

	modelfile.write("HAM")
	for key in occurrence["HAM"].keys():
		modelfile.write(" "+str(key)+":"+str(occurrence["HAM"][key]))
		ham_sum+=int(occurrence["HAM"][key])

	modelfile.write("\nSPAM")
	for key in occurrence["SPAM"].keys():
		modelfile.write(" "+str(key)+":"+str(occurrence["SPAM"][key]))
		spam_sum+=int(occurrence["SPAM"][key])

	modelfile.write("\n"+str(ham_class))
	modelfile.write("\n"+str(spam_class))
	modelfile.write("\n"+str(ham_sum))
	modelfile.write("\n"+str(spam_sum))

	trainingData.close()
	modelfile.close()

