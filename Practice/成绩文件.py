f = open('G:\文档\output2.txt')
lines = f.readlines()
print(lines)
f.close()

results = []

for line in lines:
    print(line)
    data = line.split()
    print(data)

    sum = 0
    for score in data[1:]:
        sum += int(score)
    result = '%s \t: %d\n' % (data[0], sum)
    print(result)

    results.append(result)

print(results)
output = open('G:\文档\output1.txt', 'w')
output.writelines(results)
output.close()
