from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.

def index(request):
    if not request.user.is_superuser:
        return redirect('book_rental_app:index_borrower')
    else:
        return redirect('book_rental_app:index_lender')