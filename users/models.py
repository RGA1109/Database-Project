from django.db import models

# Create your models here.


class Tester(models.Model):

    name = models.CharField(db_column='name'),
    age = models.IntegerField(db_column='age'),

    class Meta:
        db_table = 'tester'
