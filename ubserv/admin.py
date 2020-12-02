from django.contrib import admin
from .models import Post, News, Subscriptions


class PostModelAdmin(admin.ModelAdmin):
	list_display = ['idPost', 'title', 'text', 'author', 'timestamp']
	list_display_links = ['title']
	search_fields = ['title', 'author']



	class Meta:
		model = Post


class NewsModelAdmin(admin.ModelAdmin):
	list_display = ['idPost', 'owner', 'authorSub', 'postSub', 'notRead']
	list_display_links = ['idPost']
	search_fields = ['authorSub', 'author']


	class Meta:
		model = News


class SubscriptionsAdmin(admin.ModelAdmin):
	list_display = ['idScr', 'owner', 'authorSub']
	list_display_links = ['idScr']
	search_fields = ['authorSub', 'owner']

	class Meta:
		model = News


admin.site.register(Post, PostModelAdmin)
admin.site.register(News, NewsModelAdmin)
admin.site.register(Subscriptions, SubscriptionsAdmin)