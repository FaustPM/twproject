from django import forms
from .models import Feedback
from django.core.validators import validate_email


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['email', 'message']





