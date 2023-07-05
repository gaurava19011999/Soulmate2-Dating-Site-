from typing import List
from django.db.models.fields import CharField
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from chatroom.models import Room, Message
from core.models import User, UserInfo, FriendList
from django.http import HttpResponse, JsonResponse
import string, random

# Create your views here.



#   THIS SECTION IS ONLY FOR SITE DEVELOPERS(REDIRECT TO THE PAGE USING URL COPY/PASTE)   #
# 
# 
# 
# 




#  
def room(request,room):
    username = request.GET.get('username')
    room_details = Room.objects.get(roomid=room)
    #print('this is a room:',room)
    #print('this is a usernsme:',username)
    #print(room_details)
    current_user = request.user 

    #print('USer=', request.user)
    #print(current_user.id)

    obj = FriendList.objects.filter(user=current_user)
    #print('obj', obj)

    f_list = obj.all()
    #print('LIST==',f_list)

    ans=[]
    for frnd in obj.all():
        ans.append(frnd)
    #print('here new function')
    #print(ans[0])

    
    #print(i for i in f_list)
    return render(request,'room/messages2.html', {
        'username': username,
        'room': room,
        'room_details': room_details,
        'info': f_list,
    })
#   return render(request, 'chatroom/messages.html' )




#   THIS SECTION IS ONLY FOR SITE DEVELOPERS(REDIRECT TO THE PAGE USING URL COPY/PASTE)   #
#
#
#
def room2(request,room2):
    username = request.GET.get('username')
    
    room_details = Room.objects.get(roomid=room2)
    #print('this is a room:',room2)
    #print('this is a usernsme:',username)
    #print(room_details)
    current_user = request.user 

    #print('USer=', request.user)
    #print(current_user.id)

    obj = FriendList.objects.filter(user=current_user)
    #print('obj', obj)

    f_list = obj.all()
    #print('LIST==',f_list)

    ans=[]
    for frnd in obj.all():
        ans.append(frnd)
    #print('here new function')
    #print(ans[0])

    
    #print(i for i in f_list)
    return render(request,'room/messages3.html', {
        'username': username,
        'room': room2,
        'room_details': room_details,
        'info': f_list,
    })




#   THIS IS THE DEFAULT CHATROOM FUNCTION IN WHICH YOU CAN NOT SEE ANY CHAT   #
#
#
#
def default(request):
    current_user = request.user 

    #print('USer=', request.user)
    #print(current_user.id)

    obj = FriendList.objects.filter(user=current_user)
    #print('obj', obj)

    f_list = obj.all()
    #print('LIST==',f_list)

    ans=[]
    for frnd in obj.all():
        ans.append(frnd)
    #print('here new function')
    #print(ans[0])

    
    #print(i for i in f_list)
    context = {
        'info': f_list,
    }
    
   
    return render(request,'room/messages.html',context)



#   THIS IS THE MAIN FUNCTION ****PLEASE DON'T TOUCH WITHOUT SITE DEVELOPERS PERMISSION****   #
#
#
#
def check(request,data):
    username = request.user
    #print(type(username))
    username = str(username)
    #print('checking')
    #print(type(username))
    email = data
    doom=[]
    doom2=[]
    #print(doom)
    doom.append(username)
    doom.append(email)
    doom2.append(email)
    doom2.append(username)
    #print(username)
    #print('This is checkview')
    #print(email)
    #print(doom[0])
    #print(doom[1])
    #print(doom2[0])
    #print(doom2[1])
    room = ''.join(map(str, doom))
    #print(room)
    room2 = ''.join(map(str,doom2))
    #print(room2)
    if Room.objects.filter(roomid=room).exists():
#    return redirect('/'+room+'/?username='+username)
        room_details = Room.objects.get(roomid=room)
        #print('this is a room:',room)
        #print('this is a usernsme:',username)
        #print(room_details)
        current_user = request.user 

        #print('USer=', request.user)
        #print(current_user.id)

        obj = FriendList.objects.filter(user=current_user)
        #print('obj', obj)

        f_list = obj.all()
        #print('LIST==',f_list)

        ans=[]
        for frnd in obj.all():
            ans.append(frnd)
        #print('here new function')
        #print(ans[0])

    
        #print(i for i in f_list)
        return render(request,'room/messages2.html', {
            'username': username,
            'room': room,
            'room_details': room_details,
            'info': f_list,
        })       
    elif Room.objects.filter(roomid=room2).exists():
       # return redirect('/'+room2+'/?username='+username)
        room_details = Room.objects.get(roomid=room2)
        #print('this is a room:',room2)
        #print('this is a usernsme:',username)
        #print(room_details)
        current_user = request.user 

        #print('USer=', request.user)
        #print(current_user.id)

        obj = FriendList.objects.filter(user=current_user)
        #print('obj', obj)

        f_list = obj.all()
        #print('LIST==',f_list)

        ans=[]
        for frnd in obj.all():
            ans.append(frnd)
        #print('here new function')
        #print(ans[0])

    
        #print(i for i in f_list)
        return render(request,'room/messages2.html', {
            'username': username,
            'room': room2,
            'room_details': room_details,
            'info': f_list,
        })
    else:
        new_room = Room.objects.create(roomid=room)
        new_room.save()
#        return redirect('/'+room+'/?username='+username)
        room_details = Room.objects.get(roomid=room)
        #print('this is a room:',room)
        #print('this is a usernsme:',username)
        #print(room_details)
        current_user = request.user 

        #print('USer=', request.user)
        #print(current_user.id)

        obj = FriendList.objects.filter(user=current_user)
        #print('obj', obj)

        f_list = obj.all()
        #print('LIST==',f_list)

        ans=[]
        for frnd in obj.all():
            ans.append(frnd)
        #print('here new function')
        #print(ans[0])

    
        #print(i for i in f_list)
        return render(request,'room/messages2.html', {
            'username': username,
            'room': room,
            'room_details': room_details,
            'info': f_list,
        })  




#   HERE IS A UNIQUE KEY GENERATOR THIS CODE MAY USE IN FUTURE
#
#
#
#def ran_gen(size, chars=string.ascii_uppercase + string.digits):
#   return ''.join(random.choice(chars) for x in range(size))
  
## function call for random string
## generation with size 8 and string 
#i=ran_gen(16, "AEIOSUMDHDD7444SDVA23WSEDRT6YT543W3E4R5T6Y7U8I9OI8U7Y7U8JIKOLPOKIJUHYGTFCVGBHNJNHBGVFCD")



#   HERE IS AJAX SEND FUNCTION  #
#
#
#
def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']
    

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')



#   HERE IS AJAX GET FUNCTION   #
#
#
#
def getMessages(request, room):
    room_details = Room.objects.get(roomid=room)
    #print('this ijava s a :'+room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})



#   HERE IS AJAX SEND FUNCTION (WHICH IS USE INVERT SITUATION)  #
#
#
#
def send2(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']
    

    new_message = Message.objects.create(value=message, user=username, room2=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')




#   HERE IS AJAX GET FUNCTION (WHICH IS USE INVERT SITUATION)  #
#
#
#
def getMessages2(request, room2):
    room_details = Room.objects.get(roomid=room2)
    #print('this ijava s a :'+room2)

    messages = Message.objects.filter(room2=room_details.id)
    return JsonResponse({"messages":list(messages.values())})




#   HERE IS A TESTING FUNCTION DO ANY TYPE OF EXPERIMENTS HERE  #
def test(request):
    current_user_id = request.user.id
    #print('this is current user id:  ')
    #print(current_user_id)
    user_name = User.objects.filter(id=current_user_id)
    #print(user_name[0])
    return render(request,'room/test.html')

