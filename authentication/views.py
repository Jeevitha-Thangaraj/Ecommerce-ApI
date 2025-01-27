from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from authentication.serializers import UserSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework import status 
from rest_framework.authtoken.models import Token


@api_view(["POST"])
def signup_user(request):
    serializer = UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({"message": "User Created"})


@api_view(["POST"])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if not username or not password:
        return Response({"error": "Username and password are required."}, status=400)

    user = authenticate(username=username, password=password)

    if not user:
        return Response({"error": "Invalid credentials"}, status=401)
    
    # else:
    #     return Response({"message":"login successfully","data":UserSerializer(user).data},status=status.HTTP_200_OK)

    token ,created= Token.objects.get_or_create(user=user)

    return Response({"message": "Login successful", "key": token.key})
        

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def logout_view(request):
#     logout(request)
#     response = Response({'message': 'Logged out successfully'},status=status.HTTP_200_OK)
#     response.delete_cookie('jwt')
#     return response

@api_view(["POST"])
def get_user(request,id):
    try:
        user=User.objects.get(id=id)
        serializer=UserSerializer(user)
        return Response({"message":"User fectched successfully","data":serializer.data},status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({"message":"User Doesn't Exists"},status=status.HTTP_404_NOT_FOUND)

