from django.urls import path,reverse_lazy
from . import views

urlpatterns = [
    path('', views.ItemListView.as_view(), name='item_list'),
    path('item/<int:pk>/', views.ItemDetailView.as_view(), name='item_detail'),
    path('item/create/', views.ItemCreateView.as_view(), name='item_create'),
    path('item/<int:pk>/delete/', views.ItemDeleteView.as_view(), name='item_delete'),
]