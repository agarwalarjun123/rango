from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default= 0)
    likes = models.IntegerField(default=0)
    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name
class Page(models.Model):
    title = models.CharField(max_length=128, unique=True)
    url = models.URLField()
    views = models.IntegerField(default= 0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.title