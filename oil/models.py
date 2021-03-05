from django.db import models

class Vehcle(models.Model):
    rejist_num = models.IntegerField
    rejist_dist = models.CharField(max_length=6)


class Employee(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)


class Purchase(models.Model):
    item = models.CharField(max_length=100)
    item_amount = models.IntegerField(null=False)
    pur_data = models.DateTimeField('data published')


#class Sales(models.Model):
#    item = models.ForeignKey()
