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

for i in errorList:
    print(i)

print(len(errorList))
file.close