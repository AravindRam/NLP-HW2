import sys

fin = open(sys.argv[1],"r")
fout = open(sys.argv[2],"w")

for inputline in fin.readlines():
	line = inputline.split(" ")
	if(line[0] == "POSITIVE" or line[0] == "HAM"):
		line[0] = "+1"
	elif(line[0] == "NEGATIVE" or line[0] == "SPAM"):
		line[0] = "-1"
	fout.write(str(line[0]))
	for i in range(1,len(line)):
		kv = line[i].split(":")		
		fout.write(str(" "+str(int(kv[0]))+":"+str(kv[1])))


fin.close()
fout.close()

