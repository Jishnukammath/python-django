from django.urls import path
from . import views

app_name='firstApp'

urlpatterns = [

    path('',views.demo,name="demo"),
    path('shop/<int:shop_id>',views.details,name="detail"),
    path('add/',views.add_product,name="add_product"),
    path('edit/<int:id>',views.edit,name="edit"),
    path('delete/<int:id>',views.delete,name="delete")
    
]