from apps.books.views import ListBookView, CategoryView, DetailBookView
from apps.scraper.views import ScraperView
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from apps.books import views


urlpatterns = [
    path(r'scraper/', ScraperView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
