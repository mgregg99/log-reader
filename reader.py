file = open('access.log', 'r')

rollingList = []
errorList = []

for line in file:
    currentTest = ''
    

    for x in line:
        if x != ' ':
            currentTest = currentTest + x
        else:
            if currentTest.isdigit() and int(currentTest) < 600 and int(currentTest) > 399:
                rollingList.append(line)
                errorList.append(currentTest)
            
            currentTest = ''




file.close
