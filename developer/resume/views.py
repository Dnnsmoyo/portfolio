# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .forms import ContactForm

from django.views.generic.list import ListView

from django.http import HttpResponseRedirect

# Create your views here.
def index_view(request):
    return render(request, 'resume/base.html',{})
    
def work_view(request):
    return render(request, 'resume/work.html',{})

    
def contact_view(request):
    form = ContactForm()
    return render(request, 'resume/contactform_list.html',{'form':form})

