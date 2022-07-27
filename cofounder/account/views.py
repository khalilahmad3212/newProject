from django.contrib.auth import get_user_model

User = get_user_model()
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from rest_framework.generics import (
    RetrieveAPIView,
    ListAPIView,
    DestroyAPIView
)

from .serializers import AccountViewSerialier, AccountSerialier
from .models import UserAccount


# additional
from rest_framework import permissions



class SignupView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data

        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']
        role = data['role']
        password = data['password']
        password2 = data['password2']

# {
#     "email": "sooraj@gmail.com",
#     "first_name": "Khalil",
#     "last_name": "Ahmad",
#     "role": "inverstor",
#     "password": "sooraj123",
#     "password2": "sooraj123"
# }

        if password == password2:
            if User.objects.filter(email=email).exists():
                return Response({'error': 'Email already exists'})
            else:
                if len(password) < 6:
                    return Response(
                        {'error': 'Password must be at least 6 characters'})
                else:
                    user = User.objects.create_user(email=email,
                                                    password=password,
                                                    first_name=first_name,
                                                    last_name=last_name,
                                                    role=role
                                                    )

                    user.save()
                    serializer = AccountSerialier(user)
                    # return Response({
                    #     'success': 'User created successfully', 
                    #     "user": serializer.data
                    #     })
                    return Response(serializer.data)
        else:
            return Response({'error': 'Passwords do not match'})


class AccountDestroyView(DestroyAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = AccountSerialier
    lookup_field = 'email'


class ListView(ListAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = AccountSerialier
    lookup_field = 'email'