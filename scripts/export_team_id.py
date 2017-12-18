import csv

from reg.models import Team

FILE = '../team_id_export.csv'

teams = Team.objects.all()

data = [[team.team_id, team.name.encode('ascii','ignore'), team.idea.encode('ascii','ignore')] \
    for team in teams if team.team_id]
with open(FILE,'wb') as f:
    teams = Team.objects.all()
    writer = csv.writer(f)
    writer.writerows(data)
