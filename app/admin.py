from django.contrib import admin
from app.models import Category, Comment, Post, Profile
# Register your models here.
admin.site.register([Category, Comment, Post, Profile])
