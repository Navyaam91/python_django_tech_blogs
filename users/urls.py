from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('logout', views.logout, name="logout"),
    #  path('forgot-password', views.forgot_password, name="forgot_password"),
    


    path(
        'forgot-password',
        auth_views.PasswordResetView.as_view(
            template_name='forgot_password.html',
            email_template_name='password_reset_email.html',
            success_url='/forgot-password/done/'
        ),
        name='forgot_password'
    ),

    path(
        'forgot-password/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='password_reset_done.html'
        ),
        name='password_reset_done'
    ),

    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='password_reset_confirm.html',
            success_url='/reset/done/'
        ),
        name='password_reset_confirm'
    ),

    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),


]
