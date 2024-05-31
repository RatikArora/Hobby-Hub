from django.shortcuts import render,HttpResponse,HttpResponseRedirect,redirect
from .forms import RegisterForm,EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import hobbies,post,follower,Notification,Profile
from django.shortcuts import get_object_or_404
from datetime import datetime
from django.urls import reverse


@csrf_exempt
@login_required(login_url='login/')
def home(request):
    user = request.user.id
    print(user)
    response = render(request, 'home.html')
    return response


import re

def is_valid_username(username):
    # Define a regular expression pattern for valid usernames
    pattern = r'^[a-zA-Z0-9_]+$'
    return re.match(pattern, username) is not None



@csrf_exempt
def register(request):
    if request.method=="POST":
        form = RegisterForm(request.POST)
        username = request.POST.get('username')
        username = request.POST.get('username')
        if not is_valid_username(username):
            # Invalid username format, return an error to the user
            return render(request, 'register.html', {"form":form,'error': 1})

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(username,first_name,last_name,email,password)
        if User.objects.filter(email=email).exists():
            # messages.info(request,"Email taken")
            return render(request,'register.html',{"form":form,"mess":True}) 
        elif User.objects.filter(username=username).exists():
            # messages.info(request,"Username taken")
            return render(request,'register.html',{"form":form,"message":True}) 
        
        user = User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name)
        profile = Profile(user=user)
        profile.save()
        user.save()
        return redirect('login')
    else:
        form = RegisterForm()
    return render(request,"register.html",{'form':form})


@csrf_exempt
def login_view(request):
    error = ''
    form = AuthenticationForm(request)
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)

            if hobbies.objects.filter(username=user).exists():
                return redirect('/first')
            else :
                return redirect('followtopic')
        else:
            print("no user found")
            return render(request,'login.html',{"form":form,"message":True}) 

            
    return render(request,'login.html',{"form":form}) 


def logout_view(request):
    logout(request)
    return redirect('/')

@csrf_exempt 
@login_required(login_url='login/')
def followtopic(request):
    if request.method == 'POST':
        ft = request.POST.get('selectedItems').split(',')
        # print(ft)
        # print(request.user)
        # username = request.user.username
        # print(username)
        # for i in ft:
        #     print(i)
        print(ft)
        if ft[0] != "":
            for i in ft:
                h = hobbies()
                h.username=request.user
                h.hobby=i
                print(h.username,h.hobby)
                h.save()
                
                print("data entered")
        return redirect('/first')
    
    hobbi = ["Reading", "Writing","Football", "Painting", "Photography", "Cooking", "Baking", "Gardening", "Playing a musical instrument", "Singing", "Dancing", "Yoga", "Meditation", "Hiking", "Camping", "Running", "Cycling", "Swimming", "Surfing", "Skateboarding", "Snowboarding", "Skiing", "Fitness training", "Weightlifting", "Pilates", "Boxing", "Martial arts", "Soccer", "Basketball", "Tennis", "Golf", "Cricket", "Baseball", "Volleyball", "Table tennis", "Badminton", "Chess", "Puzzles", "Board games", "Video games", "Watching movies", "Binge-watching TV series", "Traveling", "Playing Guitar","Exploring new cuisines", "Wine tasting", "Beer brewing", "Collecting stamps", "Collecting coins", "Collecting vintage items", "Antiquing", "Scrapbooking", "Calligraphy", "Knitting", "Crocheting", "Sewing", "Quilting",  "Beat Boxing","Woodworking", "Metalworking", "Pottery", "Origami", "Model building", "Model trains", "Fishing", "Birdwatching", "Star gazing", "Astrology", "Coin collecting", "Genealogy", "Blogging", "Podcasting", "Rock climbing", "Skydiving", "Scuba diving", "Sailing", "Paragliding", "Motorcycling", "Cycling", "Horseback riding", "Horse racing", "Waterskiing", "Wakeboarding", "Snowmobiling", "Ice skating", "Ice hockey", "Cooking", "Baking", "Wine tasting", "Cocktail mixing", "Coffee brewing", "Tea tasting", "Chocolate making", "Beer brewing", "Gardening", "Indoor plants", "Bonsai gardening", "Cactus gardening", "Herb gardening", "Vegetable gardening", "Fruit gardening", "Rose gardening", "Orchid cultivation", "Hiking", "Camping", "Mountain biking", "Nature photography", "Wildlife watching", "Birdwatching", "Geocaching", "Stargazing", "Meteorology", "Volunteering", "Charity work", "Community service", "Writing", "Journaling", "Poetry", "Short story writing", "Novel writing", "Screenwriting", "Journalism", "Comic book writing", "Drawing", "Painting", "Sculpting", "Digital art", "Calligraphy", "Graphic design", "Fashion design", "Jewelry making", "Pottery", "Astrophotography", "Urban exploration", "Ghost hunting", "Cosplay", "Metal detecting", "Beekeeping", "Foraging", "Mushroom hunting", "Candle making", "Soap making", "Candlestick making", "Perfume making", "Astrology", "Tarot reading", "Magic tricks", "Feng shui", "Cryptography", "Escape rooms", "Archery", "Fencing", "Parkour", "Circus arts", "Fire dancing", "Bodybuilding", "Powerlifting", "Triathlon", "Belly dancing", "Capoeira", "Salsa dancing", "Bollywood dancing", "Ice sculpting", "Sand sculpting", "Beekeeping", "Bread making", "Home brewing", "Furniture restoration", "Upcycling", "Soap carving", "Papercraft", "Candle carving", "Glassblowing", "Engraving", "Taxidermy", "Bonsai tree cultivation", "Aquascaping", "Falconry", "Kiteboarding", "Wake surfing", "Parasailing", "Hot air ballooning", "Ziplining", "Hang gliding", "Unicycling", "Roller derby", "Robotics", "Astronomy", "Archaeology", "Paleontology", "Meteorology", "Philately", "Numismatics", "Dowsing", "Quilling", "Puppetry", "Silversmithing", "Leatherworking", "Basket weaving", "Blacksmithing", "Braiding", "Glass etching", "Macrame", "Metal engraving", "Spoon carving", "Wine making", "Cheese making", "Jewelry design", "Perfume blending", "Embroidery", "Patchwork", "Tapestry weaving", "Candle making", "Quilling", "Origami", "Basket weaving", "Leathercraft", "Furniture making", "Kite making", "Model rocketry", "Silversmithing", "Cartooning", "Comic book collecting", "Film photography", "Scrap metal art", "Circus arts", "Stand-up comedy", "Storytelling", "Podcasting", "Mobile app development", "Robotics", "Virtual reality gaming", "Archery tag", "Geocaching", "Extreme ironing", "Competitive eating", "Quidditch", "Chessboxing", "Cheese rolling", "Extreme knitting", "Underwater hockey", "Sepak takraw"]
    return render(request,"followtopics.html",{"hobbies":hobbi})

# def o(request):
#     return render(request,'o.html')


# def a(request):
#     return render(request,'a.html')



# simple frst with only hobbies post and stuff no fucks soo 


# def first(request):
#     # Get hobbies based posts
#     ph = hobbies.objects.filter(username=request.user).values_list("hobby", flat=True).distinct()
#     posts = post.objects.filter(tags__in=ph)

#     # # Get users that the current follower is following
#     # following_users = followc.objects.filter(follower=request.user).values_list('user', flat=True)

#     # # Get posts from the users that the current follower is following
#     # follower_based_posts = post.objects.filter(username__in=following_users)

#     # # Extend the two querysets and sort them by date_posted in descending order
#     # all_posts = posts.union(follower_based_posts).order_by('-date_posted')

#     return render(request, 'first.html', {"posts": posts, "request": request})



@csrf_exempt
@login_required(login_url='login/')
def first(request):
    # Get hobbies based posts
    user_hobbies = hobbies.objects.filter(username=request.user).values_list("hobby", flat=True)
    hobbies_posts = post.objects.filter(tags__in=user_hobbies)

    # Get posts from the users that the current user is following
    following_users = follower.objects.filter(followed_by=request.user).values_list('following', flat=True)
    follower_based_posts = post.objects.filter(username__in=following_users)

    # Combine both querysets and sort them by date_posted in descending order
    all_posts = hobbies_posts.union(follower_based_posts).order_by('-date_posted')

    # Fetch profile image URLs for each user


    profile_image_urls = {}

    # for p in all_posts:
    #     profile_image_urls[p.username] = Profile.objects.get(user=p.username).image.url

    # for u,p in profile_image_urls.items():
    #     print(u,p)  
    print("****************************************************************")

    context = {
        'posts': all_posts,
        'profile_image_urls': profile_image_urls,
    }
    
    return render(request, 'first.html', context)



# def first(request):
#     # print("came in first")
#     posts = post.objects.all().filter().order_by('-date_posted')
#     # print(posts.values())
    
#     ph = hobbies.objects.filter(username=request.user).values_list("hobby", flat=True).distinct()
#     # print(ph)

#     if ph :
#         posts = posts.filter(tags__in=ph)
#         # print(posts.values())
        

#     return render(request,'first.html',{"posts":posts,"request":request})
@csrf_exempt
@login_required(login_url='login/')
def explore(request):
    posts = post.objects.all().filter().order_by('-date_posted')
    # print(posts.values())
    return render(request,'explore.html',{"posts":posts,"request":request})



@csrf_exempt
@login_required(login_url='login/')
def profile_view(request,username):
    # user = get_object_or_404(User, username=username)
    # print(user)       
    # print("in profile view")
    ph = hobbies.objects.filter(username=request.user).values_list("hobby", flat=True).distinct()
    # print(ph)
    # print(type(ph))
    hobb = []
    k=0
    x=[]
    # print(len(ph))
    for i in ph:
        # print(i['hobby'])
        x.append(i)
        k+=1
        if k%5==0 :
            hobb.append(x)
            # print(x)
            # print(hobb)
            x=[]
    if len(x)>0:
        hobb.append(x)
    # print(hobb) 
    return render(request,'profile.html',{"hobbies":hobb,})


@csrf_exempt
@login_required(login_url='login/')
def search(request,username):
    print("in search view")
    
    user = get_object_or_404(User, username=username)
    user = get_object_or_404(User, username=username)

    print(user)
    ph = hobbies.objects.filter(username=user).values_list("hobby", flat=True).distinct()
    # print(ph)
    # print(type(ph))
    hobb = []
    k=0
    x=[]
    # print(len(ph))
    for i in ph:
        # print(i['hobby'])
        x.append(i)
        k+=1
        if k%5==0 :
            hobb.append(x)
            # print(x)
            # print(hobb)
            x=[]
    if len(x)>0:
        hobb.append(x)
    # print(hobb) 
       

    # is_following = followc.objects.filter(follower=request.user, user=user).exists()
    # is_following = followc.objects.filter(follower=request.user, user=user).exists()
    # is_following = user.followed_by.filter(followed_by=request.user).exists()
    is_following = follower.objects.filter(followed_by=request.user, following=user).exists()

    print(is_following)

    # return render(request, 'search.html', {"hobbies": hobb, "user": user,})
    return render(request, 'search.html', {"hobbies": hobb, "user": user, "is_following": is_following})




# def search_view(request):
#     username = request.GET.get('username')
#     users = User.objects.filter(username__icontains=username)
#     return render(request, 'search.html', {'users': users})




from django.core.files.storage import FileSystemStorage

@csrf_exempt
@login_required(login_url='login/')
def savepost(request):
    if request.method == "POST":
        username = request.user
        data = request.POST.get("post_content")
        tags = request.POST.get('selected_hobbies')
        date_posted = datetime.now()
        post_image = request.FILES.get('post_image')  # Get the uploaded image

        # Handle the image, for example, save it to your media directory
        if post_image:
            fs = FileSystemStorage()
            image_filename = fs.save(post_image.name, post_image)

        # Create the post and save it in the database
            savep = post(username=request.user, data=data, date_posted=date_posted, tags=tags, pic=image_filename)
            savep.save()

        else:
            savep = post(username=request.user, data=data, date_posted=date_posted, tags=tags)
            savep.save()

        return redirect('/first')

    ph = hobbies.objects.filter(username=request.user).values_list("hobby", flat=True).distinct()
    return render(request, 'post.html', {"hobbies": ph})


# @login_required(login_url='login/')
# def follow(request):
#     if request.method == "POST":
#         value = request.POST.get('value')
#         profile_username = request.POST.get('user')  # Renamed to profile_username
#         follower = request.user  # Use request.user to get the follower User instance

#         if value == "follow":
#             user_instance = get_object_or_404(User, username=profile_username)  # Renamed to profile_username
#             follows = followc.objects.create(follower=follower, user=user_instance)
#             follows.save()
#         elif value == "unfollow":
#             followc.objects.filter(follower=follower, user__username=profile_username).delete()  # Renamed to profile_username

#         referer = request.META.get('HTTP_REFERER', None)
#         if referer:
#             return redirect(referer)

#     return redirect('search')


# def follow(request):
#     if request.method == "POST":
#         value = request.POST.get('value')
#         user = request.POST.get('user')
#         follower_username = request.POST.get('follower')  # Follower's username

#         if value == "follow":
#             user_instance = get_object_or_404(User, username=user)
#             follower_instance = get_object_or_404(User, username=follower_username)
#             follows = followc.objects.create(username=follower_instance, following=user_instance)
#             follows.save()

#         referer = request.META.get('HTTP_REFERER', None)
#         if referer:
#             return redirect(referer)

#     return redirect('search')


@csrf_exempt
@login_required(login_url='login/')
def follow_user(request, username):
    user_to_follow = User.objects.get(username=username)
    follower_obj, created = follower.objects.get_or_create(followed_by=request.user, following=user_to_follow)
    # return redirect('profile', username=username)
    Notification.objects.create(user=user_to_follow, message=f"{request.user.username} has started following you")

    referer = request.META.get('HTTP_REFERER', None)
    if referer:
        return redirect(referer)

@csrf_exempt
@login_required(login_url='login/')
def unfollow_user(request, username):
    user_to_unfollow = User.objects.get(username=username)
    follower_obj = follower.objects.filter(followed_by=request.user, following=user_to_unfollow)
    follower_obj.delete()
    # return redirect('profile', username=username)
    referer = request.META.get('HTTP_REFERER', None)
    if referer:
        return redirect(referer)
    


@csrf_exempt
@login_required(login_url='login/')
def notifications(request):
# Get the current user
    current_user = request.user
    if not current_user.is_authenticated:
        print("user is authenticated ")
        return render(request, 'error.html', {'error_message': 'User not authenticated'})
    # Get the usernames of all users following the current user
    followers = follower.objects.filter(user=current_user).values_list('follower__username', flat=True)
    print(followers)
    return render(request, 'notifications.html', {'current_user': current_user, 'followers': followers})



def notifications(request):
    # Retrieve notifications for the current user
    user_notifications = Notification.objects.filter(user=request.user).order_by('-timestamp')

    return render(request, 'notifications.html', {"notifications": user_notifications})





@login_required
def editprofile(request):
    profile = request.user.profile

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect(f'/profile/{request.user.username}/')  # Redirect to the profile page
    else:
        form = EditProfileForm(instance=profile)

    return render(request, 'editprofile.html', {'form': form})


def message(request):
    return render(request,"message.html")



@login_required
def delete_post(request, post_id):
    # print(post_id)
    p = get_object_or_404(post, id=post_id)
    # print(p)
    # print(p.username,request.user)
    if request.user.is_superuser or p.username == request.user:
        p.delete()
        previous_page = request.META.get('HTTP_REFERER', '/')
        return redirect(previous_page)    
    else:
        # Handle permission denied, e.g., display an error message
        return render(request, 'error.html', {'message': 'Permission Denied'})
    
