from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse

from django.contrib.auth.decorators import login_required

from .models import Topic
from .forms import ContactForm
from .forms import TopicForm

# Create your views here.
def index(request):
    """The home page for Silver"""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """Show all medications."""
    topics = Topic.objects.filter(owner=request.user).order_by('expiration_date')
    context = {'topics': topics }
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """Show a single medication and all its entries"""
    medication = get_object_or_404(Topic, id=topic_id)

    # Make sure the topic belongs to the current user.
    if medication.owner != request.user:
        raise Http404

    context = {'medication': medication}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """Add a new topic"""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:medications'))

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

def map(request):
    """The support page for Silver"""
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            return render(request, 'learning_logs/map.html', {'success': True, 'form': ContactForm()})
    return render(request, 'learning_logs/map.html', {'form': form})

def reports(request):
    """The support page for Silver"""
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            return render(request, 'learning_logs/reports.html', {'success': True, 'form': ContactForm()})
    return render(request, 'learning_logs/reports.html', {'form': form})

def citizen_roster(request):
    """The support page for Silver"""
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            return render(request, 'learning_logs/citizen_report.html', {'success': True, 'form': ContactForm()})
    return render(request, 'learning_logs/citizen_report.html', {'form': form})

def camera(request):
    """The support page for Silver"""
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            return render(request, 'learning_logs/camera.html', {'success': True, 'form': ContactForm()})
    return render(request, 'learning_logs/camera.html', {'form': form})
