from django.shortcuts import render,redirect
from.models import Hotel
from .forms import BookingForm
# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def rooms(request):
    dict_room={
        'rom':Hotel.objects.all()
    }
    return render(request,'rooms.html',dict_room)
def booking(request):
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form=BookingForm()
    dict_forms={
        'form':form
    }
    return render(request,'booking.html',dict_forms)
