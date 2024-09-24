from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.poll_list, name='poll_list'),
    path('polls/<int:poll_id>/', views.poll_detail, name='poll_detail'),
    path('polls/create/', views.create_poll, name='create_poll'),
    path('polls/<int:poll_id>/update/', views.update_poll, name='update_poll'),
    path('polls/<int:poll_id>/delete/', views.delete_poll, name='delete_poll'),
    path('polls/<int:poll_id>/vote/<int:choice_id>/', views.vote, name='vote'),
]