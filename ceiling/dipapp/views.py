from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import UserForm, ReviewForm
from .models import Order, Review


def index(request):
    userform = UserForm()
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
    reviewform = ReviewForm()
    review = Review.objects.all().order_by('-created_at')
    print(review)
    return render(request, "review.html", {"form": reviewform, "review": review})


def create_review(request):
    if request.method == "POST":
        review = Review()
        review.name = request.POST.get("name")
        review.surname = request.POST.get("surname")
        review.text = request.POST.get("text")
        review.image = request.POST.get("image")
        review.save()
        return HttpResponseRedirect("/review")
    else:
        reviewform = ReviewForm()
        return render(request, "review.html", {"form": reviewform})

