from django import forms
from .models import Post, News, Subscriptions
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
	

	class Meta:
		model = Post
		fields = ['idPost', 'title', 'text']



class NewsForm(forms.ModelForm):
	

	class Meta:
		model = News
		fields = ['idPost', 'notRead']


class SubscriptionsForm(forms.ModelForm):
	
	authorSub = forms.ModelMultipleChoiceField(
        queryset = User.objects.all(), 
        widget  = forms.CheckboxSelectMultiple,
        label = 'Авторы постов'
    )

	class Meta:
		model = Subscriptions
		fields = ['authorSub']