from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_challenges = {
    "january": "Eat no meat for the entire month.",
    "february": "Walk for atleast 20 minutes every day.",
    "march": "Learn Django for atleast 20 minutes every day.",
    "april": "Eat 7-9 cups of veggies every day.",
    "may": "Do brain training exercises.",
    "june": "Cook a new recipe every day.",
    "july": "Sleep for 8-9 hours every night.",
    "august": "Walk 10,000 steps every day.",
    "september": "Follow a productivity system.",
    "october": "Follow a morning routine.",
    "november": "Follow a bedtime routine.",
    "december": "Check email once or twice a day."
}

# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href='{month_path}'>{capitalized_month}</a></li>"
        response_data = f"<ul>{list_items}</ul>"

    return HttpResponse(response_data)

def monthly_challenges_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)



def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported.</h1>")