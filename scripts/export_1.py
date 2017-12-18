from reg.models import Participant, Team

import csv

data = [[p.participant_id, p.name.encode('ascii', 'ignore'), p.team.name.encode('ascii', 'ignore'), p.email] for p in Participant.objects.all()]


for i in range(len(data)):
    data[i].append("Genius{}".format(str(i+1).zfill(3)))

with open('export_1.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(data)
