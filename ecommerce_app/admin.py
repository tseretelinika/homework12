from django.contrib import admin
from .models import Profile, Product, Cart, Payment, ProductHistory, Comment, Rate

admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Payment)
admin.site.register(ProductHistory)
admin.site.register(Comment)
admin.site.register(Rate)
