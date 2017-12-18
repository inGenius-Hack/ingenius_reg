import csv

from reg.models import Participant, Team


data = [[p.participant_id, p.name, p.email, p.phone, p.team.name, p.college, p.paid] for p in Participant.objects.all()]


with open('export_2.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(data)
