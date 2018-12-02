from django.shortcuts import render


# Master list of all html page redirects
def index(request):
    """The home page for application"""
    return render(request, 'learning_logs/index.html')


def map(request):
    """The map page"""
    return render(request, 'learning_logs/map.html')


def reports(request):
    """Citizens reports for individual people"""
    return render(request, 'learning_logs/reports.html')


def citizen_details(request):
    """Citizens report details for individual people"""
    return render(request, 'learning_logs/citizen-details.html')


def citizen_roster(request):
    """Master roster for all the citizens"""
    return render(request, 'learning_logs/citizen-roster.html')


def tavern(request):
    """Basic loading page for locations switches depending on the location"""
    return render(request, 'learning_logs/tavern.html')


def confirm(request):
    return render(request, 'learning_logs/confirm.html')




