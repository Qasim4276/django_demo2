from django.shortcuts import render,redirect
from .models import Room, Message
from django.http import HttpResponse,JsonResponse
# Create your views here.

def home(request):
    return render(request,'home.html')

def checkview(request):
    room_name = request.POST['room_name']
    username = request.POST['username']
    if Room.objects.filter(name=room_name).exists():
        return redirect('/'+room_name+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room_name)
        new_room.save()
        return redirect('/'+room_name+'/?username='+username)
    
def room(request,room):
    room_detail = Room.objects.get(name=room)
    print(room_detail)
    user_name = request.GET.get('username')
    return render(request,'room.html',{
        'username':user_name,
        'room_detail':room_detail,
        'room':room})
    
def send(request):
    username = request.POST['username']
    room_id = request.POST['room_id']
    message = request.POST['message']
    new_message = Message.objects.create(value=message,user = username,room = room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')
        
def getMessages(request,room):
    room_details = Room.objects.get(name=room)
    message = Message.objects.filter(room=room_details.id)
    return JsonResponse({'messages':list(message.values())})

