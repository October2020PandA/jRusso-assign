from django.urls import path
from . import views

urlpatterns = [
    path('', views.testerHome, name='testerHome'),
    path('<int:tid>/', views.takeTest, name='takeTest'),
    path('<int:tid>/submit', views.submitTest, name='submitTest'),
    path('<int:tid>/review/', views.reviewTest, name='reviewTest'),
    path('review/', views.reviewQG, name='reviewQG'),
    path('<int:tid>/grade/', views.grade, name='grade'),
]