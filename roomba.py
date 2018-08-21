import sys
import collections

# simple counter of file lines
def line_count(filename):
	with open(filename) as f:
		for i, l in enumerate(f):
			pass
	return i + 1


# roomba controller 
def roomba(filename):
	# get line count of the current file (minus 1 to account for 0 index)
	count = line_count(filename)-1
	with open(filename) as f:
	    lines = [line.rstrip('\n') for line in open(filename)]
	    #assigning room_area, coordinates, patches, and direction variables by parsing text file lines 
	    room_area = lines[0].split(" ")
	    coordinates = lines[1].split(" ")

	    #adding patches to a list 
	    p =  lines[2:count]
	    patches = []
	    for i in p:
	    	j = i.split(" ")
	    	patches.append(j)
	    #assigning variables to account for # of patches cleaned 
	    # and when a patch has been cleaned (and can be removed from patch list)
	    patchCleanNumber = 0

	    #parsing directions into a list
	    directions = []
	    for d in lines[count]:
	    	directions.append(d)


	    #For every letter in directions, update coordinates
	    for i in directions:
	    	coordinates = updateCoordinates(coordinates, i, room_area)
	    	#with every update in coordinates, check if it matches a patch location
	    	for p in patches:
	    		#if it does, iterate on the patchCleanNumber and remove patch from list
	    		if p == coordinates:
	    			patchCleanNumber += 1
	    			patches.remove(p)

	    #output formatted as intructions state 
    	print coordinates[0] +" "+ coordinates[1]
    	print patchCleanNumber



#method to update coordinates depending on the direction inserted	
def updateCoordinates(coordinates,i,room_area):
	if i is "E":
		#check that the roomba will not run into a wall using room_area
		if (int(coordinates[0]) +  1) < room_area[0]:
			#move roomba east
			coordinates[0] = str(int(coordinates[0]) + 1)
	if i is "W":
		#check that the roomba will not run into a wall using room_area
		if (int(coordinates[0]) - 1) > 0:
			#move roomba west
			coordinates[0] = str(int(coordinates[0]) - 1)
	if i is "N":
		#check that the roomba will not run into a wall using room_area
		if (int(coordinates[1]) +  1) < room_area[1]:
			#move roomba north
			coordinates[1] = str(int(coordinates[1]) + 1)
	if i is "S":
		#check that the roomba will not run into a wall using room_area
		if (int(coordinates[1]) -  1) > 0:
			#move roomba sount
			coordinates[1] = str(int(coordinates[1]) - 1)
	return coordinates

def main():
    script = sys.argv[0]
    #reads the file name here 
    filename = sys.argv[1]
    roomba(filename)

    

if __name__ == '__main__':
   main()
