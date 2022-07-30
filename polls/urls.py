from django.urls import path
from . import views

app_name='polls'
urlpatterns = [
    path('',views.vote,name='vote'),
    path('vote/<str:lecture>/',views.update_vote,name='updatevote'),
    path('detail/',views.vote_detail,name='detail'),
    
]