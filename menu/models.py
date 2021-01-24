from django.db import models
from django.urls import reverse

# Create your models here.

class Menu(models.Model):
	title         = models.CharField(max_length=120)
	slug          = models.SlugField(blank=True, unique=True)
	named_url = models.CharField(max_length=255, verbose_name='Named URL', blank=True)
	is_visible = models.BooleanField(default=True, verbose_name='Visibility')
	timestamp       = models.DateTimeField(auto_now_add=True, auto_now =False)
	updated         = models.DateTimeField(auto_now=True, auto_now_add=False)


	class Meta:
		verbose_name = 'menu'
		verbose_name_plural = 'menu'

	def __str__(self):
		return self.title

	def get_full_path(self):
		if self.named_url:
			url = reverse(self.named_url)
		else:
			url = '/{}/'.format(self.slug)
		return url



class MenuItem(models.Model):
	menu = models.ForeignKey(Menu, related_name='items',
		verbose_name='menu', blank=True, null=True,
		on_delete=models.CASCADE)
	parent = models.ForeignKey('self', blank=True, null=True,
		related_name='items',
		verbose_name='parent menu item',
		on_delete=models.CASCADE)
	title = models.CharField(max_length=100, verbose_name='Item title')
	url = models.CharField(max_length=255, verbose_name='Link', blank=True)
	named_url = models.CharField(max_length=255, verbose_name='Named URL', blank=True,
		help_text='Named url from your urls.py file')
	is_visible = models.BooleanField(default=True, verbose_name='Visibility')
	timestamp       = models.DateTimeField(auto_now_add=True, auto_now =False)
	updated         = models.DateTimeField(auto_now=True, auto_now_add=False)



	class Meta:
		verbose_name = 'menu item'
		verbose_name_plural = 'menu items'

	def get_url(self):
		if self.named_url:
			url = reverse(self.named_url)
		elif self.url:
			url = self.url
		else:
			url = '/'

			return url

	def __str__(self):
		return self.title

