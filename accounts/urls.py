from django.urls import path

from .models import sample_view
from .views import UserListView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('sample-main/', sample_view, name='sample-view'),

]
