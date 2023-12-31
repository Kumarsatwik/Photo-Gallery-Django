from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255,null=False,blank=False)

    def __str__(self):
        return self.name

class Photo(models.Model):
    description=models.TextField()
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    image=models.ImageField(null=False,blank=False)

    def __str__(self):
        return self.description
