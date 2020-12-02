from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.mail import send_mail
from threading import Thread

class Post(models.Model):
	idPost = models.AutoField(primary_key=True, verbose_name='idPost')
	title = models.CharField(max_length=255, verbose_name='Заголовок поста')
	text = models.TextField(verbose_name='Текст поста')
	author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор поста')
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name='Дата создания поста')



	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title


	class Meta():
		verbose_name = 'Пост'
		verbose_name_plural = 'Посты'
		db_table = 'posts'
		ordering = ['-idPost']


class News(models.Model):
	idPost = models.AutoField(primary_key=True, verbose_name='idPost')
	owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userown', verbose_name='Владелец подписки')
	authorSub = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор поста')
	postSub = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост')
	notRead = models.BooleanField(default=True, verbose_name='Пост не прочитан')

	def __unicode__(self):
		return 'Subscription of user {self.owner}'

	def __str__(self):
		return 'Subscription of user {self.owner}'


	class Meta():
		verbose_name = 'Новости'
		verbose_name_plural = 'Новости'
		db_table = 'news'
		ordering = ['-idPost']


class Subscriptions(models.Model):
	idScr = models.AutoField(primary_key=True, verbose_name='idScr')
	owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userow', verbose_name='Владелец подписки')
	authorSub = models.CharField(max_length=255, verbose_name='Автор пдписки')


	def __unicode__(self):
		return 'Subscription of user {self.owner}'

	def __str__(self):
		return 'Subscription of user {self.owner}'


	class Meta():
		verbose_name = 'Подписка'
		verbose_name_plural = 'Подписка'
		db_table = 'Subscription'
		ordering = ['idScr']


# Функция обработки сигнала post_save, которая вызывается 
# внутри регистрируемой функции my_callback через Thread
def indef(sender):
	instance = Post.objects.latest('timestamp')
	subscr_list = Subscriptions.objects.filter(authorSub=instance.author)
	for el in subscr_list:
		instance_sub = News()
		instance_sub.authorSub = instance.author
		instance_sub.owner = el.owner
		instance_sub.postSub = instance
		instance_sub.save()
		try:
			send_mail('Add a new post in your News', 
				'User {} add a new post. See it in the http://localhost:8000/news/'.format(instance_sub.owner), 
				'from@example.com',  ['{instance_sub.owner.email}'], fail_silently=False)
		except Exception as e:
			print('Letter was not send to user {} by E-mail: {}'.format(instance_sub.owner, instance_sub.owner.email))


def my_callback(sender, **kwargs):
	print('in my_callback')
	thread = Thread(target=indef, args=(sender,))
	thread.start()	



post_save.connect(my_callback, sender=Post)