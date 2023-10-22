from django.urls import path
from . import views


app_name = 'food'

urlpatterns = [
    path('', views.index, name='index'),
  #  path('love/', views.love, name='love'),
    path('<int:item_id>/',views.detail, name='detail'),
    path('add/',views.add_item, name='add_item'),
    path('update/<int:id>/', views.update_item, name= 'update_item'),
    path('delete/<int:id>/', views.delete_item, name='delete_item'),
    path('custom/',views.custom, name='custom'),
    #path('random-array/', RandomArray.as_view(), name='random-array'),
]

