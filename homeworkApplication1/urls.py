from django.urls import path


from homeworkApplication1 import views

urlpatterns = [
    path('h1/', views.hello1),
    path('hay1/', views.howAreYou1),
    path('g1/', views.goodbye1),
]
