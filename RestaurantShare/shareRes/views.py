from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'shareRes/index.html')
def restaurantDetail(request):
    return render(request, 'shareRes/restaurantDetail.html')
def restaurantCreate(request):
    return render(request, 'shareRes/restaurantCreate.html')
def categoryCreate(request):
    return render(request, 'shareRes/categoryCreate.html')