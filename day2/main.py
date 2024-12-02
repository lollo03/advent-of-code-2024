file = open("input.txt", "r")

safe = 0

for line in file:
    levels = list(map(int, line.split()))
    trend = 0
    if(levels[0] < levels[1]):
        trend = 1
    elif(levels[0] > levels[1]):
        trend = -1
    else:
        trend = 0
    for i in range(1, len(levels)):
        if(levels[i-1] < levels[i] and trend != 1):
            break
        elif(levels[i-1] > levels[i] and trend != -1):
            break

        if not( 1 <= abs(int(levels[i]) - int(levels[i-1])) <= 3):
            break
    else:
        safe += 1


print(safe)

