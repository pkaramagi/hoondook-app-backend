#urls.py

from django.urls import include, path
from rest_framework import routers
from . import views

#register Api routes and views

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'tpwords', views.TPWordsViewSet)
router.register(r'diary', views.DiaryViewSet)
router.register(r'author', views.AppUserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

