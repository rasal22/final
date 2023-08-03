from django.urls import path
from . import views
#app_name='storeapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('computer', views.computer, name='computer'),
    path('commerce', views.commerce, name='commerce'),
    path('science', views.science, name='science'),
    path('philosophy', views.philosophy, name='philosophy'),
    path('psychology', views.psychology, name='psychology')

]

