from django.urls import path

from . import views
import accounts

urlpatterns = [
    path('user_input',views.user_input, name='user_input'),
    path('user_input1',views.user_input1, name='user_input1'),
    path('analytics',views.analytics, name='analytics'),
    path('ianalytics',views.ianalytics, name='ianalytics'),
    path('delete/<int:id>/',views.delete_data, name='deletedata'),
    path('delete1/<int:id>/',views.delete_data1, name='deletedata1'),
    path('<int:id>/',views.update_data, name='updatedata'),
    path('<int:id>/1/',views.update_data1, name='updatedata1'),
    path('accounts/logout',accounts.views.logout, name='logout'),
    path('accounts/login',accounts.views.login, name='login'),
    path('accounts/register',accounts.views.register, name='register')
]