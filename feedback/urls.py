from django.urls import path
from .views import FeedbackForm


urlpatterns = [
    path('', FeedbackForm.as_view(), name='feedback_view')
]