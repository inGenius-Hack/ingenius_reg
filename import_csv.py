import csv

from reg.models import Participant, Team
from django.utils.crypto import get_random_string

def get_pid():
    allowed_chars       = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
    pid_list            = list()

    while True:
        pid = get_random_string(4,allowed_chars)
        if pid not in pid_list:
            pid_list.append(pid)
            break
    return pid

def main():
    """
    Create teams and participants in the database, and link participants with
    their respective teams.
    """

    csv_file            = "shortlist.csv"
    team_count          = 0
    participant_count   = 0


    #Delete all existing teams and participants from the database.
    Team.objects.all().delete()
    Participant.objects.all().delete()

    with open(csv_file) as f:
        reader = csv.reader(f)
        data = [row for row in reader]

    for item in data:
        if item[0]:
            team_count += 1

            t = Team.objects.create(
                name=item[0].strip(),
            )

            no_of_p = int(item[1])
            print(item[1])
            participant_count += no_of_p

            p1 = Participant.objects.create(
                participant_id=get_pid(),
                name=item[2].strip() + " " + item[3].strip(),
                gender=item[4].strip(),
                college=item[7].strip(),
                email=item[5].strip(),
                phone=str(item[6]),
                team=t
            )

            p2 = Participant.objects.create(
                participant_id=get_pid(),
                name=item[8].strip() + " " +item[9].strip(),
                gender=item[10].strip(),
                college=item[13].strip(),
                email=item[11].strip(),
                phone=str(item[12]),
                team=t
            )

            if no_of_p == 3:
                p3 = Participant.objects.create(
                    participant_id=get_pid(),
                    name=item[14].strip() + " " +item[15].strip(),
                    gender=item[16].strip(),
                    college=item[19].strip(),
                    email=item[17].strip(),
                    phone=str(item[18]),
                    team=t
                )

    print("{} teams and {} participants imported.".format(team_count,
        participant_count))

main()
