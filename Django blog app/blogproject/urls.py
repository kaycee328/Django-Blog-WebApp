# PROJECT VIEWS

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views
from django.urls import reverse_lazy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogapp.urls')),

    path('register/', user_views.register, name='register' ),
    path('profile/', user_views.profile, name='profile' ),
    path('login/', user_views.Login_user.as_view(), name='login'),
    path('logout/', user_views.Logout_user.as_view(), name='logout' ),

    path('password-reset/', auth_views.PasswordResetView.as_view( template_name = 'users/password_reset.html', success_url = reverse_lazy('password_reset_confirm')), name='password_reset' ),
    path('confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'password_reset_confirm.html',success_url = reverse_lazy('reset_password_done')), name='password_reset_confirm' ),
    path('done/', auth_views.PasswordResetDoneView.as_view(template_name = 'password_reset_done.html'), name='password_reset_done' ),

    # path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'password_reset_confirm.html', success_url=reverse_lazy('reset_password_done')), name='reset_password_confirm'),
    # path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(template_name = 'password_reset_done.html'), name='reset_password_done' ),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

    
    
    
    
    # path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html', redirect_authenticated_user=True), name='login' ),
    # path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name='logout' ),
    # path('userprofile/<int:pk>/', user_views.ViewUserProfile.as_view(), name='profile'),