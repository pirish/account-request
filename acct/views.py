# Framework imports
from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework import permissions

# local imports
from .models import AccountType, AccountRequest
from .serializers import AccountRequestSerializer, AccountTypeSerializer
from .forms import AccountRequestForm


class AccountTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows requests to be viewed or submitted
    """
    queryset = AccountType.objects.all()
    serializer_class = AccountTypeSerializer
    permission_classes = [permissions.IsAuthenticated]


class AccountRequestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows requests to be viewed or submitted
    """
    queryset = AccountRequest.objects.all()
    serializer_class = AccountRequestSerializer
    permission_classes = [permissions.IsAuthenticated]


def index(request):
    account_type_list = AccountType.objects.all()
    print(account_type_list)
    context = {
        'account_type_list': account_type_list
    }
    return render(request, 'acct/index.html', context)


def request_account(request):
    if request.method == 'POST':
        form = AccountRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AccountRequestForm
    return render(request, 'acct/request.html', {'form': form})
