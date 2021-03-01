from django.shortcuts import render, redirect
from .models import summary
from .forms import summaryForm
# Create your views here.


def index(request):
    return render(request, 'index.html')


def add(request):

    context = {'form': summaryForm}
    if request.method == "POST":
        form = summaryForm(request.POST)
        form.save()
        return redirect('index')

    return render(request, 'add.html', context)


def display(request):
    data = summary.objects.all().order_by('-date')
    context = {'data': data}
    return render(request, 'display.html', context)
