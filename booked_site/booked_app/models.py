from django.db import models

class EventManager(models.Model):
    name = models.CharField()
    address = models.ForeignKey('Address')

class Talent(models.Model):
    name = models.TextField()

class Match(model.Model):
    talent = models.ForeignKey('Talent')
    event_manager = models.ForeignKey('EventManager')

class Address(models.Model):
    street = models.TextField()
    city = models.TextField()
    province = models.TextField()
    code = models.TextField()
