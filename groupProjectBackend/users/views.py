from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializers import CustomUserSerializer

from django.db import IntegrityError
from rest_framework.exceptions import ParseError

class CustomUserList(APIView):
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)

        if serializer.is_valid():

            email = serializer.validated_data.get('email')
            try:
                # checking for any pre-existing users with this email. If found, continues to next line and raises Error. If not found, raises CustomUser.DoesNotExist exception, in which case it is ok to save this new user! We put the serializer.save() method inside the exception.
                nonUniqueUser = CustomUser.objects.get(email=email)
                raise ParseError(detail="This email is already signed up")
            except CustomUser.DoesNotExist:
                try:
                    serializer.save()
                    return Response(serializer.data)
                except IntegrityError:
                    # checking this instance of CustomUser doesn't already exist (ie. same username). If username not found in system, save. Else, raise Error
                    raise ParseError(detail="This username already exists")


class CustomUserDetail(APIView):
    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)
