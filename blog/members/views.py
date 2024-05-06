from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
# Create your views here.
from .forms import SignUpForm,EditProfileForm,ChangePasswordForm,ProfileForm
from django.http import HttpResponseForbidden
from my_blog.models import Profile


class RegisterUser(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class EditUser(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/personal_info.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
    
class ChangePassword(PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = 'registration/change-password.html'
    success_url = reverse_lazy('password_success')

    def dispatch(self, request, *args, **kwargs):
        uid = self.kwargs.get('uid')
        if request.user.is_authenticated and request.user.id == uid:
            return super().dispatch(request, *args, **kwargs)
        else:
            return custom_forbidden_view(request)

def password_success(request):
    return render(request, 'registration/password_success.html',{})

def custom_forbidden_view(request):
    return render(request, 'forbidden.html', status=403)

class ProfilePage(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ProfilePage,self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id = self.kwargs['pk'])
        context["page_user"] = page_user
        return context
    
class EditProfilePage(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile.html'
    fields = ['bio','profile_pic','instagram_link','twitter_link','website_link','github_link','discord_link','spotify_link','soundcloud_link','youtube_link']
    success_url = reverse_lazy('home')

def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('edit_profile')  # Redirect to a success page or the profile page
    else:
        form = ProfileForm(instance=request.user.profile)
    
    return render(request, 'edit_profile.html', {'form': form})
