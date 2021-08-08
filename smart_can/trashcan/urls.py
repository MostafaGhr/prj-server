from django.urls import path
from . import views

urlpatterns = [
    path('can/', views.CanView.as_view()),
    path('can/<int:pk>/', views.CanDetailView.as_view()),
    path('can/<int:pk>/history', views.CanHistoryView.as_view()),

]
