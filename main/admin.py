from django.contrib import admin
from main.models import hobbies,post,follower,Notification,Profile,Message

class hobbiesadmin(admin.ModelAdmin):
    list_display=('username','hobby')

admin.site.register(hobbies,hobbiesadmin)


class postadmin(admin.ModelAdmin):
    list_display=('data','pic','date_posted','username','tags')

admin.site.register(post,postadmin)


admin.site.register(follower)

admin.site.register(Notification)

admin.site.register(Profile)


admin.site.register(Message)

