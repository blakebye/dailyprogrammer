data = []
datafile = open('data.txt')
for line in datafile:
    data.append(line.split())
datafile.close()
for point in data:
    for x in (0, 2):
        point[x] = int(point[x])
towers = []
days = ["Sun","Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
for point in data:
    towers.append(point[0])
towers = sorted(set(towers))
output = [["KILOS"]]

for i in range(len(towers)):
    output.append([towers[i]])
for i in range(len(days)):
    output[0].append(days[i])
    for j in range(1, len(towers) + 1):
        output[j].append(0)

for point in data:
    for tower in towers:
        for day in days:
            if point[0] == tower and point[1] == day:
                output[towers.index(tower) + 1][days.index(day) + 1] += point[2]

char_maxes = map(len, map(str, output[0]))
for i in output:
    row = map(len, map(str, i))
    for j in range(len(row)):
        if row[j] > char_maxes[j]:
            char_maxes[j] = row[j]

for row in output:
    for element in row:
        print "{0:^{1}}".format(element, char_maxes[row.index(element)] + 2) ,
    print

