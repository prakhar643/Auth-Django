from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth.decorators import login_required

# Create your views here.

class SignupView(View):
    def get(self, request):
        # Handles GET requests
        return render(request, "signup.html")

    def post(self, request):
        # Handles POST requests
        name = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if User.objects.filter(email=email).exists():
            return HttpResponse("Email already registered") 
        
        if password != confirm_password:
            return HttpResponse("Passwords do not match")
        
        user = User.objects.create_user(username=email, email=email, password=password,first_name=name)
        user.save()
        return HttpResponse("User registered successfully")

# def signup(request):
#     if request.method == "POST":
#         user = request.POST.get("username")
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#         confirm_pass = request.POST.get("confirm_password")

#         user = User.objects.filter(email=email).first()
#         if user:
#             return HttpResponse("Email already registered")

#         if password != confirm_pass:
#             return HttpResponse("Password is not same")
#         else:
#             myUser = User.objects.create_user(user,email,password)
#             myUser.save()
#     return render(request,"signup.html")

def logout(request):
    request.session.flush()
    return redirect("login")

@login_required
def home(request):
    return render(request,"home.html")