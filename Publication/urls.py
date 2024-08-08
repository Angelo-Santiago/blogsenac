from django.urls import path

from .views import about, contact, index, post, post_detail, create_publication

urlpatterns = [
    path('', index, name='index'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('post/new/', create_publication, name='create_publication'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('post/', post, name='post'),
]