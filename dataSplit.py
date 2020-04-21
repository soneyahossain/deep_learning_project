import random
infile = open("DATA/label.csv")

lines = []
for line in infile:
    split = line.split(',')
    lines.append(split)

places = dict()
for line in lines:
    placeName = line[2].rstrip()
    if placeName in places:
        places[placeName].append(line)
    elif placeName =="name":
        pass
    else:
        places[placeName] = [line]

trainSet = []
valSet = []

for place in places:
    placeCount = len(places[place])
    valNum = int(.2*placeCount)
    a = random.sample(places[place], valNum)
    b = []
    for item in places[place]:
        if item not in a:
            b.append(item)
    for item in a:
        valSet.append(item)
    for item in b:
        trainSet.append(item)
infile.close()

s = ","

valSetFile = open("valSet.csv", 'w')
valSetFile.write("image_name,label_id,name\n")
for line in valSet:
    valSetFile.write(s.join(line))
valSetFile.close()

trainSetFile = open("trainSet.csv", 'w')
trainSetFile.write("image_name,label_id,name\n")
for line in trainSet:
    trainSetFile.write(s.join(line))
trainSetFile.close()
