from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    name = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    user = models.CharField(max_length=100)
    points = models.IntegerField()
    team = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            {'email': 'ironman@marvel.com', 'username': 'IronMan', 'team': 'Marvel'},
            {'email': 'captain@marvel.com', 'username': 'CaptainAmerica', 'team': 'Marvel'},
            {'email': 'batman@dc.com', 'username': 'Batman', 'team': 'DC'},
            {'email': 'superman@dc.com', 'username': 'Superman', 'team': 'DC'},
        ]
        for u in users:
            User.objects.create_user(email=u['email'], username=u['username'], password='password')

        # Create activities
        Activity.objects.create(name='Running', user='IronMan', team='Marvel')
        Activity.objects.create(name='Swimming', user='CaptainAmerica', team='Marvel')
        Activity.objects.create(name='Cycling', user='Batman', team='DC')
        Activity.objects.create(name='Flying', user='Superman', team='DC')

        # Create leaderboard
        Leaderboard.objects.create(user='IronMan', points=100, team='Marvel')
        Leaderboard.objects.create(user='CaptainAmerica', points=90, team='Marvel')
        Leaderboard.objects.create(user='Batman', points=95, team='DC')
        Leaderboard.objects.create(user='Superman', points=110, team='DC')

        # Create workouts
        Workout.objects.create(name='Pushups', user='IronMan', team='Marvel')
        Workout.objects.create(name='Situps', user='CaptainAmerica', team='Marvel')
        Workout.objects.create(name='Pullups', user='Batman', team='DC')
        Workout.objects.create(name='Squats', user='Superman', team='DC')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
