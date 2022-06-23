from django.shortcuts import render

from book_rental_app.models import LargeCategory, SmallCategory, Books

def select_large_category(request):
    large_categories = LargeCategory.objects.all()
    context = {
        'large_categories': large_categories,
    }
    return render(request, 'lender/add_book/select_large_category.html', context)

def select_small_category(request, large_pk):
    large_category = LargeCategory.objects.get(id=large_pk)
    small_categories = SmallCategory.objects.all()
    context = {
        'large_category': large_category,
        'small_categories': small_categories, 
    }
    return render(request, 'lender/add_book/select_small_category.html', context)

def add_book(request, large_pk, small_pk):
    large_category = LargeCategory.objects.get(id=large_pk)
    small_category = SmallCategory.objects.get(id=small_pk)
    context = {
        'large_category': large_category,
        'small_category': small_category,
    }
    return render(request, 'lender/add_book/add_book.html', context)


def add_book_confirm(request, pk):
    if request.method == 'POST':
        small_category = SmallCategory.objects.get(id=pk)
        manage_id = request.POST.get('manage_id')
        id_in_category = request.POST.get('id_in_category')
        title = request.POST.get('title')
        Books.objects.create(manage_id=manage_id, id_in_category=id_in_category, title=title
                            ,category=small_category)
    return render(request, 'lender/add_book/add_book_confirm.html')

def list_books(request):
    books = Books.objects.all()
    context = {
        'books': books,
    }
    return render(request, 'lender/list_books/list_books.html', context)