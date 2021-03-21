from django.contrib import admin
from apps.DragonOathApp import models

# Register your models here.

admin.site.register(models.Userinfo)
admin.site.register(models.Roleinfo)
admin.site.register(models.Pageview)
admin.site.register(models.BooksInfo)
admin.site.register(models.ForeignAuthor)
admin.site.register(models.Mark)
admin.site.register(models.Author)
admin.site.register(models.Holmes)
