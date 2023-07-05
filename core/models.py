import os 
import uuid 
from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                    PermissionsMixin
from .choices import GENDER_CHOICES, GENDER_PREFRENCE, LOCATION_PREFERENCE, \
                    AGE_GROUP

def user_image_file_path(instance, filename):
    """Generates file path for user image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/user/image', filename) 


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Email is must required!')
        user = self.model(email=self.normalize_email(email), **extra_fields) 
        user.set_password(password)
        user.save(using=self.db)

        return user 

    def create_superuser(self, email, password):
        """Create a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model"""
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def __str__(self):
        return '{}'.format(self.email)


class UserInfoManager(models.Manager):
    def create_userinfo(self, user, **extra_kwargs):
        user_info = self.model(**extra_kwargs)
        user_info.save(using=self.db)
        
        return user 
    

class UserInfo(models.Model):
    """User's Info"""
    user = models.OneToOneField(User, related_name="parent_user", on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_image_file_path)
    age = models.IntegerField()
    bio = models.CharField(max_length=400)
    hobbies = models.CharField(max_length=255)
    height = models.IntegerField()
    gender = models.CharField(max_length=255 ,choices=GENDER_CHOICES, default=GENDER_CHOICES[0][0])
    location = models.CharField(max_length=255, choices=LOCATION_PREFERENCE, default=LOCATION_PREFERENCE[0][0])
    preffered_age_group = models.CharField(max_length=255, choices=AGE_GROUP,default=AGE_GROUP[0][0])
    preffered_location = models.CharField(max_length=255, choices=LOCATION_PREFERENCE, default=LOCATION_PREFERENCE[0][0])
    preffered_gender = models.CharField(max_length=255 ,choices=GENDER_PREFRENCE, default=GENDER_PREFRENCE[0][0])

    objects = UserInfoManager()

    def __str__(self):
        return '{}'.format(self.user)


class FriendList(models.Model):
    """ User's Friend list"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user")
    friends = models.ManyToManyField(User, blank=True, related_name="friends")

    def __str__(self):
        return '{}{}'.format(self.user, self.friends.all())

    def add_friend(self, account):
        """Add a new friend"""
        if not account in self.friends.all():
            self.friends.add(account)
            self.save()
    
    def remove_friend(self, account):
        """Remove a friend"""
        if account in self.friends.all():
            self.friends.remove(account)
    
    def unfriend(self, removee):
        """Initiating the action of unfriending someone"""
        remover_friends_list = self  #person terminating the friendship

        # Remove friend from remover friend list
        remover_friends_list.remove_friend(remove)

        #Remove friend from removee friend list
        friends_list = FriendList.objects.get(user=removee)
        friends_list.remove_friend(self.user)


class FriendRequest(models.Model):
    """
    Friend Request consist of two main parts:
    1> Sender:
            - Person sending/initiating the friend request
    2> Reciever:
            - Person recieving the friend request
    """

    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    reciever = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reciever")
    is_active = models.BooleanField(blank=True, null=False, default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.sender)  
    
    def accept(self):
        """
        Accept a friend request
        Update both Sender and Reciever friend lists
        """
        # request goes into try 
        try :
            #now if the user has already some friends (which means it has a FriendList object ) so this 
            #will not throw error 
            #print('frist acive=?', self.is_active)
            self.is_active = False
            self.save()
            #print('frist acive now =?', self.is_active)
            reciever_friend_list = FriendList.objects.get(user=self.reciever)
            # #print(reciever_friend_list)
            # #print(self.sender)
            # reciever_friend_list.save()
            #print('What?')
            if reciever_friend_list : 
                ##print('FreindList object exist for Reciever')
                reciever_friend_list.add_friend(self.sender)
                reciever_friend_list.save()
                try :
                    #if sender has not any Friend yet this will throw error
                    sender_friend_list = FriendList.objects.get(user=self.sender)
                    if sender_friend_list:
                        #print('Exist for sender')
                        sender_friend_list.add_friend(self.reciever)
                        
                        self.is_active = False
                        self.save()
                        sender_friend_list.refresh_from_db()
                except FriendList.DoesNotExist:
                    sender = FriendList(user=self.sender)
                    #print('active or not', self , self.is_active)
                    self.is_active = False
                    sender.save()
                    sender.add_friend(self.reciever)
                    sender.save()
                    #print('Just made new Sender object for first time for this user in inner try')
                    sender.refresh_from_db()
        except FriendList.DoesNotExist:
            #print('catched')    
            reciever = FriendList(user=self.reciever)
            reciever.save()
            #print('Just made new Reciever object for first time for thi user')
            reciever.add_friend(self.sender)
            reciever.save()
            reciever.refresh_from_db()


            sender = FriendList(user=self.sender)
            #print('catched2')
            #print('ACtive=?', self.is_active) 
            self.is_active = False
            #print('ACtive=?', self.is_active) 
            sender.save()
            #print('Just made new Sender object for first time for thi user')
            sender.add_friend(self.reciever)
            sender.save()
            sender.refresh_from_db()
        


    def decline(self):
        """
        Decline a friend request.
        It is "declined" by setting the 'is_active' field to False
        """
        self.is_active = False
        self.save()
    
    def cancel(self):
        """
        canceling through settings?
        """
        self.is_active = False
        self.save()


    