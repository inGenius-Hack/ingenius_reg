import csv

from reg.models import Participant 

FILE = '../recharge_possible.csv'

participants = Participant.objects.all()

data = [(p.participant_id,p.name.encode('ascii','ignore'),p.barcode,p.phone,p.service_provider) for p in participants if p.recharge_possible == True and len(p.service_provider)>2]

with open(FILE,'wb') as f:
    writer = csv.writer(f)
    writer.writerows(data)
