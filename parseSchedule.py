schedule = open('schedule.txt','r').read()

schedule = schedule.split('\n')

for i in range(len(schedule)):
    if i%3 == 0:
        continue
    details = schedule[i].split('\t')
    if i%3 == 1:
        print(details[2],details[5])
    if i%3 == 2:
        print(details[1])

