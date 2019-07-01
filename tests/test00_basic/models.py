from django.db import models


class A(models.Model):
    primary_key = models.IntegerField(primary_key=True)
    x = models.IntegerField(name='y', db_column='z')


class B(models.Model):
    pass
