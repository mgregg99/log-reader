file = open('/home/byu.local/mgregg99/Source/log-reader/access.log', 'r')

errorList4 = []
errorList5 = []

for line in file:
    currentTest = ''
    count = 7
    

    for x in line:
        if x != ' ':
            currentTest = currentTest + x
            
            
        else:
            count = count - 1
            if currentTest.isdigit() and int(currentTest) < 600 and int(currentTest) > 399 and count > -3:
                innerlist = [currentTest, line]
                if int(currentTest) > 399 and int(currentTest) < 500:
                    errorList4.append(line)
                if int(currentTest) > 499 and int(currentTest) < 600:
                    errorList5.append(line)
            
            currentTest = ''
file.close

for line in errorList4:
    print(line)
for line in errorList5:
     print(line)

print("Size 4xx: " + str(len(errorList4)))
print("Size 5xx: " + str(len(errorList5)))