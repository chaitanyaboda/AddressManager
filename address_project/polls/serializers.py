from django.contrib.auth.models import User, Group
from polls.models import Company, StateJapan
from rest_framework import serializers


class CompanySerializer(serializers.ModelSerializer):
    state = serializers.PrimaryKeyRelatedField(queryset=StateJapan.objects.all())

    # returns the model company for get single or list

    class Meta:
        model = Company
        fields = ('company_name', 'building_number', 'postal_code', 'locality', 'city', 'state')


class PinCodeSerializer(serializers.ModelSerializer):
    # returns only the postal code from the Company model

    class Meta:
        model = Company
        fields = ['postal_code']
