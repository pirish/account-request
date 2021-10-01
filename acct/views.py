# Framework imports
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render, redirect
from rest_framework import viewsets
from rest_framework import permissions


#local imports
from .models import AccountType, AccountRequest, AccountRequestForm
from .serializers import AccountRequestSerializer, AccountTypeSerializer
#from .forms import AccountRequestForm


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
    #template = loader.get_template('acct/index.html')
    context = {
        'account_type_list': account_type_list
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'acct/index.html', context)

def request_account(request, account_type):
    if request.method == 'POST':
        account_type_object = AccountType(name=account_type)
        form = AccountRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AccountRequestForm
    return render(request, 'acct/request.html', {'form': form, 'account_type': account_type})
