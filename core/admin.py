from django.contrib import admin
from core    import models

class UserAdmin(admin.ModelAdmin):
    oredering = ['id']
    list_display = ['id', 'email', 'first_name']


class UserInfoAdmin(admin.ModelAdmin):
    oredering = ['id']
    list_display = ['id', 'user', 'age', 'gender', 'location']
    list_display_links = ['id', 'user']


class FriendListAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ['id', 'user']


class FriendRequestAdmin(admin.ModelAdmin):
    oredering = ['id']
    list_display = ['id', 'is_active', 'sender', 'reciever']
    search_fields = ['is_active']
    list_editable = ['is_active']

admin.site.register(models.User, UserAdmin)
admin.site.register(models.UserInfo, UserInfoAdmin)
admin.site.register(models.FriendList, FriendListAdmin)
admin.site.register(models.FriendRequest, FriendRequestAdmin)
