from django.contrib import admin

from forumsite.models import Category,Thread,Comment
# Register your models here.

admin.site.register(Category)
admin.site.register(Thread)
admin.site.register(Comment)