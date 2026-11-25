from django.urls import path
from .views import home, product_create,product_update,product_delete

urlpatterns = [
    path('', home, name='home'),
    path('create/', product_create, name='create'),
    path('update/<int:id>/', product_update, name='update'),
    path('delete/<int:id>/', product_delete, name='delete'),
]
