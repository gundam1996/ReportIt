from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from .forms import ReporterSignUpForm, AgentSignUpForm, AdditionalForm

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def dashboard(request):
    return render(request, 'webpage/dashboard.html')

def home(request):
    return render(request, 'webpage/home.html')

def login(request):
    html = 'This is a login page'
    #template = loader.get_template('webpage/login.html')
    #return HttpResponse(template.render(request))
    #return HttpResponse(html)
    return render(request, 'webpage/login.html')


def reporterSignup(request):
    if request.method == 'POST':
        form = ReporterSignUpForm(request.POST)
        #print(form)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            form.save()
            return redirect('/')
    else:
        form = ReporterSignUpForm()
    return render(request, 'webpage/reporterSignup.html', {'form': form})

def agentSignup(request):
    if request.method == 'POST':
        form1 = AgentSignUpForm(request.POST)
        print (form1)
        form2 = AdditionalForm(request.POST)
        print(form2)
        if form1.is_valid() and form2.is_valid():
            model1 = form1.save()
            print(model1)
            model2 = form2.save(commit=False)
            print(model2)
            model2.user = model1
            model2.save()
            return redirect('/')
    else:
        form1 = AgentSignUpForm()
        form2 = AdditionalForm()
    return render(request, 'webpage/agentSignup.html', {'form1': form1, 'form2': form2})


def viewProfile(request):
    return render(request, 'webpage/profile.html')