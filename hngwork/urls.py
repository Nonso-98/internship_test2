from django.urls import path
from . import views  # Import the whole file instead of specific classes

urlpatterns = [
    path('profiles/', views.ProfileCreateView.as_view(), name='profile-create'),
    path('list/', views.ProfileListView.as_view(), name='profile-list'),
    path('<uuid:id>/', views.ProfileDetailView.as_view(), name='profile-detail'),
    path('<uuid:id>/delete/', views.ProfileDeleteView.as_view(), name='profile-delete'),
]
