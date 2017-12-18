from django.contrib import admin

from .models import Participant, Team

class ParticipantAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personal Information',    {'fields': ['participant_id', 'name',
            'gender', 'phone', 'email', 'college', 'github_url',
            'linkedin_url']}),
        ('Event Information',       {'fields': ['team', 'barcode', 'registered',
            'paid', 'checked_in', 'had_lunch', 'had_dinner', 'had_breakfast',
            'noc_submitted', 'recharge_possible']})
    ]
    list_display = ('participant_id', 'name', 'team', 'phone', 'email', 'gender', 'paid')
    search_fields = ('participant_id', 'name', 'barcode', 'team__name')

admin.site.register(Participant, ParticipantAdmin)

class ParticipantInline(admin.StackedInline):
    model = Participant
    extra = 1
    # fields = ('name', 'gender', 'barcode', 'participant_id', '/checked_in', 'had_lunch', 'had_dinner', 'had_breakfast')

class TeamAdmin(admin.ModelAdmin):
    inlines = [ParticipantInline]
    search_fields = ('name', 'domain')
    list_display = ('name', 'team_id', 'domain', 'get_team_member_names', 'get_team_size')

admin.site.register(Team, TeamAdmin)
