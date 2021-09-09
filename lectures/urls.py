from django.urls import  path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='lectures'

urlpatterns = [
    path("",views.home,name="home"),
    path('upload/',views.uploadLecture,name="uploadLec"),
    path('<str:stage>/', views.lectures, name='lectures'),
    path('<str:stage>/<slug:les>/', views.lessons, name="lessons"),
    

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)