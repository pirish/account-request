from rest_framework import serializers
from .models import AccountType, AccountRequest


class AccountRequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AccountRequest
        fields = (
            'account_type',
            'request_by',
            'request_email',
            'request_email',
            'request_email',
            'date_required',
            'customer_name',
            'customer_org',
            'customer_phone',
            'customer_email',
            'customer_user',
            'field_1',
            'field_2',
            'field_3',
            'field_4',
            'field_5'
            )


class AccountTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AccountType
        fields = (
            'name',
            'field_1',
            'field_2',
            'field_3',
            'field_4',
            'field_5'
            )
