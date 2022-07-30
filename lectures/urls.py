from django.urls import  path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='lectures'

urlpatterns = [
    path("",views.home,name="home"),
    path('upload/',views.upload_lecture,name="uploadLec"),
    path("addStage/",views.add_stage,name="add_stage"),
    path('<str:stage>/', views.view_lectures, name='view_lectures'),
    path('<str:stage>/addLecture', views.add_lectures, name='add_lecture'),
    path('<str:stage>/<slug:les>/', views.lessons, name="lessons"),

    path('<str:stage>/deleteStage', views.delete_stage, name='delete_stg'),
    path('<str:stage>/<slug:lect>/deleteLecture', views.delete_lecture, name='delete_lect'),
    path('<str:lect>/<str:title>/deleteLesson', views.delete_lesson, name='delete_lesson'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)