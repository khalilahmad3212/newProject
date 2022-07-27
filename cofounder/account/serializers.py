from rest_framework import serializers

from account.models import UserAccount


class AccountViewSerialier(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = '__all__'
        lookup_field = 'email'


class AccountSerialier(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id', 'email', 'first_name', 'last_name', 'role']
        lookup_field = 'email'