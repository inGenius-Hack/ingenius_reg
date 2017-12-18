import csv
from reg.models import Team


FILE = '../team_list_with_abstract.csv'

data = [[t.pk, t.name, t.idea] for t in Team.objects.all()]

with open(FILE, 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(data)
