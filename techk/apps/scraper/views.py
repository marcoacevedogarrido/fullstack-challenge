from apps.books.serializers import BookSerializer, CategorySerializer
from apps.books.models import Category
from apps.books.models import Book

from rest_framework import generics, status
from rest_framework.response import Response

from django.utils.text import slugify
from collections import OrderedDict
import collections
from .utils import (categories,pages_t,page_books,book_info)


class ScraperView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = []
    authentication_classes = []

    def post(self, request):
        create_categories = categories()
        categories_collection = collections.defaultdict(str)

        for cat in create_categories:
            category, created_cat = Category.objects.get_or_create(name=cat)
            categories_collection.update({category.slug: category})

        pages = pages_t()
        if len(pages) == 0:
            return Response(status=400)

        links = []
        for page in pages:
            one_page_book = page_books(page)
            if len(one_page_book) > 0:
                links = one_page_book + links

        created_books = list(Book.objects.values_list('title', flat=True))
        links = [scrape for scrape in links if scrape['title'] not in created_books]

        if len(links) == 0:
            return Response({"Datos Actualizados"},status=200)

        for data in links:
            book = book_info(data)
            if bool(book):
                book_category = categories_collection.get(slugify(book['category']))
                new_book, created_book = Book.objects.get_or_create(upc=book['upc'],defaults={'category':book_category,'title':book['title'],'price':book['price'],'stock':book['stock'],'product_description':book['product_description'],})
        return Response(status=200)
