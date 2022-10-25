from django.urls import path, re_path
from . import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('save_request/', views.save_request, name='save_request'),
    path('show_request', views.show_checklist, name='show_checklist'),



    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='home'),

]
