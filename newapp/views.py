from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import customer
from .forms import CustomerInfoForm


def addnew(request):

    if request.method == 'POST':

        formset = CustomerInfoForm(request.POST)

        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect("/homepage")
    else:
        formset = CustomerInfoForm()
        return render(request, 'addnew.html', {'formset': formset})


def homepage(request):
    x = customer.objects.all()

    return render(request, 'index.html', {'data': x})
