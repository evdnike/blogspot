from django.contrib import admin
from .models import Post, Comments
# Register your models here.


class AdminComments(admin.StackedInline):
    model = Comments
    extra = 2


class AdminPost(admin.ModelAdmin):
    fields = ['title', 'image', 'body',]
    inlines = [AdminComments]


admin.site.register(Post, AdminPost)