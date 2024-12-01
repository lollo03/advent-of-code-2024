file = open("input.txt", "r")

arr1 = []
arr2 = []

for line in file:
    splitted = line.split(" ")
    arr1.append(splitted[0])
    arr2.append(splitted[3])


similarity = 0;

def count_occurances(arr, item):
    ret = 0;
    for i in arr:
        if (int(i) == int(item)):
            ret = ret+1
    return ret

for i in range(len(arr1)):
    tmp = count_occurances(arr2, arr1[i])
    similarity += int(arr1[i]) *tmp


print(similarity)

