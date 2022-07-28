from django.shortcuts import redirect
from django.core.validators import validate_email
from django.core.validators import ValidationError
from .forms import FeedbackForm
from django.views.generic.edit import CreateView
from django.contrib import messages


class FeedbackView(CreateView):
    email_message = None

    def post(self, request, **kwargs):
        form = FeedbackForm(self.request.POST)
        if form.is_valid():
            last_form = form.save(commit=False)
            last_form.save()
        else:
            data = form.data
            email = data.get('email')
            message = data.get('message')
            try:
                validate_email(email)
            except ValidationError:
                messages.error(request, 'Incorrect email!')
            if not message:
                messages.warning(request, 'Required field!')
        return redirect('/')
