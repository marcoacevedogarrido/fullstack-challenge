from apps.books.views import ListBookView, DetailBookView, CategoryView
from apps.scraper.views import ScraperView
from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'api/', include('apps.books.urls')),
    url(r'api/', include('apps.scraper.urls')),

]
