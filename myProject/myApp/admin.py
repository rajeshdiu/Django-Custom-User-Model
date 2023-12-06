from django.contrib import admin

from .models import *

from django.contrib.auth.admin import UserAdmin
class userModel(UserAdmin):
    
    list_display=["username","user_type","profile_pic"]

admin.site.register(customUser,userModel)