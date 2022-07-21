from django.shortcuts import render, redirect
from .forms import FeedbackForm
from django.views.generic import View


class FeedbackForm(View):
    def post(self, request):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
