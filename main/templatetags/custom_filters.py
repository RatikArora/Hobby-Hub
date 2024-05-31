from django import template
from main.models import Profile

register = template.Library()

@register.filter(name='get_profile_image_url')
def get_profile_image_url(username):
    profile = Profile.objects.get(user__username=username)
    # print("in custom filter") 
    return profile.image.url



    