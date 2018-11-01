from django.db import models


class Team(models.Model):
    DOMAIN_CHOICES = (
        ('hardware', 'Hardware'),
        ('iot', 'Internet of Things'),
        ('ml', 'Machine Learning'),
        ('mobile', 'Mobile'),
        ('web', 'Web'),
        ('zwibe', 'Zwibe')
    )
    name = models.CharField(max_length=50)
    idea = models.TextField(blank=True)
    domain = models.CharField(max_length=10, choices=DOMAIN_CHOICES, blank=True)
    team_id = models.PositiveIntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    def get_team_size(self):
        return self.participants.count()

    get_team_size.short_description = 'Team Size'

    def get_team_member_names(self):
        members = self.participants.all()
        names = ", ".join([member.name for member in members])
        return names

    get_team_member_names.short_description = 'Team Members'


class Participant(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    participant_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1)
    team = models.ForeignKey(Team, related_name='participants')
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    college = models.CharField(max_length=100)
    github_url = models.URLField(null=True, blank=True)
    linkedin_url = models.URLField(null=True, blank=True)
    barcode = models.CharField(max_length=50, blank=True)
    recharge_possible = models.BooleanField(default=True,blank=True)
    service_provider = models.CharField(max_length=50, blank=True)
    registered = models.BooleanField(default=False)
    checked_in = models.BooleanField(default=False)
    paid = models.BooleanField(default=False)
    noc_submitted = models.BooleanField(default=True)
    had_lunch = models.BooleanField(default=False)
    had_dinner = models.BooleanField(default=False)
    had_breakfast = models.BooleanField(default=False)
    had_snacks_evening = models.BooleanField(default=False)
    had_snacks_midnight = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def is_team_checked_in(self):
        team_members = self.team.participants.all()
        for member in team_members:
            if member.registered:
                return True
        return False
