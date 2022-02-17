from django.contrib import admin
from rango import models
from django.contrib.sessions.models import Session
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
class PageAdmin(admin.ModelAdmin):
    list_display = ('title','category',"url")
# Register your models here.
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Page,PageAdmin)
admin.site.register(models.UserProfile)
admin.site.register(Session)