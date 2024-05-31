from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.utils import timezone
from django import forms



class hobbies(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    hobby = models.CharField(max_length=50)



class post(models.Model):
    data = models.TextField()
    pic = models.ImageField(upload_to='media/images',blank=True)
    date_posted = models.DateTimeField(default=timezone.now)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.CharField(max_length=100)


class follower(models.Model):
    followed_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='followed_by')
    following = models.ForeignKey(User,on_delete=models.CASCADE,related_name='following')

    def __str__(self):
        return f"{self.followed_by.username} is following {self.following.username}"
    
    class Meta:     
        unique_together = ('followed_by','following')



class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(blank=True)

    def __str__(self):
        return f'{self.user_profile.username} Profile'
    


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('timestamp',)

    def __str__(self):
        return f"From {self.sender} to {self.recipient}: {self.content}"


