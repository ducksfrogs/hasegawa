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

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
