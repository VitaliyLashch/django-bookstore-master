from django.contrib import admin
from .models import Categories, Author, book, status_order, order

admin.site.register(Categories)
admin.site.register(Author)
admin.site.register(book)
admin.site.register(status_order)
admin.site.register(order)
