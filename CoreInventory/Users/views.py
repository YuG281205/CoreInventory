from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignupSerializer,LoginSerializer
from django.shortcuts import render,redirect
from .models import User
from django.core.mail import send_mail
from django.contrib.auth.hashers import check_password
import random

class SignupView(APIView):

    def post(self, request):

        serializer = SignupSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            otp = random.randint(100000,999999)
            user.otp = otp
            user.save()

            send_mail(
                "Email Verification OTP",
                f"Your OTP is {otp}",
                "noreply@coreinventory.com",
                [user.email],
                fail_silently=False,
            )

            return Response({
                "message":"User created. Verify email with OTP"
            })

        return Response(serializer.errors,status=400)
class VerifyOTP(APIView):
    def post(self, request):

        email = request.data.get("email")
        otp = request.data.get("otp")

        user = User.objects.get(email=email)

        if user.otp == int(otp):
            user.is_verified = True
            user.save()

            return Response({"message":"Email verified successfully"})

        return Response({"error":"Invalid OTP"},status=400)

def signup_page(request):
    return render(request, 'signup.html')

class LoginView(APIView):

    def post(self, request):

        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():

            user = serializer.validated_data['user']

            if not user.is_verified:
                return Response(
                    {"error": "Email not verified"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            return Response({
                "message": "Login successful",
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "role": user.role
                }
            })

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
def login_view(request):

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = User.objects.get(email=email)

            if check_password(password, user.password):
                request.session['user_id'] = user.id
                request.session['username'] = user.username
                request.session['role'] = user.role

                return redirect('dashboard.html')

            else:
                return render(request, "login.html", {"error": "Invalid password"})

        except User.DoesNotExist:
            return render(request, "login.html", {"error": "User not found"})

    return render(request, "login.html")

def login_page(request):
    return render(request, 'login.html')



def verify_otp_page(request):
    return render(request, "verify_otp.html")

def dashboard_page(request):
    return render(request,"dashboard.html")