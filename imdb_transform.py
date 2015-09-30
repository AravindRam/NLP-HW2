import sys
from collections import OrderedDict

features = OrderedDict()
	
#Convert labels to POSITIVE, NEGATIVE and increment features by 1 

givenData = open(sys.argv[1],"r")
projectData = open(sys.argv[2],"w")

for line in givenData.readlines():
	line = line.split(" ")
	label=int(line[0])
	if(label>=7 and label<=10):
		features["class"]="POSITIVE"
	elif(label>=1 and label<=4):
		features["class"]="NEGATIVE"
	projectData.write(features["class"])
	for i in range(1,len(line)):
		kv = line[i].split(":")
		features[kv[0]] = kv[1]
		projectData.write(str(" "+str(int(kv[0])+1)+":"+str(kv[1])))

givenData.close()
projectData.close()

