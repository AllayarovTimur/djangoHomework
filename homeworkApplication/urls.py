from django.urls import path


from homeworkApplication import views

urlpatterns = [
    path('h/', views.hello),
    path('hay/', views.howAreYou),
    path('g/', views.goodbye),
]
