from django.db import models
import datetime
from django.contrib.auth.models import User 
from django.urls import reverse

# Create your models here.
class JobPost(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(max_length = 250)
    date = models.DateField(("Date"), default=datetime.date.today)
    maxPeople = models.IntegerField()
    compensation = models.TextField(max_length = 250)
    # Add the foreign key linking to a user instance
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'jobpost_id': self.id})
        # return reverse('index')

class Photo(models.Model):
    url = models.CharField(max_length=200) #we store url where it hosted (AWS)
    jobpost = models.ForeignKey(JobPost, on_delete=models.CASCADE) #on_delete - means if we delete this it will delete the chain
    
    def __str__(self):
        #cat_id will referrence cat property above
        return f"Photo for jobpost_id: {self.jobpost_id} @{self.url}" 


class Volonteer(models.Model):
  name = models.CharField(max_length=50)
  
  def __str__(self):
      return self.name

  def get_absolute_url(self):
      return reverse('volonteer_detail', kwargs={'pk': self.id})

class JobApplicationMap(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    jobPost = models.ForeignKey(JobPost, on_delete=models.CASCADE)
