import requests
import json
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from icalendar import Calendar, Event

c = Calendar()

weekdays = {'Mo': 0, 'Di': 1, 'Mi': 2, 'Do': 3, 'Fr': 4}

date = input('Start Year, Month, Day[Y-M-D]:')
name = input('Name of the class:')


def get_interval(date):
    st = date
    en = date
    url = 'https://api.gymkirchenfeld.ch/api/common/holiday?startDate={}&endDate={}'
    st = datetime.strptime(st, '%Y-%m-%d')
    st = datetime.replace(st, month=8, day=1)
    en = datetime.strptime(en, '%Y-%m-%d')
    en = datetime.replace(en, month=8, day=1)
    en += relativedelta(years=1)
    req = requests.get(url.format(st.strftime('%Y-%m-%d'), en.strftime('%Y-%m-%d')))
    json_data = json.loads(req.text)
    dates = []
    non_vacations = []
    for i in range(len(json_data['result'])):
        dates.append([json_data['result'][i]['startDate'], json_data['result'][i]['endDate']])

    for i in range(len(dates) - 1):
        int1 = [dates[i][1], dates[i + 1][0]]
        non_vacations.append(int1)

    intervals = [[datetime.strptime(non_vacations[0][0], '%Y-%m-%d'), datetime.strptime(non_vacations[2][1], '%Y-%m-%d')], [datetime.strptime(non_vacations[3][0], '%Y-%m-%d'), datetime.strptime(non_vacations[4][1], '%Y-%m-%d')]]
    if intervals[0][0] < datetime.strptime(date, '%Y-%m-%d') < intervals[0][1]:
        return intervals[0]
    else:
        return intervals[1]


en = get_interval(date)[1]

url = 'https://api.gymkirchenfeld.ch/api/course/timetable?code={}&next=false'

req = requests.get(url.format(name))
json_data = json.loads(req.text)

for i in range(len(json_data['result']['lessons'])):
    e = Event()
    st_date = date + 'T' + json_data['result']['lessons'][i]['startTime']
    en_date = date + 'T' + json_data['result']['lessons'][i]['endTime']
    e.add('summary', json_data['result']['lessons'][i]['subject']['code'] + ', Zimmer: ' + json_data['result']['lessons'][i]['rooms'][0]['code'].strip('/'))
    e.add('dtstart', datetime.strptime(st_date, '%Y-%m-%dT%H:%M') + timedelta(days=weekdays[json_data['result']['lessons'][i]['day']['code']]))
    e.add('dtend', datetime.strptime(en_date, '%Y-%m-%dT%H:%M'))
    e.add('rrule', {'freq': 'weekly', 'until': en})
    c.add_component(e)

f = open('my.ics', 'wb')
f.write(c.to_ical())
f.close()