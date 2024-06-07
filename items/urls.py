from django.urls import path, reverse_lazy
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', login_required(views.ItemListView.as_view()), name='item_list'),
    path('item/<int:pk>/', login_required(views.ItemDetailView.as_view()), name='item_detail'),
    path('item/create/', login_required(views.ItemCreateView.as_view()), name='item_create'),
    path('item/<int:pk>/delete/', login_required(views.ItemDeleteView.as_view()), name='item_delete'),
]