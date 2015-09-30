import sys

filename = sys.argv[2]
token = filename.split("/")
filetype = token[-1].split(".")[0]

actual_file = open(sys.argv[1],"r")
predicted_file = open(sys.argv[2],"r")

count = 0
predicted_label = []
for line in predicted_file.readlines():
	predicted_label.append(line.rstrip("\n"))
	count = count+1

actual_label = []

if(filetype == "spam"):

	for line in actual_file.readlines():
		words = line.split(" ")
		if(words[0] == "+1"):
			actual_label.append("HAM")
		elif(words[0] == "-1"):
			actual_label.append("SPAM")
	correct=0
	incorrect=0
	line_count=0
	actual_ham_count=0
	actual_spam_count=0
	predicted_ham_count=0
	predicted_spam_count=0
	correct_ham_count=0
	correct_spam_count=0

	for i in range(count):
		if(actual_label[i] == predicted_label[i]):
			correct+=1
			if(actual_label[i] == "HAM"):
				correct_ham_count+=1
			else:
				correct_spam_count+=1
		else:
			incorrect+=1

		if(actual_label[i] == "HAM"):
			actual_ham_count+=1
		else:
			actual_spam_count+=1

		if(predicted_label[i] == "HAM"):
			predicted_ham_count+=1
		else:
			predicted_spam_count+=1		

	sys.stdout.write("Line Count : "+str(count)+"\n")

	accuracy = correct/(correct + incorrect)
	precision_ham = correct_ham_count/predicted_ham_count
	precision_spam = correct_spam_count/predicted_spam_count
	recall_ham = correct_ham_count/actual_ham_count
	recall_spam = correct_spam_count/actual_spam_count

	fscore_ham = 2 * precision_ham * recall_ham/(precision_ham + recall_ham)
	fscore_spam = 2 * precision_spam * recall_spam/(precision_spam + recall_spam)

	sys.stdout.write("Accuracy : "+str(accuracy*100)+"%\n")
	sys.stdout.write("Correct: "+str(correct)+"\n")
	sys.stdout.write("Incorrect: "+str(incorrect)+"\n")
	sys.stdout.write("Ham Precision: "+str(precision_ham*100)+"%\n")
	sys.stdout.write("Spam Precision: "+str(precision_spam*100)+"%\n")
	sys.stdout.write("Ham Recall: "+str(recall_ham*100)+"%\n")
	sys.stdout.write("Spam Recall: "+str(recall_spam*100)+"%\n")
	sys.stdout.write("Ham F-Score: "+str(fscore_ham)+"\n")
	sys.stdout.write("Spam F-score: "+str(fscore_spam)+"\n")

elif(filetype == "sentiment"):
	
	for line in actual_file.readlines():
		words = line.split(" ")
		if(words[0] == "+1"):
			actual_label.append("POSITIVE")
		elif(words[0] == "-1"):
			actual_label.append("NEGATIVE")
	correct=0
	incorrect=0
	line_count=0
	actual_positive_count=0
	actual_negative_count=0
	predicted_positive_count=0
	predicted_negative_count=0
	correct_positive_count=0
	correct_negative_count=0

	for i in range(count):
		if(actual_label[i] == predicted_label[i]):
			correct+=1
			if(actual_label[i] == "POSITIVE"):
				correct_positive_count+=1
			else:
				correct_negative_count+=1
		else:
			incorrect+=1

		if(actual_label[i] == "POSITIVE"):
			actual_positive_count+=1
		else:
			actual_negative_count+=1

		if(predicted_label[i] == "POSITIVE"):
			predicted_positive_count+=1
		else:
			predicted_negative_count+=1		

	sys.stdout.write("Line Count : "+str(count)+"\n")

	accuracy = correct/(correct + incorrect)
	precision_positive = correct_positive_count/predicted_positive_count
	precision_negative = correct_negative_count/predicted_negative_count
	recall_positive = correct_positive_count/actual_positive_count
	recall_negative = correct_negative_count/actual_negative_count

	fscore_positive = 2 * precision_positive * recall_positive/(precision_positive + recall_positive)
	fscore_negative = 2 * precision_negative * recall_negative/(precision_negative + recall_negative)

	sys.stdout.write("Accuracy : "+str(accuracy*100)+"%\n")
	sys.stdout.write("Correct: "+str(correct)+"\n")
	sys.stdout.write("Incorrect: "+str(incorrect)+"\n")
	sys.stdout.write("Positive Precision: "+str(precision_positive*100)+"%\n")
	sys.stdout.write("Negative Precision: "+str(precision_negative*100)+"%\n")
	sys.stdout.write("Positive Recall: "+str(recall_positive*100)+"%\n")
	sys.stdout.write("Negative Recall: "+str(recall_negative*100)+"%\n")
	sys.stdout.write("Positive F-Score: "+str(fscore_positive)+"\n")
	sys.stdout.write("Negative F-score: "+str(fscore_negative)+"\n")
	
actual_file.close()
predicted_file.close() 
	
