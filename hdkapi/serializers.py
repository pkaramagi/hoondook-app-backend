#serializers.py

from rest_framework import serializers

#import Api Models
from .models import Category,TPWords, Diary, AppUser

#create serializers for Api Models

class TPWordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TPWords
        fields = ('id','content','author','date','page', 'category_id','status')


class CategorySerializer(serializers.ModelSerializer):
    tpwords = TPWordsSerializer(many = True, read_only= True)
    class Meta:
        model = Category
        fields =  ('id','name', 'description', 'created_at', 'status','tpwords')

class DiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Diary
        fields = ('id','date','image_link','tp_words_id','content','author_id')

class AppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUser
        fields = ('id','username', 'password','email','phone')

