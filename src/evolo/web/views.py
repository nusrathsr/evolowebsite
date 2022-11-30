import json
from django.http import HttpResponse
from django.shortcuts import render
from web.forms import ContactForm

from web.models import Customer, Plan, Service, Team


def index(request):

    Customers = Customer.objects.all()
    Services = Service.objects.all()
    Teams = Team.objects.all()
    form = ContactForm()
    plans = Plan.objects.all()
    context = {
        "Customers": Customers,
        "Services": Services,
        "Teams": Teams,
        "form": form,
        "Plans": plans,
    }
    return render(request, "index.html", context=context)


def contact(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        response_data = {
            "status": "success",
            "title": "Thankyou for yout interest",
            "message": "Our team will contact you soon"
        }
    else:
        response_data = {
            "status": "error",
            "title": "An error occured",
            "message": "Please try again"
        }

    return HttpResponse(json.dumps(response_data), content_type="application/javascript")
