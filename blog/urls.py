from django.urls import path
from .views import HomePageView, AboutPageView



urlpatterns = [
    # function base view
    # path("", HomePageView, name="home")
    
    
    
    path('', HomePageView.as_view(), name="home"),
    path('about/', AboutPageView.as_view(), name="about")
]
