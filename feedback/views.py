from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Feedback
from django.urls.base import reverse_lazy

class FeedbackCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Feedback
    fields = ['movie', 'rating', 'good', 'bad']
    template_name = "feedback/index.html"
    success_url = reverse_lazy('feedback:index')
    def form_valid(self, form):
        # Set the form's author to the submitter if the form is valid
        form.instance.author = self.request.user
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())

def index(request):
    return render(request, 'feedback/index.html')