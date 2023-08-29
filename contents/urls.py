from django.urls import path
from .views import GetAllContents,RateContent

urlpatterns = [
    path('', GetAllContents.as_view()),
    path('<int:content_id>/', RateContent.as_view()),
]
