from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CategorySerializer, TPWordsSerializer, DiarySerializer, AppUserSerializer
from .models import Category, TPWords, Diary, AppUser

#create Api views 
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer

class TPWordsViewSet(viewsets.ModelViewSet):
    queryset = TPWords.objects.select_related('category_id').all().order_by("?")
    serializer_class = TPWordsSerializer

class DiaryViewSet(viewsets.ModelViewSet):
    queryset = Diary.objects.select_related('tp_words_id').all().order_by('id')
    serializer_class = DiarySerializer

class AppUserViewSet(viewsets.ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer
    