from django.db import models


class Nationality(models.Model):
    name = models.CharField(max_length=100, default='Unknown')

    def __str__(self):
        return f"{self.name}"


class Position(models.Model):
    name = models.CharField(max_length=50, default='Unknown')

    def __str__(self):
        return f"{self.name}"


class League(models.Model):
    name = models.CharField(max_length=100, default='Unknown')
    logo_url = models.URLField(max_length=300, null=True)

    def __str__(self):
        return f"{self.name}"


class Team(models.Model):
    name = models.CharField(max_length=100, default='Unknown')
    logo_url = models.CharField(max_length=300, null=True)
    league = models.ForeignKey(League, related_name='LeagueTeam', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Player(models.Model):
    name = models.CharField(max_length=100, default='Unknown')
    image_url = models.URLField(max_length=300, null=True)
    team = models.ForeignKey(Team, related_name='TeamPlayer', on_delete=models.CASCADE)
    nationality = models.ForeignKey(Nationality, related_name='NationalityPlayer', on_delete=models.CASCADE)
    position = models.ForeignKey(Position, related_name='PositionPlayer', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"
