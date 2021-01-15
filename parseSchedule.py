from os.path import split

dayConversion = {'M':'MO','T':'TU','W':'WE','R':'TH','F':'FR','-':''}
timeConverstion = {'a':0,'p':12}

def timeConvert(time):
    seperated = time.split(':')
    hour = int(seperated[0]) + timeConverstion[seperated[1][2]]
    minute = seperated[1][:2]
    return [int(hour),int(minute)]

def parseSchedule():
    scheduleData = []
    classData = []
    schedule = open('schedule.txt','r').read()
    schedule = schedule.split('\n')
    for i in range(1,len(schedule)):
        if i%3 == 0:
            scheduleData.append(classData.copy())
            classData.clear()
            continue
        details = schedule[i].split('\t')
        if i%3 == 1:
            timeInfo = details[5].split(' ')
            dates = []
            times = []
            if(timeInfo[0] != 'TBA'):
                dates = list(filter(lambda x: x != '',map(lambda x: dayConversion[x],timeInfo[0])))
                dates = ",".join(dates)
                times = list(map(timeConvert,timeInfo[1].split('-')))
                classData.append(details[2])
                classData.append(dates)
                classData.append(times)
            else:
                classData.append('noData')
        if i%3 == 2:
            startAndEnd = list(map(lambda x: x[x.index(':')+2:].split('/'),details[1].split('   ')))
            classData.append(list(map(lambda x: int(x),startAndEnd[0])))
            classData.append(list(map(lambda x: int(x),startAndEnd[1])))
    return scheduleData

