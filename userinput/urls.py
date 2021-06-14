from django.urls import path

from . import views
import accounts

urlpatterns = [
    path('user_input',views.user_input, name='user_input'),
    #path('add',views.add, name='add'),
    path('analytics',views.analytics, name='analytics'),
    path('accounts/logout',accounts.views.logout, name='logout')
]