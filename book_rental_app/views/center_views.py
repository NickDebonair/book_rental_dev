from django.shortcuts import render
from django.shortcuts import redirect

from book_rental_app.models import LargeCategory, SmallCategory
# Create your views here.

def index(request):
    if not request.user.is_superuser:
        return redirect('book_rental_app:index_borrower')
    else:
        return redirect('book_rental_app:index_lender')

def list_large_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name == '':
            return redirect('book_rental_app:create_large_category')
        else:
            LargeCategory.objects.create(name=name)
        
    large_categories = LargeCategory.objects.all()
    print(large_categories)
    context = {
        'large_categories': large_categories,
    }
    return render(request, 'lender/category/list_large_category.html', context)

def create_large_category(request):
    return render(request, 'lender/category/create_large_category.html')

def list_small_category(request, pk):
    if request.method == 'POST':
        name = request.POST.get('name')
        large_category = LargeCategory.objects.get(id=pk)
        SmallCategory.objects.create(large_category=large_category, name=name)

    large_category = LargeCategory.objects.get(id=pk)
    small_categories = SmallCategory.objects.filter(large_category__id=pk)
    context = {
        'small_categories': small_categories,
        'large_category': large_category,
    }
    return render(request, 'lender/category/list_small_category.html', context)

def create_small_category(request, pk):
    large_category = LargeCategory.objects.get(id=pk)
    context = {
        'large_category': large_category,
    }
    return render(request, 'lender/category/create_small_category.html', context)
