from django.urls import path
from . import views  # Import the whole file instead of specific classes

urlpatterns = [
    path('profiles/', views.ProfileView.as_view(), name='profile-create'),
    path('list/', views.ProfileListView.as_view(), name='profile-list'),
    path('profiles/<uuid:id>/', views.ProfileDetailView.as_view(),
         name='profile-detail'),
    path('profiles/<uuid:id>/delete/', views.ProfileDeleteView.as_view(), name='profile-delete'),
]
        