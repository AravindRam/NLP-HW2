import os
import codecs
from collections import OrderedDict

vocab_dictionary=OrderedDict()

path=[]
path.append(os.getcwd()+"/email/enron1/ham")
path.append(os.getcwd()+"/email/enron1/spam")
path.append(os.getcwd()+"/email/enron2/ham")
path.append(os.getcwd()+"/email/enron2/spam")
path.append(os.getcwd()+"/email/enron4/ham")
path.append(os.getcwd()+"/email/enron4/spam")
path.append(os.getcwd()+"/email/enron5/ham")
path.append(os.getcwd()+"/email/enron5/spam")

vocab_path = os.getcwd()+"/email/enron.vocab"
 
fout=open("email_consolidated_data.txt","w")
vocab_in=open(vocab_path,"r",encoding='latin')
vocab_out=open("email_vocab_id.txt","w")
email_data=open("email_consolidated_data.txt","r")

for i in range(0,8):
	directory_path=path[i]
	for filename in os.listdir(directory_path):
		fin=open(directory_path+"/"+filename,"r",encoding='latin')		
		if((i+1)%2):
			fout.write("HAM")
		else:
			fout.write("SPAM")	
		for line in fin.readlines():
			line = line.rstrip("\n")
			fout.write(" "+line)
		fout.write("\n")	
		fin.close()
	
fout.close()
id1 = 1
for line in vocab_in.readlines():
	vocab_dictionary[line.rstrip("\n")] = id1
	vocab_out.write(line.rstrip("\n")+" "+str(id1))
	vocab_out.write("\n")
	id1 = id1 + 1

fout2 = open("spam_project_data.txt","w")
for line in email_data.readlines():
	words=line.rstrip("\n").split(" ")
	vocab_count=OrderedDict()
	for word in words[1:]:
		if(word in vocab_dictionary.keys()):		
			vocab_count[vocab_dictionary[word]]=0	
	for word in words[1:]:
		if(word in vocab_dictionary.keys()):
			vocab_count[vocab_dictionary[word]]+=1
	fout2.write(words[0])
	for key in sorted(vocab_count.keys()):	
		fout2.write(" "+str(key)+":"+str(vocab_count[key]))
	fout2.write("\n")


vocab_in.close()
vocab_out.close()
email_data.close()
fout2.close()

vocab_dictionary=OrderedDict()

path = os.getcwd()+"/spam_or_ham_test"
vocab_path = os.getcwd()+"/email/enron.vocab"
 
fout=open("email_test_data.txt","w")
vocab_in=open(vocab_path,"r",encoding='latin')
vocab_out=open("email_vocab_id.txt","w")
email_data=open("email_test_data.txt","r")


for filename in sorted(os.listdir(path)):
	if(filename.endswith(".txt")):
		fin=open(path+"/"+filename,"r",encoding='latin')		
		for line in fin.readlines():
			line = line.rstrip("\n")
			fout.write(line)
		fout.write("\n")	
		fin.close()
	
fout.close()

id1 = 0
for line in vocab_in.readlines():
	vocab_dictionary[line.rstrip("\n")] = id1
	vocab_out.write(line.rstrip("\n")+" "+str(id1))
	vocab_out.write("\n")
	id1 = id1 + 1

fout2 = open("spam_project_test_data.txt","w")
for line in email_data.readlines():
	words=line.rstrip("\n").split(" ")
	vocab_count=OrderedDict()
	for word in words:
		if(word in vocab_dictionary.keys()):		
			vocab_count[vocab_dictionary[word]]=0	
	for word in words:
		if(word in vocab_dictionary.keys()):
			vocab_count[vocab_dictionary[word]]+=1
	for key in sorted(vocab_count.keys()):	
		fout2.write(str(key)+":"+str(vocab_count[key])+" ")
	fout2.write("\n")

vocab_in.close()
vocab_out.close()
email_data.close()
fout2.close()


