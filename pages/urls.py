from django.urls import path
from .views import HomePageView, AboutPageView, MojaPageView

urlpatterns = [
    path('moja/', MojaPageView.as_view(), name='moja'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
]
