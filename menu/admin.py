from django.contrib import admin

# Register your models here.
from .models import Menu, MenuItem

class MenuItemAdmin(admin.ModelAdmin):
	list_display = ['title',  'updated']
	search_fields = ['title']
	date_hierarchy = 'timestamp'

	class Meta:
		model = MenuItem
	
admin.site.register(MenuItem, MenuItemAdmin)


class MenuAdmin(admin.ModelAdmin):
	list_display = ['title', 'updated']
	search_fields = ['title']
	date_hierarchy = 'timestamp'

	class Meta:
		model = Menu
	
admin.site.register(Menu, MenuAdmin)