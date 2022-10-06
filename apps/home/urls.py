from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('save_request/', views.save_request, name='save_request'),


    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='home'),

]
