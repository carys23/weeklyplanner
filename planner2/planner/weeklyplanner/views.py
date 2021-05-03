from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import SignUpForm, EditProfileForm
from .forms2 import ListForm


from datetime import datetime, timedelta, date
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe
import calendar
from itertools import groupby
from calendar import HTMLCalendar



from datetime import datetime, timedelta, date
from django.views import generic
from django.urls import reverse



def notes2(request):
    day = {"day": Week.objects.all()}
    return render  ( request, "weeklyplanner/notes2",day)







def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, ('You have updated your password'))
            return redirect('index')
    else:
        form = PasswordChangeForm(user=request.user)
        
    context = {'form': form}
    return render(request, 'weeklyplanner/change_password.html', context)



def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ('You have edited your profile'))
            return redirect('index')
    else:
        form = EditProfileForm( instance=request.user)
        
    context = {'form': form}
    return render(request, 'weeklyplanner/edit_profile.html', context)



def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,('Logged in'))
            return redirect('index') 

        else: 
            messages.success(request,('Wrong username or password'))
            return redirect('login')
    else: 
        return render(request, 'weeklyplanner/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ('You have been logged out'))
    return redirect('index')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ('You have registered'))
			return redirect('index')
	else:
		form = SignUpForm()
	
	context = {'form': form}
	return render(request, 'weeklyplanner/register.html', context)




def index(request):
    all_items = Note.objects.all()
    return render (request, "weeklyplanner/index.html", {'all_items':all_items})



def notes(request):
    if request.method == 'POST':
        form = ListForm (request.POST or None) 

        if form.is_valid():
            form.save()
            all_items = Note.objects.all()
            messages.success(request, ('Added to planner'))
            return render (request, "weeklyplanner/notes.html", {'all_items':all_items})

    else: 
        all_items = Note.objects.all()
        return render (request, "weeklyplanner/notes.html", {'all_items':all_items})




def delete(request, note_id):
    item = Note.objects.get(pk=note_id)
    item.delete()
    messages.success(request, ('Removed from planner'))
    return redirect('notes')

def cross_off(request, note_id):
    item = Note.objects.get(pk=note_id)
    item.completed = True
    item.save()
    return redirect('notes')

def uncross(request, note_id):
    item = Note.objects.get(pk=note_id)
    item.completed = False
    item.save()
    return redirect('notes')

def edit(request, note_id):
    if request.method == 'POST':
        form = ListForm (request.POST or None) 

        if form.is_valid():
            form.save()
            all_items = Note.objects.all()
            messages.success(request, ('Added to planner'))
            return render (request, "weeklyplanner/edit.html", {'all_items':all_items})

    else: 
        item = Note.objects.get(pk=note_id)
        return render (request, "weeklyplanner/edit.html", {'item':item})

# def get_event(request, EventForm):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = EventForm(request.POST)
#         form.save()
#         return HttpResponseRedirect('/thanks/')
        # return render(request, 'notes.html', {'form': form})