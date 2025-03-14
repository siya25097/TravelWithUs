from django.shortcuts import render
from django.http import JsonResponse
from .forms import BookingForm
import logging
logger = logging.getLogger(__name__)
def home(request):
    return render(request, 'travel/home.html')

def destinations(request):
    return render(request, 'travel/destinations.html')

def packages(request):
    return render(request, 'travel/packages.html')

def contact(request):
    return render(request, 'travel/contact.html')

def book_now(request):
    if request.method == 'POST':
        print("Form submission received")
        print(f"POST data: {request.POST}")
        
        form = BookingForm(request.POST)
        if form.is_valid():
            print("Form is valid. Saving data.")
            form.save()
            return JsonResponse({'success': True})
        else:
            print(f"Form is invalid: {form.errors}")
            return JsonResponse({'success': False, 'errors': form.errors})
    else:
        print("Invalid request method. Only POST is allowed.")
    return JsonResponse({'success': False, 'errors': {'non_field_errors': 'Invalid request.'}})
