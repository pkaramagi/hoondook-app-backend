from django.db import models
from datetime import datetime

#Hoondok App api Models

# This class represents Category Model
class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    created_at =  models.DateTimeField(editable=False, default=datetime.now)
    status = models.IntegerField()

    def __str__(self):
        return self.name

    
#This class represents TPWord Model
class TPWords(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=50)
    date = models.DateField()
    page = models.CharField(max_length=50)
    status = models.IntegerField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tpwords')

    def __str__(self):
        return self.category_id.name + ' ' + self.content[:20]+'...'

#This class represents AppUser Model
class AppUser(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50,)
    email = models.EmailField()
    phone = models.CharField(max_length=50)

#This class represnets Diary Model
class Diary(models.Model):
    date = models.DateTimeField(auto_now_add=True, blank=True)
    image_link = models.CharField(max_length=200)
    tp_words_id = models.ForeignKey(TPWords, on_delete = models.CASCADE)
    content = models.TextField()
    author_id = models.ForeignKey(AppUser, on_delete=models.CASCADE)

