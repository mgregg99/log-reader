file = open('access.log', 'r')

errorList = []

for line in file:
    currentTest = ''
    

    for x in line:
        if x != ' ':
            currentTest = currentTest + x
        else:
            if currentTest.isdigit() and int(currentTest) < 600 and int(currentTest) > 399:
                innerlist = [currentTest, line]
                errorList.append(innerlist)
            
            currentTest = ''

errorList.sort()
relist = []
i = 0
for x in errorList:
    temp = errorList[x][1]
    relist.append(temp)

for line in relist:
    print(line)
file.close
