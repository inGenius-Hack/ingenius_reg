import csv

from reg.models import Participant, Team


FILE1 = '../updated_participant_id.csv'

failed = []

with open(FILE1, 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        p = Participant.objects.filter(email=row[3])
        if len(p) != 1:
            failed.append([row[3]])
            continue
        p = p[0]
        p.participant_id = row[0]
        p.save()


print "Failed count: {}\n".format(len(failed))
print failed
