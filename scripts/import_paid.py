from reg.models import Participant

import csv


FILE = '../payment_exports.csv'


with open(FILE, 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        try:
            p = Participant.objects.get(participant_id=row[0])
        except Participant.DoesNotExist:
            continue
        if row[7] == 250 or row[7] == '250':
            p.paid = True
        if row[6]:
            p.gender = row[6].strip()
        if len(row[9])>1 and row[9].strip() != 'paytm':
            p.service_provider = row[9].strip()
        p.save()
