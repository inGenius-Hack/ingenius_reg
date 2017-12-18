from reg.models import Participant, Team

for p in Participant.objects.all():
    p.name = p.name.encode('ascii', 'ignore')
    p.team.name = p.team.name.encode('ascii', 'ignore')
    p.team.idea = p.team.idea.encode('ascii', 'ignore')
    p.team.save()
    p.save()
