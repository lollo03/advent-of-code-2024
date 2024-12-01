file = open("input.txt", "r")

arr1 = []
arr2 = []

for line in file:
    splitted = line.split(" ")
    arr1.append(splitted[0])
    arr2.append(splitted[3])


distance = 0

arr1.sort()
arr2.sort()


for index in range(len(arr1)):
    distance += abs(int(arr1[index]) - int(arr2[index]))


print(distance)
