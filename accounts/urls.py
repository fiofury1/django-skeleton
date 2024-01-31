from django.urls import path

from .views import logout_view, SignUpView


urlpatterns = [
    # The following routes are included via Django provided django.contrib.auth.urls:
    #   path('login/', views.LoginView.as_view(), name='login'),
    #   path('logout/', views.LogoutView.as_view(), name='logout'),
    #   path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    #   path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    #   path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    #   path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    #   path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    #   path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # Added Routes
    path('logout/', logout_view, name='logout'),
    path("signup/", SignUpView.as_view(), name="signup"),
]
