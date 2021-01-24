# simple-django-app-tree-menu

This django app implements the tree menu via template tag every menu and item menu are stored in the database editable in the Django admin
There can be several menus on one page. They are identified by name
When you click on the menu, you go to the URL specified in it. The URL can be specified either explicitly or through a named url.
Exactly 1 database request is required to render each menu
the app allows you to add a menu (one or more) to the database through the admin panel, and draw a menu by name on any desired page.
 {% draw_menu 'main_menu'%}
