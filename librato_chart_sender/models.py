from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Configuration(models.Model):
    librato_user = models.CharField(max_length=250)
    librato_api_key = models.CharField(max_length=100)
    recipients_emails = models.TextField()
    chart_ids = models.CommaSeparatedIntegerField(max_length=250)
    interval = models.IntegerField()
    duration = models.IntegerField()
    template = models.CharField(max_length=100)

    def __str__(self):
    	return (' | ').join([self.librato_user, self.librato_api_key, self.recipients_emails, self.chart_ids, str(self.interval), str(self.duration), self.template])
