from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^entrar/$', auth_views.login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^sair/$', auth_views.logout, name='logout'),
    url(r'^cadastre-se/$', views.register, name='register'),
    url(r'^editar/$', views.edit, name='edit'),
    url(r'^editar-senha/$', views.edit_password, name='edit_password'),
]
