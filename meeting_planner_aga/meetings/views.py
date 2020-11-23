from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory

from .models import Meeting, Room

# Create your views here.
def detail(request, id):
    meeting = get_object_or_404(Meeting, pk=id)
    return render(request, "meetings/detail.html",{"meeting": meeting})

def room_detail(request, id):
    room = get_object_or_404(Room, pk=id)
    return render(request, "meetings/room_details.html", {"room": room})

def rooms_list(request):
    return render(request, "meetings/all_rooms.html", {"rooms_list": Room.objects.all()})

MeetingForm = modelform_factory(Meeting, exclude=[])

def new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        
    else:
        form = MeetingForm()
    return render(request, "meetings/new.html", {"form": form})