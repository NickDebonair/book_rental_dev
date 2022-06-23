from django.shortcuts import render, redirect
from book_rental_app.forms import LenderForm
from register.models import User
from book_rental_app.models import Books

# Create your views here.

def index_borrower(request):
    return render(request, 'borrower/index.html')


"""
貸出
"""
def list_borrowing(request):
    books = Books.objects.all().order_by('manage_id')
    user = request.user
    print()
    print('borrowing_books:', end='')
    print(user.borrowing_books.all())
    print('len(borrowing_books):', end='')
    print(len(user.borrowing_books.all()))
    total_borrowing = len(user.borrowing_books.all())

    context = {
        'books': books,
        'total_borrowing': total_borrowing,
    }
    return render(request, 'borrower/list_borrowing.html', context)

def permission_borrowing(request):
    if request.method == 'POST':
        #次のページ"confirm_borrowing"に反映させるための構え
        borrowing_books = request.POST.getlist('borrowing_books')
        print()
        print('borrowing_books:', end='')
        print(borrowing_books)
        books = []
        for i in borrowing_books:
            books.append(Books.objects.get(id=i))
        form = LenderForm()
        print('form:', end='')
        print(form)
        try:
            context = {
                'books': books,
                'form': form,
            }
            print('books:', end='')
            print(books)
            return render(request, 'borrower/permission_borrowing.html', context)
        except:
            return redirect('book_rental_app:list_borrowing')

def confirm_borrowing(request):
    if request.method == 'POST':
        # データベース反映の為の下準備と、ページ表示のための処理
        books_ids = request.POST.getlist('books')
        print('books_ids:', end='')
        print(books_ids)


        books = []
        for i in books_ids:
            books.append(Books.objects.get(id=i))
        print('books:', end='')
        print(books)
        
        lender_pk = request.POST.get('lender')
        print('lender_pk:', end='')
        print(lender_pk)
        lender_user = User.objects.get(id=lender_pk)
        print('lender_user:', end='')
        print(lender_user)
       
        # ここからデータベースへの反映処理
        # Booksへの反映

        # LendignStatusへの反映

        # Userのrental_limitの確認




        context = {
            'books': books,
            'lender_user': lender_user
        }
        return render(request, 'borrower/confirm_borrowing.html', context)
    
"""
返却
"""
def list_borrowed(request):
    user = request.user
    borrowed_books = user.borrowed_books.all()


    return render(request, 'borrower/list_borrowed.html')
