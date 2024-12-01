# here to calculate the smalest "distance" between the two lists of numbers in the input file
input = open("day1input.txt", "r")
left = []
right = []
for line in input:
    numbers = line.lstrip(" ").split(" ")
    left.append(int(numbers[0]))
    right.append(int(numbers[3]))
left.sort()
right.sort()
distance = 0
for location in range(len(left)):
    localDistance = left[location] - right[location]
    if localDistance < 0:
        localDistance = -localDistance
    distance += localDistance
print(distance)

# part 2
similarity = 0
for location in left:
    acurances = right.count(location)
    similarity += location * acurances
print(similarity)
    