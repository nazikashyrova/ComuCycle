from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, View
from .models import Item
from .forms import ItemForm
from django.urls import reverse_lazy
from django.shortcuts import redirect

class ItemListView(LoginRequiredMixin, ListView):
    model = Item
    template_name = 'item_list.html'
    context_object_name = 'items'

class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item
    template_name = 'item_detail.html'
    context_object_name = 'item'

class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'item_form.html'

    def form_valid(self, form):
        form.instance.uploader = self.request.user
        response = super().form_valid(form)
        return redirect(reverse_lazy('item_list'))

class ItemDeleteView(View):
    def post(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        item.delete()
        return redirect('item_list')  # Redirect to item list page after deletion

