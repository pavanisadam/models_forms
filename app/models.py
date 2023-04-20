from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_member=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.topic_member



class Webpage(models.Model):
    topic_member=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,unique=True)
    url=models.URLField()
    email=models.EmailField(default='pavani@gmail.com')
    def __str__ (self):
        return self.name

class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    author=models.CharField(max_length=100)
    date=models.DateField()
    def __str__(self):
        return self.author