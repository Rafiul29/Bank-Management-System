from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import FormView
from .forms import UserRegistrationForm,UserUpdateForm
from django.contrib.auth import login,logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
class UserRegistrationView(FormView):
    template_name = 'accounts/user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('profile')
    
    def form_valid(self,form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form) # form_valid function call hobe jodi sob thik thake
    
class UserLoginView(LoginView):
  template_name='accounts/user_login.html'
  
  def get_success_url(self):
    return reverse_lazy('home' )
  
  def form_valid(self, form):
      return super().form_valid(form)


# class UserLogoutView(LogoutView):
#     def get_success_url(self):
#         if self.request.user.is_authenticated:
#             logout(self.request)
#         return reverse_lazy('home')
    
# from django.contrib.auth import logout
# from django.urls import reverse_lazy
# from django.views import View
# from django.http import HttpResponseRedirect

class UserLogoutView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            logout(request)
        return HttpResponseRedirect(reverse_lazy('home'))


class UserBankAccountUpdateView(View):
    template_name = 'accounts/profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the user's profile page
        return render(request, self.template_name, {'form': form})
    

 
class PasswordChangeView(LoginRequiredMixin, FormView):
    template_name = 'accounts/pass_change.html'
    form_class = PasswordChangeForm
    success_url = reverse_lazy('profile')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.save()
        update_session_auth_hash(self.request, form.user)
        messages.success(self.request, 'Password changed successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Please correct the error below.')
        return super().form_invalid(form)