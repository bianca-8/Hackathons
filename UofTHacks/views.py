import json
from django.shortcuts import render, redirect, get_object_or_404
from .models import Memento, UserProfile, User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail



@login_required
def index(request):
    mementos = Memento.objects.filter(user=request.user)
    return render(request, 'index.html', { "mementos": mementos })

@login_required
def memento(request, id):
    memento = get_object_or_404(Memento, id=id, user=request.user)

    context = {
        'memento': memento,
    }

    return render(request, 'mementos.html', context)

@login_required
def addMemento(request):
    if request.method == 'POST':
        # Retrieve form data from POST request
        title = request.POST['title']
        text = request.POST['text']
        img1 = request.FILES.get('img1')
        img2 = request.FILES.get('img2')
        img3 = request.FILES.get('img3')
        audio = request.FILES.get('audio')

        user = request.user

        memento = Memento.objects.create(
            title=title,
            text=text,
            img1=img1,
            img2=img2,
            img3=img3,
            audio=audio,
            user=user
        )
        memento.save()
        messages.success(request, 'Yayy!! You Added Your Memento!')
        return redirect('index')  
    else:
        return render(request, 'add-memento.html')
    
@login_required
def profile(request):
    user = request.user

    try:
        user_profile = UserProfile.objects.get(user=user)
    except UserProfile.DoesNotExist:
        user_profile = None

    total_mementos = Memento.objects.filter(user=user).count()

    return render(request, 'profile.html', {'total_mementos': total_mementos, 'user_profile': user_profile})


def signin(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            else:
                # Redirect to a default URL if 'next' is not present
                return redirect('index')
        else:
            # Authentication failed, display an error message
            messages.error(request, 'Invalid credentials. Please try again.')
            return redirect('login')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        profile_pic = request.FILES['profile_pic']

        user = User.objects.create_user(username=username, email=email, password=password)

        profile = UserProfile(user=user, profile_pic=profile_pic)
        profile.save()

        user = authenticate(username=username, password=password)
        login(request, user)

        return redirect('index')  

    return render(request, 'register.html')

@login_required
def delete_memento(request, id):
    memento = get_object_or_404(Memento, id=id, user=request.user)

    recipient_email = memento.user.email

    memento.delete()

    subject = 'Memento Deleted!!'
    message = 'Your memento has been deleted. Please contact the customer support if you did not delete it.'
    from_email = 'nicebanjaraa@gmail.com' 
    recipient_list = [recipient_email]

    send_mail(subject, message, from_email, recipient_list)

    messages.success(request, 'Memento deleted successfully.')
    return redirect('index')

@login_required
def edit_memento(request, memento_id):
    memento = get_object_or_404(Memento, id=memento_id)

    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        img1 = request.FILES.get('img1', memento.img1)  # Use existing image if not changed
        img2 = request.FILES.get('img2', memento.img2)  # Use existing image if not changed
        img3 = request.FILES.get('img3', memento.img3)  # Use existing image if not changed
        audio = request.FILES.get('audio', memento.audio)  # Use existing audio if not changed

        memento.title = title
        memento.text = text
        memento.img1 = img1
        memento.img2 = img2
        memento.img3 = img3
        memento.audio = audio
        memento.save()
        messages.success(request, 'Yayy!! You Edited Your Memento!')

        # Redirect to the index page after editing
        return redirect('index')
    else:
        return render(request, 'edit-mementos.html', {'memento': memento})

    

@login_required()
def signout(request): 
    logout(request)
    return redirect('login')