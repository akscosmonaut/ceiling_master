from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import UserForm, ReviewForm
from .models import Order


def index(request):
    userform = UserForm(auto_id=False)
    order = Order.objects.all()
    return render(request, "index.html", {"form": userform})


def create(request):
    if request.method == "POST":
        order = Order()
        order.name = request.POST.get("name")
        order.phone = request.POST.get("phone")
        order.save()
        return HttpResponseRedirect("/")
    else:
        userform = UserForm()
        return render(request, "index.html", {"form": userform})



def ceiling_kind(request):
    return render(request, "ceiling-kind.html")


def advice(request):
    return render(request, "advice.html")


def gallery(request):
    return render(request, "gallery.html")


def price(request):
    return render(request, "price.html")


def review(request):
    reviewform = ReviewForm(auto_id=False)
    order = Order.objects.all()
    return render(request, "review.html", {"form": reviewform})

