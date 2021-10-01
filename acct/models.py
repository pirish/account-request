from django.db import models
from django.forms import ModelForm


class AccountType(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=200)
    field_1 = models.CharField(max_length=200, blank=True)
    field_2 = models.CharField(max_length=200, blank=True)
    field_3 = models.CharField(max_length=200, blank=True)
    field_4 = models.CharField(max_length=200, blank=True)
    field_5 = models.CharField(max_length=200, blank=True)


class AccountRequest(models.Model):
    def __str__(self):
        return self.customer_user
    account_type = models.ForeignKey(AccountType, on_delete=models.CASCADE)
    acct_id = models.AutoField(primary_key=True, blank=True)
    request_by = models.CharField(max_length=200)
    request_email = models.CharField(max_length=200)
    date_required = models.DateField('Date required', blank=True)
    customer_name = models.CharField(max_length=200)
    customer_org = models.CharField(max_length=200)
    customer_phone = models.CharField(max_length=200)
    customer_email = models.CharField(max_length=200)
    customer_user = models.CharField(max_length=200)
    customer_pass = models.CharField(max_length=200)
    field_1 = models.CharField(max_length=200, blank=True)
    field_2 = models.CharField(max_length=200, blank=True)
    field_3 = models.CharField(max_length=200, blank=True)
    field_4 = models.CharField(max_length=200, blank=True)
    field_5 = models.CharField(max_length=200, blank=True)
    status = models.IntegerField(default=0, blank=True)


class AccountRequestForm(ModelForm):
    class Meta:
        model = AccountRequest
        fields = [
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
            ]
