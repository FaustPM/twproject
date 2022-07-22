from django.shortcuts import redirect
from .forms import FeedbackForm
from django.views.generic.edit import CreateView


class FeedbackView(CreateView):
    def post(self, request):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
