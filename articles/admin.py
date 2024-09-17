from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Topic, Article, FAQ


admin.site.register([Topic, Article, FAQ])