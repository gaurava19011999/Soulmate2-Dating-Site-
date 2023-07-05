from django.shortcuts import render

from core.models import User, UserInfo, FriendRequest
from django.contrib.auth.decorators import login_required
from .location_group import LOCATION_GROUPS
from django.http import HttpResponse
import json

def HomePage(request, *args, **kwargs):
    return render(request, 'home/home.html')

@login_required
def Homefeed(request, *args, **kwargs):
    current_user_id = request.user.id
    user_name = User.objects.filter(id=current_user_id)
    print('Name====',user_name[0])
    current_user_info = UserInfo.objects.filter(user=user_name[0]).values()[0]
    print('current--', current_user_info['location'])
    print('Info===',current_user_info['preffered_gender'])
    current_user_pref_age_group = current_user_info['preffered_age_group']
    current_user_pref_gender = current_user_info['preffered_gender']
    current_user_pref_location = current_user_info['preffered_location']
   # print('Info===',current_user_info['age'])
    #print('Info===',current_user_info)
    if current_user_pref_age_group == 'Y':
        start = 18
        end = 25
    elif current_user_pref_age_group == 'O':
        start = 25
        end = 45
    else:
        start = 45
        end = 100

    if current_user_pref_location in LOCATION_GROUPS['North']:
        loc_group = 'N'
        print('Yes')
    else:
        loc_group = 'S'
        print('NO')
    print('Loc=', loc_group)

    #need to write logic for not to show the user who he has already sent friend request 
    # or not in friend list 


    #calling all the matching profiles
    matching = UserInfo.objects.filter(
        age__gte=start, age__lte=end,
        location__startswith=loc_group,
        gender=current_user_pref_gender, 
    ).values()

    catching = UserInfo.objects.filter(
        age__gte=start, age__lte=end,
        location__startswith=loc_group,
        gender=current_user_pref_gender, 
    )

    print('"CATCHing===', catching)

    print('matching===', matching)
 
    all = []
    #getting user_id of all matthcing profiles
    for y in range(len(matching)):
        all.append(matching[y]['user_id'])
  #  print('all==', all)


    #filtering already add-friend-requested ids 
    already_friend = FriendRequest.objects.filter(sender=user_name[0]).values()
    print(len(already_friend))
    liked = len(already_friend)
    rec_ids = []
    for x in range(liked):
    #    print('reciever id=', already_friend[x]['reciever_id'])
        rec_ids.append(already_friend[x]['reciever_id'])
    rec_ids.sort()
    print(rec_ids)

    #creating profiles that user must watch 
    profiles = []
    for z in matching:
        if z['user_id'] not in rec_ids:
            profiles.append(z)
    print('profiles====', profiles)
    print(already_friend)

    #print(profiles[0],)
   # print('length==',   len(profiles))
    #up = profiles
    #print('UP+++++', up)
    p = catching[0]
    if hasattr(p, 'user'):
        new_user = p.user
    print('NEW==', new_user)

    context = {
        'profiles' : profiles,
        'catching' : catching,
    }

    return render(request, 'home/match.html', context)

@login_required
def matching_system(request, *args, **kwargs):

    current_user_id = request.user.id
    user_name = User.objects.filter(id=current_user_id)
    print('Name====',user_name[0])
    current_user_info = UserInfo.objects.filter(user=user_name[0]).values()[0]
    print('current--', current_user_info['location'])
    print('Info===',current_user_info['preffered_gender'])
    current_user_pref_age_group = current_user_info['preffered_age_group']
    current_user_pref_gender = current_user_info['preffered_gender']
    current_user_pref_location = current_user_info['preffered_location']
   # print('Info===',current_user_info['age'])
    #print('Info===',current_user_info)
    if current_user_pref_age_group == 'Y':
        start = 18
        end = 25
    elif current_user_pref_age_group == 'O':
        start = 25
        end = 45
    else:
        start = 45
        end = 100

    if current_user_pref_location in LOCATION_GROUPS['North']:
        loc_group = LOCATION_GROUPS['North']
        print('Yes')
    else:
        loc_group = LOCATION_GROUPS['South']
        print('NO')
    print('Loc=', loc_group)


    #filtering already add-friend-requested ids 
    already_friend = FriendRequest.objects.filter(sender=user_name[0]).values()
    print(len(already_friend))
    liked = len(already_friend)
    rec_ids = []
    for x in range(liked):
    #    print('reciever id=', already_friend[x]['reciever_id'])
        rec_ids.append(already_friend[x]['reciever_id'])
    rec_ids.sort()
    print('REC_IDS==',rec_ids)


    #calling all the matching profiles excluding already frnd rqst sent
    matching = UserInfo.objects.filter(
        age__gte=start, age__lte=end,
        location__in=loc_group,
        gender=current_user_pref_gender, 
    ).exclude(user_id__in=rec_ids)

    print('matching===', matching)
 

    context = {
        # 'profiles' : profiles,
        'profiles' : matching,
    }
    return render(request, 'home/match.html', context)

@login_required
def send_friend_request(request, *args, **kwargs):
    user = request.user
    print('Sending ==', user)
    
    if request.method == 'POST' :
        payload = {}
        print('ifififififififi')
        try: 
            print('forst try')
            user_id = request.POST.get('reciever_user_id')
            reciever = User.objects.get(pk=user_id)
            friend_requests = FriendRequest.objects.filter(sender=user,reciever=reciever).values()
            print(friend_requests, len(friend_requests))
        
           # print('status=', friend_request_status)
            if len(friend_requests) > 0 :
                friend_request_status = friend_requests[0]['is_active']
                print('WHY THE')
                try:
                    print('Got  into try 2 ')
                    for requset in friend_requests:
                        print('For loop not working ofcrs')
                        print('okok')
                        if friend_request_status == True:
                            payload['response'] = "Already Sent!"
                            print('Request is freking active!')
                            
                            raise Exception("You already sent them a Friend Request.")
                        #If none are active, then create a new one      
                        friend_request = FriendRequest(sender=user, reciever=reciever)
                        friend_request.save()
                        payload['response'] = "Friend Request Sent"
                except Exception as e:
                    payload['response'] = str(e)
                    print('Default exception got mee 1 = ', str(e))
            else:
                print('Got  into else ')
                #there are no friend request so create one
                friend_request = FriendRequest(sender=user, reciever=reciever)
                friend_request.save()
                payload['response'] = "Friend Request Sent"
        except Exception as f:
            payload['response'] = str(f)
            print('Default exception got mee=', str(f))  

    else:
        print('GOTCHAAAA')
        payload['response'] = "You must be authenticated"
    return HttpResponse(json.dumps(payload), content_type="application/json")


@login_required
def accept_friend_request(request, *args, **kwargs):
    user_id = request.user.id
    payload = {}

    if request.method == 'POST':
        #use try here
        print('Got the GET request')
        friend_request = request.POST.get('friend_request_id')
        print('frriend_req==', friend_request)
        invoke = FriendRequest.objects.get(pk=friend_request)
        checking = FriendRequest.objects.filter(pk=friend_request).values()[0]
        print('alfaflanafna======',checking['reciever_id'])
        if checking['reciever_id'] == user_id :
            if friend_request :
                invoke.accept()
                payload['response'] = "Friend request accepted"
            else:
                payload['response'] = "Something went wrong"
        #garbage 
        else:
            payload['response'] = "THis is not your reauest"


    return HttpResponse(json.dumps(payload), content_type='application/json')

@login_required
def decline_friend_request(request, *args, **kwargs):
    user_id = request.user.id
    payload = {}

    if request.method == 'POST':
        #use try here
        print('Got the GET request')
        friend_request = request.POST.get('friend_request_id')
        print('frriend_req==', friend_request)
        invoke = FriendRequest.objects.get(pk=friend_request)
        checking = FriendRequest.objects.filter(pk=friend_request).values()[0]
        print('alfaflanafna======',checking['reciever_id'])
        if checking['reciever_id'] == user_id :
            if friend_request :
                invoke.decline()
                payload['response'] = "Friend request declined"
            else:
                payload['response'] = "Something went wrong"
        #garbage 
        else:
            payload['response'] = "THis is not your reauest"


    return HttpResponse(json.dumps(payload), content_type='application/json')

@login_required
def notification(request, *args, **kwargs):
    current_user_id = request.user.id
    print(current_user_id)
    print(request.user)
    
    requests = FriendRequest.objects.filter(reciever_id=current_user_id, is_active=True)
    request_values = FriendRequest.objects.filter(reciever_id=current_user_id, is_active=True).values()
    print('CHECK==', requests)
    print('value==', request_values)
    
    context = {
    'res' : requests,
    'ids' : request_values,
    }

    return render(request, 'home/notification.html', context)