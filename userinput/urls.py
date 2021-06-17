from django.urls import path

from . import views
import accounts

urlpatterns = [
    path('user_input',views.user_input, name='user_input'),
    path('analytics',views.analytics, name='analytics'),
    path('ianalytics',views.ianalytics, name='ianalytics'),
    path('delete/<int:id>/',views.delete_data, name='deletedata'),
    path('<int:id>/',views.update_data, name='updatedata'),
    path('accounts/logout',accounts.views.logout, name='logout'),
    path('accounts/login',accounts.views.login, name='login'),
]