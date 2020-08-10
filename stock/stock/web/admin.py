from django.contrib import admin
from .models import Profile, Portfolio, Watchlist

# Register your models here.
admin.site.register(Profile)
admin.site.register(Portfolio)
admin.site.register(Watchlist)