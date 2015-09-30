import sys
from collections import OrderedDict
import math

filename = sys.argv[1]
token = filename.split("/")
filetype = token[-1].split(".")[0]

if(filetype == "sentiment"):
	
	occurrence=OrderedDict()
	occurrence["POSITIVE"]=OrderedDict()
	occurrence["NEGATIVE"]=OrderedDict()

	# Reading from modelfile

	lineCount = 0
	modelfile = open(sys.argv[1],"r")
	for line in modelfile.readlines():
		words = line.rstrip("\n").split(" ")
		if(lineCount == 0 or lineCount == 1):
			for word in words[1:]:
				kv = word.split(":")
				occurrence[words[0]][kv[0]]=kv[1]
		elif(lineCount == 2):
			positive_class = int(str(line))
		elif(lineCount == 3):
			negative_class = int(str(line))
		elif(lineCount == 4):
			positive_sum = int(str(line))
		elif(lineCount == 5):
			negative_sum = int(str(line))
		lineCount+=1
	
	modelfile.close()

	probabilityPositive=math.log10(positive_class/(positive_class+negative_class))
	probabilityNegative=math.log10(negative_class/(positive_class+negative_class))
	vocab_size = 89527

	# Classify as POSITIVE or NEGATIVE

	devData = open(sys.argv[2],"r")
	line_count=0

	for line in devData.readlines():
		words = line.split(" ")
		positiveProduct=0
		negativeProduct=0
		for word in words[1:]:
			kv=word.split(":")
			if(kv[0] in occurrence["POSITIVE"].keys()):
				positiveProduct = positiveProduct + math.log10((int(occurrence["POSITIVE"][kv[0]])/positive_sum))	
			else:
				positiveProduct = positiveProduct + math.log10((1/(positive_sum+vocab_size)))	
			if(kv[0] in occurrence["NEGATIVE"].keys()):
				negativeProduct = negativeProduct + math.log10((int(occurrence["NEGATIVE"][kv[0]])/negative_sum))	
			else:
				negativeProduct = negativeProduct + math.log10((1/(negative_sum+vocab_size)))

		numerator1 = probabilityPositive+positiveProduct
		
		numerator2 = probabilityNegative+negativeProduct
	
		if(numerator1 > numerator2):
			sys.stdout.write("POSITIVE\n")
		else:
			sys.stdout.write("NEGATIVE\n")
		line_count+=1

	devData.close()
	
elif(filetype == "spam"):

	occurrence=OrderedDict()
	occurrence["HAM"]=OrderedDict()
	occurrence["SPAM"]=OrderedDict()

	# Reading from modelfile

	lineCount = 0
	modelfile = open(sys.argv[1],"r")
	for line in modelfile.readlines():
		words = line.rstrip("\n").split(" ")
		if(lineCount == 0 or lineCount == 1):
			for word in words[1:]:
				kv = word.split(":")
				occurrence[words[0]][kv[0]]=kv[1]
		elif(lineCount == 2):
			ham_class = int(str(line))
		elif(lineCount == 3):
			spam_class = int(str(line))
		elif(lineCount == 4):
			ham_sum = int(str(line))
		elif(lineCount == 5):
			spam_sum = int(str(line))
		lineCount+=1
	
	modelfile.close()
	

	probabilityHam=math.log10(ham_class/(ham_class+spam_class))
	probabilitySpam=math.log10(spam_class/(ham_class+spam_class))
	vocab_size = 89527


	# Classify as POSITIVE or NEGATIVE

	devData = open(sys.argv[2],"r")
	line_count=0

	for line in devData.readlines():
		words = line.split(" ")
		hamProduct=0
		spamProduct=0
		for word in words[1:]:
			kv=word.split(":")
			if(kv[0] in occurrence["HAM"].keys()):
				hamProduct = hamProduct + math.log10((int(occurrence["HAM"][kv[0]])/ham_sum))	
			else:
				hamProduct = hamProduct + math.log10((1/(ham_sum+vocab_size)))	
			if(kv[0] in occurrence["SPAM"].keys()):
				spamProduct = spamProduct + math.log10((int(occurrence["SPAM"][kv[0]])/spam_sum))	
			else:
				spamProduct = spamProduct + math.log10((1/(spam_sum+vocab_size)))

		numerator1 = probabilityHam+hamProduct
		
		numerator2 = probabilitySpam+spamProduct
		
		if(numerator1 > numerator2):
			sys.stdout.write("HAM\n")
		else:
			sys.stdout.write("SPAM\n")
		line_count+=1

	devData.close()
