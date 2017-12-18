import csv

from reg.models import Team, Participant

FILE = '../team_pno_export.csv'

teams = Team.objects.all()

data = list()

for team in teams:
	p_set = team.participants.all()
	data.append([team.team_id,team.name]+[p.phone for p in p_set])


with open(FILE,'wb') as f:
	writer = csv.writer(f)
	writer.writerows(data)	
