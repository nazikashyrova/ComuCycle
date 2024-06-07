from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import ProfileForm
from .models import User

# Register View
class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

# Login View
class LoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    next_page = ''

# Logout View
def custom_logout(request):
    # Additional actions before logout (if needed)
    logout(request)
    return redirect(reverse_lazy('login')) 

# Profile Edit View
class ProfileEditView(UpdateView):
    model = User
    form_class = ProfileForm
    template_name = 'profile_edit.html'
    success_url = reverse_lazy('item_list')

    def get_object(self):
        return self.request.user
