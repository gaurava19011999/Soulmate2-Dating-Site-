from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from core.models import User, UserInfo

def Signup(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        #password validation
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'email is already in use!')
                return redirect('register')
            else:
                user = User.objects.create_user(email=email, password=password1, first_name=first_name,
                                last_name=last_name)
                user.save()
                messages.success(request, 'You are registererd and can log in')
                return redirect('login')
        else:
            messages.error(request, 'Password does not match')
            return redirect('sign_up')
    return render(request, 'accounts/sign_up.html')

def Login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            user = request.user 
            messages.success(request, 'You are now logged in')


            user_info = UserInfo.objects.filter(user=request.user)
            if user_info.exists():
                return redirect('matching')

            return redirect('profile')

        else:
            messages.error(request, 'Invalid Credentials')
            return render(request, 'accounts/login.html')

    return render(request, 'accounts/login.html')

@login_required
def logout(request):
  if request.method == 'POST':
    auth.logout(request)
   # messages.success(request, 'You are now logged out')
    return redirect('Homepage')

@login_required
def Profile(request):
    if request.method == 'POST'  :
        image = request.FILES['image1']
        bio = request.POST['bio']
        age = request.POST['age']
        gender = request.POST['gender']
        hobbies = request.POST['hobbies']
        height = request.POST['height']
        location = request.POST['location']
        pref_age = request.POST['prefered_age']
        pref_location = request.POST['prefered_location']
        pref_gender = request.POST['prefered_gender']
        
        user_id = request.user.id 

        user = User.objects.filter(pk=user_id)
      #  print('user=', user[0])

        user_info = UserInfo.objects.create(
            user=user[0], image=image, age=age,
            bio=bio, gender=gender, hobbies=hobbies,
            height=height, location=location, preffered_age_group= pref_age,
            preffered_location=pref_location, preffered_gender=pref_gender
        )
        user_info.save()

        return redirect('matching')

    return render(request, 'accounts/edit_profile.html')

# def Home(request):
#     return render(request, 'home/match.html')





