from datetime import date, datetime, timedelta
from cal_setup import get_calendar_service
from parseSchedule import parseSchedule

service = get_calendar_service()

d = datetime.now().date()
tomorrow = datetime(d.year, d.month, d.day, 10)+timedelta(days=1)
start = tomorrow.isoformat()
end = (tomorrow + timedelta(hours=1)).isoformat()
cal = open('calendarID.txt','r')
calID = cal.read()
cal.close()

schedule = parseSchedule()
for classData in schedule:
    if(classData[0] != 'noData'):
        className = classData[0]
        startTime = datetime(classData[3][2],classData[3][0],classData[3][1],classData[2][0][0],classData[2][0][1]).isoformat()
        endTime = datetime(classData[3][2],classData[3][0],classData[3][1],classData[2][1][0],classData[2][1][1]).isoformat()
        recurrenceRule =  'RRULE:FREQ=WEEKLY;UNTIL=' + str(classData[4][2]) + '{0:0=2d}'.format(classData[4][0]) + str(classData[4][1]) +'T000000Z;BYDAY=' + classData[1]
        event = {
                "summary": className,
                "start": {"dateTime": startTime, "timeZone": 'CST'},
                "end": {"dateTime": endTime, "timeZone": 'CST'},
                'recurrence': [recurrenceRule],
                'reminders': {
                    'useDefault': False,
                    'overrides': [
                        {'method': 'popup', 'minutes': 5},
                    ],
                },
            }
        event_result = service.events().insert(calendarId=calID,body=event).execute()
