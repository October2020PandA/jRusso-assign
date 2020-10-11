from django.urls import path
from . import views

urlpatterns = [
    path('', views.testerHome, name='testerHome'),
    path('<int:tid>/', views.takeTest, name='takeTest'),
    path('<int:tid>/submit', views.submitTest, name='submitTest'),
    path('<int:tid>/review/', views.reviewTest, name='reviewTest'),
]