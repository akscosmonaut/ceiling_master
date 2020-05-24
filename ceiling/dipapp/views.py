from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def ceiling_kind(request):
    return render(request, "ceiling_kind.html")


def advice(request):
    return render(request, "advice.html")


def gallery(request):
    return render(request, "gallery.html")


def price(request):
    return render(request, "price.html")


def review(request):
    return render(request, "review.html")

