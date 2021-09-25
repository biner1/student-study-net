from django.urls import path
from . import views

app_name='polls'
urlpatterns = [
    path('',views.vote,name='vote'),
    path('detail/',views.detail,name='detail'),
    
]