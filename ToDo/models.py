from django.db import models

# Create your models here.
class Bucket(models.Model):
  name = models.CharField(max_length=100)
  deleted = models.BooleanField(default=False)
  
  def __str__(self):
    return self.name


class Task(models.Model):
  title = models.CharField(max_length=200)
  completed = models.BooleanField(default=False, blank=True, null=True)
  # bucket = models.ForeignKey('Bucket', related_name='tasks',on_delete=models.CASCADE,blank=True,
  #       null=True)

  def __str__(self):
    return self.title