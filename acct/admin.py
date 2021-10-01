from django.contrib import admin

# Register your models here.
from .models import AccountType, AccountRequest
admin.site.register(AccountType)
admin.site.register(AccountRequest)
