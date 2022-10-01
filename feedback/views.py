from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Feedback
from django.urls.base import reverse_lazy

class FeedbackCreateView(CreateView):
    model = Feedback
    fields = ['topic', 'rating', 'good', 'bad']
    template_name = "feedback/index.html"
    success_url = reverse_lazy('feedback:index')
    
