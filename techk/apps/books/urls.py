from apps.books.views import ListBookView, CategoryView, DetailBookView
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from apps.books import views


urlpatterns = [
    path(r'books/', views.ListBookView.as_view()),
    path(r'books/<int:pk>/', views.DetailBookView.as_view()),
    path(r'categories/', views.CategoryView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
