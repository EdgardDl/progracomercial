from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_pub, name='listar_pub'),
    path('post/<int:pk>/', views.detalle_pub, name='detalle_pub'),
    path('post/new', views.post_new, name='post_new'),
]
