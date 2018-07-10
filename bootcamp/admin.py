from django.contrib import admin
from .models import Articles , Messages, Feeds
from django.contrib.auth.models import User


@admin.register(Feeds)
class FeedsAdmin(admin.ModelAdmin):
	list_display = ('user' , 'status','last_modified')

@admin.register(Messages)
class MessagesAdmin(admin.ModelAdmin):
	list_display = ('message', 'date_created', 'last_modified')


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
	list_display = ('title' , 'date_created', 'last_modified')


# admin.site.register(Articles)
# admin.site.register(Messages)
# Register your models here.
