from django.db import models


class days(models.Model):
    day_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(null=False, blank=False, db_index=True)
    timestamp = models.DateTimeField(null=False, db_index=True)
    consumption = models.IntegerField(null=False)
    temperature = models.IntegerField(null=False)

    class Meta:
        db_table = 'days'


class months(models.Model):
    month_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(null=False, blank=False, db_index=True)
    timestamp = models.DateTimeField(null=False, db_index=True)
    consumption = models.IntegerField(null=False)
    temperature = models.IntegerField(null=False)

    class Meta:
        db_table = 'months'
