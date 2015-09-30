import sys

fin1 = open("sentiment.feat.fixed","r")
fin2 = open("spam_project_test_data.txt","r")
fout1 = open("svm_sentiment_test.txt","w")
fout2 = open("megam_sentiment_test.txt","w")
fout3 = open("nb_sentiment_test.txt","w")
fout4 = open("svm_spam_test.txt","w")
fout5 = open("megam_spam_test.txt","w")
fout6 = open("nb_spam_test.txt","w")

for line in fin1.readlines():
	fout1.write("+1")
	words = line.split(" ")
	for i in range(len(words)):
		kv = words[i].split(":")
		fout1.write(str(" "+str(int(kv[0])+1)+":"+str(kv[1])))

fin1.seek(0,0)

for line in fin1.readlines():
	fout2.write("1")
	words = line.split(" ")
	for i in range(len(words)):
		kv = words[i].split(":")
		fout2.write(str(" "+str(int(kv[0])+1)+" "+str(kv[1])))

fin1.seek(0,0)

for line in fin1.readlines():
	words = line.split(" ")
	for i in range(len(words)):
		kv = words[i].split(":")
		if(i == 0):
			fout3.write(str(str(int(kv[0])+1)+":"+str(kv[1])))
		else:
			fout3.write(str(" "+str(int(kv[0])+1)+":"+str(kv[1])))

for line in fin2.readlines():
	fout4.write("+1")
	words = line.split(" ")
	for i in range(len(words)):
		kv = words[i].split(":")
		if(len(kv) == 2):
			fout4.write(str(" "+str(int(kv[0])+1)+":"+str(kv[1])))
	fout4.write("\n")

fin2.seek(0,0)

for line in fin2.readlines():
	fout5.write("1")
	words = line.rstrip("\n").split(" ")
	for i in range(len(words)):
		kv = words[i].rstrip("\n").split(":")
		if(len(kv) == 2):
			fout5.write(str(" "+str(int(kv[0])+1)+" "+str(kv[1])))
	fout5.write("\n")

fin2.seek(0,0)

for line in fin2.readlines():
	words = line.rstrip("\n").split(" ")
	for i in range(len(words)):
		kv = words[i].split(":")
		if(len(kv) == 2):
			if(i == 0):
				fout6.write(str(str(int(kv[0])+1)+":"+str(kv[1])))
			else:
				fout6.write(str(" "+str(int(kv[0])+1)+":"+str(kv[1])))
	fout6.write("\n")

fin1.close()
fin2.close() 
fout1.close()
fout2.close()
fout3.close()
fout4.close()
fout5.close()
fout6.close()
