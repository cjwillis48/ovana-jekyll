import json
import csv
path = '~'

with open('../ovana/src/assets/data/meetings.json') as json_file:
    meetings = json.load(json_file)

data_file = open('_data/meetings.csv', 'w')
csv_writer = csv.writer(data_file)

for meeting in meetings:
    address = meeting.pop('address')
    meeting['street'] = address['street']
    meeting['city'] = address['city']
    meeting['state'] = address['state']
    meeting['zip'] = address['zip']

    meeting['tags'] = ','.join(meeting['tags'])


header = meetings[0].keys()
csv_writer.writerow(header)

for meeting in meetings:
    csv_writer.writerow(meeting.values())