import sys

fin = open(sys.argv[1],"r")

if(sys.argv[2] == "sentiment"):
	for line in fin.readlines():
		tokens = line.rstrip("\n").split(" ")
		classname = tokens[0].split(":")[1]
		if(classname == "-1"):
			sys.stdout.write("NEGATIVE\n")
		elif(classname == "+1"):
			sys.stdout.write("POSITIVE\n")
elif(sys.argv[2] == "spam"):
	for line in fin.readlines():
		tokens = line.rstrip("\n").split(" ")
		classname = tokens[0].split(":")[1]
		if(classname == "-1"):
			sys.stdout.write("SPAM\n")
		elif(classname == "+1"):
			sys.stdout.write("HAM\n")
	
fin.close()
