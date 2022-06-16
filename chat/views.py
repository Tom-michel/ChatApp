from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from chat.models import Room, Message
from django.contrib.auth.models import User

# Create your views here.

# pahe d'accueil
def home(request):
    roomList = Room.objects.all()
    userList = User.objects.all()

    # userRoomList = []
    # for user in roomList:
    #     userRoomList.append(user)

    context = {
        'roomList':roomList,
        'userList':userList,
    }
    return  render(request, 'chat/home.html', context)



# page de chat
def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    context = {
        'username': username,
        'room': room,
        'room_details': room_details
    }
    return render(request, 'chat/room.html', context)




def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)




def createRoom(request, u1, u2):
    user1 = User.objects.get(id=u1).username
    user2 = User.objects.get(id=u2).username
    room = 'salon-'+user1+'-'+user2

    new_room = Room.objects.create(name=room, user1=user1, user2=user2)
    new_room.save()
    return redirect('/'+room+'/?username='+user1)




def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    print(new_message.errors)
    return HttpResponse('Message sent successfully')



def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    context = {"messages":list(messages.values())}
    return JsonResponse(context)



