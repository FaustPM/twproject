from django.shortcuts import redirect
from django.core.validators import validate_email
from .forms import FeedbackForm
from django.views.generic.edit import CreateView
from django.contrib import messages

if_email = False
if_message = False


class FeedbackView(CreateView):
    def post(self, request, **kwargs):
        form = FeedbackForm(self.request.POST)
        if form.is_valid():
            last_form = form.save(commit=False)
            last_form.save()
        return redirect('/')
