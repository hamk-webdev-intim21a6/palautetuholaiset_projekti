from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.forms import ModelForm
from django.views.generic.edit import FormView

from .models import Dictionary