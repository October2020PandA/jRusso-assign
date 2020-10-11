from django.urls import path
from . import views

urlpatterns = [
    path('', views.question, name='question'),
    path('question_group/', views.qg_form, name='qg_form'),
    path('question_group/<int:qgid>/', views.qg_view, name='qg_view'),
    path('question_group/<int:qgid>/testers/', views.qg_testers, name='qg_testers'),
    path('question_group/<int:qgid>/testers/add', views.qg_testerAdd, name='qg_testerAdd'),
    path('question_group/create', views.qg_create, name='qg_create'),
    path('question_group/<int:qgid>/read', views.qg_read, name='qg_read'),
    path('question_group/<int:qgid>/update', views.qg_update, name='qg_update'),
    path('question_group/<int:qgid>/delete', views.qg_delete, name='qg_delete'),
    path('question_group/<int:qgid>/question/', views.q_form, name='q_form'),
    path('question_group/<int:qgid>/question/create', views.q_create, name='q_create'),
    path('question_group/<int:qgid>/question/<int:qid>/read', views.q_read, name='q_read'),
    path('question_group/<int:qgid>/question/<int:qid>/update', views.q_update, name='q_update'),
    path('question_group/<int:qgid>/question/<int:qid>/delete', views.q_delete, name='q_delete'),
]