from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
# Create your views here.

products = {
    "1": "phone",
    "2": "laptop",
    "3": "game"}

texts = {
    "1st": 1,
    "2nd": 2,
    "3rd": 3,
}


def wel(r):
    return HttpResponse("welcome")


def reporter(r, id):
   
    if id in products:
        return HttpResponse(products[id])
    else:
        return HttpResponseNotFound("item not found")


def t_rep(request, text):
    if text in texts:
        return HttpResponseRedirect(f"/product/{str(texts[text])}/")
    return HttpResponseNotFound("item not found")
