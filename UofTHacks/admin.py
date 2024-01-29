from django.contrib import admin
from .models import Memento, UserProfile
# Register your models here.

admin.site.register(Memento)
admin.site.register(UserProfile)