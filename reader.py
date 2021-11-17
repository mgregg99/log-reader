monthdic = {
    "Jan" : 1,
    "Feb" : 2,
    "Mar" : 3,
    "Apr" : 4,
    "May" : 5,
    "Jun" : 6,
    "Jul" : 7,
    "Aug" : 8,
    "Sep" : 9,
    "Oct" : 10,
    "Nov" : 11,
    "Dec" : 12,
}

def turnToDate(relist):
    datelist =[]

    for line in relist:
        it = line.find("[") + 1
        newlist = []

        cont = True
        day = ""
        while cont:
            if line[it] != "/":
                day += line[it]
                it += 1
            else:
                cont = False
                it += 1
                newlist.append(int(day))

        
        cont = True
        month = ""
        while cont:
            if line[it] != "/":
                month += line[it]
                it += 1
            else:
                month = monthdic[month]
                cont = False
                it += 1
                newlist.insert(0, int(month))

        cont = True
        year = ""
        while cont:
            if line[it] != ":":
                year += line[it]
                it += 1
            else:
                cont = False
                it += 1
                newlist.insert(0, int(year))
        
        newlist.append(line)
        datelist.append(newlist)
    return datelist

file = open('/home/byu.local/mgregg99/Source/log-reader/access.log', 'r')

errorList4 = []
errorList5 = []

for line in file:
    currentTest = ''
    

    for x in line:
        if x != ' ':
            currentTest = currentTest + x
        else:
            if currentTest.isdigit() and int(currentTest) < 600 and int(currentTest) > 399:
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







# errorList.sort()
# relist = []
# i = 0
# while i < len(errorList):

#     relist.append(errorList[i][1])
#     i += 1

# datelist = turnToDate(relist)


# def turntofinal(datelist):
#     datelist.sort(reverse = True)
#     workingyear = datelist[0][0]
#     workinglist = []
#     i = 0

#     while i < len(datelist):
#         if datelist[i][0] == workingyear:
#             workinglist.append(datelist[i])
#             i += 1
#         else:
#             workinglist.sort(key=lambda x:x[1], reverse = True)
#             j = 0
#             workingmonthlist = []
#             workingmonth = workinglist[j][1]

#     for line in workinglist:
#         print(line)
