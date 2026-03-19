from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

# Create your views here.
def signup(request):
    if request.method == "POST":
        user = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_pass = request.POST.get("confirm_password")
        if password != confirm_pass:
            return HttpResponse("Password is not same")
        else:
            myUser = User.objects.create_user(user,email,password)
            myUser.save()
    return render(request,"signup.html")

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.filter(email=email).first()

        if user is None:
            return render(request, 'login.html', {"error": "Email not registered"})
        
        if not check_password(password, user.password):
            return render(request, 'login.html', {"error": "Invalid Password"})

        
        return render(request, "home.html", {"user": user})

    return render(request, "login.html")

def logout(request):
    request.session.flush()
    return redirect("login")

def home(request):
    return render(request,"home.html")