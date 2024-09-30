from django.urls import path


from homeworkApplication2 import views

urlpatterns = [
    path('h2/', views.hello2),
    path('hay2/', views.howAreYou2),
    path('g2/', views.goodbye2),
]
