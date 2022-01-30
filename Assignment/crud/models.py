from django.db import models

# Create your models here.


class Userdata(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()

    def __str__(self):
        return '{} {}'.format(self.name, self.age)

    def __unicode__(self):
        return '{} {}'.format(self.name, self.age)


class Errorcode(models.Model):
    message = models.CharField(max_length=700)

    def __str__(self):
        return "{} {}".format(self.status_code, self.message)

    def __unicode__(self):
        return "{} {}".format(self.status_code, self.message)
