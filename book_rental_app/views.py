from django.shortcuts import render

# Create your views here.

def index_borrower(request):
    return render(request, 'borrower/index.html')

def index_lender(request):
    return render(request, 'lender/index.html')