import sys
import collections

compare = lambda x, y: collections.Counter(x) == collections.Counter(y)

directions = ""

def line_count(filename):
	with open(filename) as f:
		for i, l in enumerate(f):
			pass
	return i + 1


def roomba(filename):
	count = line_count(filename)-1
	with open(filename) as f:
	    lines = [line.rstrip('\n') for line in open(filename)]
	    room_area = lines[0].split(" ")
	    coordinates = lines[1].split(" ")
	    p =  lines[2:count]
	    patches = []
	    for i in p:
	    	j = i.split(" ")
	    	patches.append(j)
	    patchCleanNumber = 0
	    patchClean = False 
	    directions = []
	    for d in lines[count]:
	    	directions.append(d)

	    for i in directions:
	    	coordinates = updateCoordinates(coordinates, i, room_area)
	    	for p in patches:
	    		if p == coordinates:
	    			patchClean = True
	    			patchCleanNumber += 1
	    			patches.remove(p)

    	print coordinates[0] +" "+ coordinates[1]
    	print patchCleanNumber



		


def updateCoordinates(coordinates,i,room_area):
	if i is "E":
		if (int(coordinates[0]) +  1) < room_area[0]:
			coordinates[0] = str(int(coordinates[0]) + 1)
	if i is "W":
		if (int(coordinates[0]) - 1) > 0:
			coordinates[0] = str(int(coordinates[0]) - 1)
	if i is "N":
		if (int(coordinates[1]) +  1) < room_area[1]:
			coordinates[1] = str(int(coordinates[1]) + 1)
	if i is "S":
		if (int(coordinates[1]) -  1) > 0:
			coordinates[1] = str(int(coordinates[1]) - 1)
	return coordinates

def main():
    script = sys.argv[0]
    filename = sys.argv[1]
    roomba(filename)

    

if __name__ == '__main__':
   main()
