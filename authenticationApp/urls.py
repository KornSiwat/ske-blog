from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from authenticationApp.views import LoginView
from authenticationApp.views import RegistrationView
from authenticationApp.views import ForgetPasswordView
from authenticationApp.views import ProfileView
from authenticationApp.views import EditProfileView
from authenticationApp.views import PasswordChangeView
from authenticationApp.views import AccountVerificationView
from authenticationApp.views import SendVerificationEmailView
from authenticationApp.views import LogoutView
from authenticationApp.views import VerifyAccountView
from authenticationApp.views import ResetPasswordView

app_name = 'authenticationApp'

urlpatterns = [
    path('login/', LoginView, name='login'),
    path('register/', RegistrationView, name='register'),
    path('forgetpassword/', ForgetPasswordView, name='forget-password'),
    path('resetpassword/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
        ResetPasswordView, name='reset-password'),
    path('profile/verify/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
        VerifyAccountView,name='verify-account'),

    path('profile/', ProfileView, name='profile'),
    path('profile/edit', EditProfileView, name='edit-profile'),
    path('profile/changepassword/', PasswordChangeView, name='password-change'),
    path('profile/verification/', AccountVerificationView, name='account-verification'),
    path('sendverificationemail/', SendVerificationEmailView, name='send-verification-email'),
    path('logout/', LogoutView, name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
