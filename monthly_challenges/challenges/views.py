from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def monthly_challenges_by_number(request, month):
    return HttpResponse(month)


def monthly_challenges(request, month):
    challenge_text = None,
    if month == "january":
        challenge_text = "Eat no meat for the entire month."
    elif month == "february":
        challenge_text = "Walk for atleast 20 minutes everyday."
    elif month == "march":
        challenge_text = "Learn Django for atleast 20 minutes everyday."
    else:
        return HttpResponseNotFound("This month is not supported.")
    return HttpResponse(challenge_text)