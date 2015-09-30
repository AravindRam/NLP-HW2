import sys

fin = open(sys.argv[1],"r")

if(sys.argv[2] == "sentiment"):
	for line in fin.readlines():
		tokens = line.rstrip("\n").split("\t")
		if(tokens[0] == "1"):
			sys.stdout.write("POSITIVE\n")
		elif(tokens[0] == "0"):
			sys.stdout.write("NEGATIVE\n")
elif(sys.argv[2] == "spam"):
	for line in fin.readlines():
		tokens = line.rstrip("\n").split("\t")
		if(tokens[0] == "1"):
			sys.stdout.write("HAM\n")
		elif(tokens[0] == "0"):
			sys.stdout.write("SPAM\n")

fin.close()

