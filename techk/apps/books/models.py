from django.db import models
from django.template.defaultfilters import slugify

class Book(models.Model):
    category = models.ForeignKey("books.Category", on_delete=models.CASCADE, related_name="books", null=False)
    upc = models.CharField(max_length=200, unique=True, blank=False, null=False)
    title  = models.CharField(max_length=200, blank=False, null=False)
    product_description = models.TextField(blank=True, null=True)
    stock = models.IntegerField()
    price = models.FloatField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return 'Book {}'.format(self.title)


class Category(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    slug = models.CharField(max_length=200, blank=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return '{}'.format(self.name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
