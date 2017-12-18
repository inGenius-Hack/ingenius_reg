import csv

from reg.models import Participant, Team


FILE = "../export_team_participants.csv"


data = []

for team in Team.objects.all():
	row = [team.team_id, team.name, team.idea]
	for m in team.participants.all():
		row += [m.name, m.phone, m.college]
	data.append(row)
#	members = [m.name, m.phone, m.email, m.college for m in team.participants.all()]
#	data.append(row, members)


with open(FILE, "wb") as f:
	writer = csv.writer(f)
	writer.writerows(data)
