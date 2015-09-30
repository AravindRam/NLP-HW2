import sys

# Split the corpus into training and development data

projectData = open(sys.argv[1],"r")
trainData = open("training.txt","w")
devData = open("dev.txt","w")
line_count=1

for line in projectData.readlines():
	if(sys.argv[2] == "75"):	
		if(line_count % 4):
			trainData.write(line)
		else:
			devData.write(line)
	elif(sys.argv[2] == "25"):
		if(line_count % 4 == 0):
			trainData.write(line)
		else:
			devData.write(line)			
	line_count+=1

projectData.close()
trainData.close()
devData.close()


