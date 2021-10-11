from django.urls import path
from . import views


urlpatterns = [
    path('' , views.post_list , name='post_list'),
    path('post/<int:pk>/' , views.post_details , name='post_details'),
    path('post/new' , views.post_form , name='new_post'),
    path('post/<int:pk>/edit' , views.post_edit , name='post_edit'),
    path('post/draft', views.post_draft_list , name='post_draft_list'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<int:pk>/delete' , views.post_delete , name='post_delete'),
    path('post/<int:pk>/comment/' , views.add_comment , name='add_comment_to_post'),
    path('post/<int:pk>/comment/remove/' , views.remove_comment , name='remove_comment'),
    path('post/<int:pk>/comment/approve/' , views.approve_comment , name='approve_comment'),
]