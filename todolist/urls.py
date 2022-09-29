from django.urls import path
from todolist.views import add_new_task, register
from todolist.views import login_user
from todolist.views import logout_user 
from todolist.views import show_todolist
app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create_task/', add_new_task, name='create_task'),
]