
'''


In Django, URLs are the front door to your web application. URLs are configured in urls.py,
 which determines what the application does based on the URL that a user visits in a web browser. 
 The views.py file is where you can define your view functions. When a user requests a URL, Django 
 decides which view it will send it to. 


from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world),
]


'''
