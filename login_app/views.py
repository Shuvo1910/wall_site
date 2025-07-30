from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import User_info
from .models import Wallpaper
from .forms import WallpaperUploadForm
from django.contrib import messages
from .models import UserSignUp


def homepage(request):
    return render(request,'login_app/index.html',{})

@login_required(login_url='login_auth')
def desktop_page(request):
    return render(request, 'login_app/desktop.html')

@login_required(login_url='login_auth')
def mobile_page(request):
    return render(request, 'login_app/mobile.html')

@login_required(login_url='login_auth')
def index_2(request):
    if 'user_id' in request.session:
        return render(request, 'login_app/index_2.html')
    else:
        return redirect('login')

def raw_data(request):
    data = User_info.objects.all()
    pairs = [f"{item.email} {item.password}" for item in data]
    result = "[" + ", ".join(pairs) + "]"
    return HttpResponse(result, content_type='text/plain')

def login(request):
    return render(request, 'login_app/login.html', {})
        
def signup(request):
    if request.method == "POST":
        uemail = request.POST.get("email")
        upassword = request.POST.get("password")

        if UserSignUp.objects.filter(email=uemail).exists():
            messages.error(request, "Email already registered.")
            return redirect('signup')

        new_user = UserSignUp(email=uemail, password=upassword)
        new_user.save()

        request.session['user_id'] = new_user.id
        messages.success(request, f"Welcome, {uemail}!")
        return redirect('index_2')
    else:
        return render(request, 'login_app/signup.html')
    
    
def login_auth(request):
    if request.method == "POST":
        uemail = request.POST.get("email")
        upassword = request.POST.get("password")

        try:
            user_logged = User_info.objects.get(email=uemail, password=upassword)
            request.session['user_id'] = user_logged.id
            messages.success(request, "Welcome (User_info)!")
            return redirect('index_2')
        except User_info.DoesNotExist:
            pass 
      
        try:
            user_logged = UserSignUp.objects.get(email=uemail, password=upassword)
            request.session['user_id'] = user_logged.id
            messages.success(request, "Welcome (UserSignUp)!")
            return redirect('index_2')
        except UserSignUp.DoesNotExist:
            messages.error(request, "Invalid email or password.")
            return redirect('login')
    else:
        return render(request, 'login_app/login.html')


def media(request):
    wallpapers = Wallpaper.objects.all().order_by('-uploaded_at')
    context = {
        'wallpapers': wallpapers  
    }
    return render(request, 'login_app/desktop.html', context)
          
def upload_wallpaper(request):
    if request.method == 'POST':
        form = WallpaperUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login_app:desktop.html')
    else:
        form = WallpaperUploadForm()
    return render(request, 'login_app/desktop.html', {'form': form})

def wallpaper_list(request):
    wallpapers = Wallpaper.objects.all()
    return render(request, 'login_app/desktop.html', {'wallpapers': wallpapers})


    