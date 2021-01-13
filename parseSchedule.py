from os.path import split


dayConversion = {'M':'MO','T':'TU','W':'WE','R':'TH','F':'FR','-':''}
timeConverstion = {'a':0,'p':12}
schedule = open('schedule.txt','r').read()

schedule = schedule.split('\n')

def timeConvert(time):
    seperated = time.split(':')
    hour = int(seperated[0]) + timeConverstion[seperated[1][2]]
    minute = seperated[1][:2]
    return str(hour)+':'+minute

for i in range(len(schedule)):
    if i%3 == 0:
        continue
    details = schedule[i].split('\t')
    if i%3 == 1:
        timeInfo = details[5].split(' ')
        dates = []
        times = []
        if(timeInfo[0] != 'TBA'):
            dates = list(filter(lambda x: x != '',map(lambda x: dayConversion[x],timeInfo[0])))
            times = list(map(timeConvert,timeInfo[1].split('-')))
        print(details[2], '\n', dates, times)
    if i%3 == 2:
        startAndEnd = list(map(lambda x: x[x.index(':')+2:],details[1].split('   ')))
        print(startAndEnd,'\n')

