from django.shortcuts import render
from .models import advisordetail, usermodel, bookingdetail
from .serailizers import adminserializer, userserializer, userloginserializer, bookingdetailserializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import jwt

# Create your views here.


# django default password for database is admin;admin

# advisor adding view
@api_view(['POST'])
def advisor_add_view(request):
    # example input for this view
    # {
    #     "name":"Nishtha",
    #     "imageurl":"image.image.com"
    # }
    if request.method == "POST":
        saveserialize = adminserializer(data=request.data)
        if saveserialize.is_valid():
            saveserialize.save()
            return Response(saveserialize.data, status=status.HTTP_200_OK)
        return Response(saveserialize.data, status=status.HTTP_400_BAD_REQUEST)

# new user register view
@api_view(['POST'])
def userview(request):
    # example request for this view
    # {
    #     "name":"Xyz",
    #     "email":"email@email.com",
    #     "password":"abcd"
    # }
    if request.method == "POST":
        saveserialize = userserializer(data=request.data)
        if saveserialize.is_valid():
            saveserialize.save()
            email = saveserialize.data['email']
            password = saveserialize.data['password']
            name = saveserialize.data['name']
            jwt_token = jwt.encode({'email': request.POST.get(
                'email'), 'password': request.POST.get('password')}, 'MySecretKey', algorithm='HS256')
            response = {
                'JWT authentication token': jwt_token,
                'user id': usermodel.objects.filter(name=name, email=email, password=password).values('id')
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response(saveserialize.data, status=status.HTTP_400_BAD_REQUEST)

# Logins a user
@api_view(['POST'])
def userloginview(request):
    # example request for this view
    # {
    #     "email":"email@email.com",
    #     "password":"abcd"
    # }
    if request.method == "POST":
        saveserialize = userloginserializer(data=request.data)
        if saveserialize.is_valid():
            email = saveserialize.data['email']
            password = saveserialize.data['password']
            result = usermodel.objects.filter(
                email=email, password=password).exists()  # return True/False
            jwt_token = jwt.encode({'email': request.POST.get(
                'email'), 'password': request.POST.get('password')}, 'MySecretKey', algorithm='HS256')
            if result == True:
                response = {
                    'JWT authentication token': jwt_token,
                    'user id': usermodel.objects.filter(email=email, password=password).values('id')
                }
                return Response(response, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

# lists all the advisors
@api_view(['GET'])
def advisorlistview(request, userid):
    if usermodel.objects.filter(id=userid).exists() == True:
        entries = advisordetail.objects.all().values()
        return Response(entries, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_401_UNAUTHORIZED)

# book a call for a specific user with advsior
@api_view(['POST'])
def bookcall(request, userid, advisorid):
    # example request for this view
    # {
    #     "booking_time":"date-time string"
    # }
    if request.method == "POST":
        data = request.data
        user = usermodel.objects.get(id=userid)
        advisor = advisordetail.objects.get(id=advisorid)
        booking_date = data["booking_time"]
        booking = bookingdetail.objects.create(
            advisor_id=advisor,
            booking_time=booking_date,
            user_id=user
        )
        booking.save()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


# Get specific user booking details with userid
@api_view(['GET'])
def booked(request, userid):
    user = usermodel.objects.get(id=userid)
    bookings = user.bookingdetail_set.all()
    serializer = bookingdetailserializer(bookings, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
