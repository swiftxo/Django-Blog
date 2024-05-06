from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from members.views import ChangePassword
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_blog.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    path('<int:uid>/password/', ChangePassword.as_view(template_name = 'registration/change-password.html'))

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
