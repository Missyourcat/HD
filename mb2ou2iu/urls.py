from django.urls import path
from .views import MainContentList


urlpatterns = [
    path('main_content/', MainContentList.as_view(), name='main_content_list'),
]