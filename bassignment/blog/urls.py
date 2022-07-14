from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('<int:id>', detail, name = 'detail'),
    path('new/', new, name ='new'),
    path('new_with_django_form/', new_with_django_form, name = 'new_with_django_form'),
    path('create/', create, name = 'create'),
    path('create_with_django_form/', create_with_django_form, name = 'create_with_django_form'),
    path('update/<int:id>', update, name = 'update'),
    path('delete/<int:id>', delete, name = "delete"),
    path('create_comments/<int:id>', create_comments, name="create_comments"),
    path('delete_comments/<int:blog_id>/<int:comment_id>', delete_comments, name = "delete_comments"),
]
