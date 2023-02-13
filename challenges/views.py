from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse



# Create your views here.
monthly_challenges = {
    "january": "walk a mile",
    "february": "walk at least 20 min a day",
    "march": "learn a new skill",
    "april": "eat lots of tacos",
    "may": "learn a new skill",
    "june": "learn a new skill",
    "july": "eat lots of tacos",
    "august": "walk a mile",
    "september": "walk at least 20 min a day",
    "october": "eat lots of tacos",
    "november": "walk a mile",
    "december": None,
}


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('Invalid month')
    redirect_month = months[month-1]
    path = reverse("monthly_challenge", args=[redirect_month])
    return HttpResponseRedirect(path)


def monthly_challenge(request, month):

    # try:
        challenge_text = monthly_challenges[month]
        
        return render(request,"challenges/challenge.html",{
            "text":challenge_text,
            "month":month
        })
    # except:
        # raise Http404()


def index(request):
    months = list(monthly_challenges.keys())
    list_items = ""
    return render(request, "challenges/index.html",{
        "months":months
    })
