from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:ref_code>/', views.home, name='home'),
    path('signup/', views.signup, name="signup"),
    path('signin/', views.signin, name="signin"),
    path('signout/', views.signout, name="signout"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('dashboard/update_profile/<int:pk>', views.update_profile, name="update_profile"),
    path('property-detail/<slug:slug>/', views.estate_details, name='estate_detail'),
]