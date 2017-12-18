import csv

from reg.models import Participant 

FILE = '../noc_not_submitted.csv'

participants = Participant.objects.all()

data = [(p.participant_id,p.name.encode('ascii','ignore'),p.barcode) for p in participants if p.noc_submitted != True and p.gender == 'F']

with open(FILE,'wb') as f:
    writer = csv.writer(f)
    writer.writerows(data)
