from django.shortcuts import render

from book_rental_app.models import LendingStatus
from register.models import User

# Create your views here.

def index_lender(request):
    return render(request, 'lender/index.html')

def index_status(request):
    return render(request, 'lender/list_status/index_status.html')

def list_status(request):
    lending_status = LendingStatus.objects.filter(is_returned=False).order_by('checkout_date', 'borrower_user')
    context = {
        'lending_status': lending_status,
    }
    return render(request, 'lender/list_status/list_status.html', context)

def list_status_user(request):
    borrowing_users = User.objects.filter(is_borrowing=True)
    context = {
        'borrowing_users': borrowing_users,
    }
    return render(request, 'lender/list_status/list_status_user.html', context)

def detail_status_user(request, pk):
    status_user = User.objects.get(id=pk)
    lending_status = LendingStatus.objects.filter(borrower_user=status_user, is_returned=False)
    context = {
        'status_user': status_user,
        'lending_status': lending_status,
    }
    return render(request, 'lender/list_status/detail_status_user.html', context)

def history_status_user(request, pk):
    status_user = User.objects.get(id=pk)
    returned_status = LendingStatus.objects.filter(borrower_user=status_user, is_returned=True)
    context = {
        'status_user': status_user,
        'returned_status': returned_status,
    }
    return render(request, 'lender/list_status/history_status_user.html', context)