from django.shortcuts import render, redirect
from book_rental_app.forms import LenderForm
from register.models import User
from book_rental_app.models import Books, LendingStatus

from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
import datetime as dt
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


        books_list = []
        for i in books_ids:
            books_list.append(Books.objects.get(id=i))
        print('books:', end='')
        print(books_list)
        
        lender_pk = request.POST.get('lender')
        print('lender_pk:', end='')
        print(lender_pk)
        lender_user = User.objects.get(id=lender_pk)
        print('lender_user:', end='')
        print(lender_user)
       
        # ここからデータベースへの反映処理
        borrower_user = request.user
        # Booksへの反映
        for book in books_list:
            book.borrower_user = borrower_user
            book.lender_user = lender_user
            book.is_rental = True
            book.save()

        # LendignStatusへの反映
        for book in books_list:
            LendingStatus.objects.create(book=book, borrower_user=borrower_user, lender_user=lender_user)
        # Userのrental_limitの確認
        user_books = Books.objects.filter(borrower_user=borrower_user)
        if len(user_books) == 5:
            borrower_user.rental_limit = True
        borrower_user.is_borrowing = True
        borrower_user.save()


        context = {
            'books': books_list,
            'lender_user': lender_user
        }
        return render(request, 'borrower/confirm_borrowing.html', context)
    
"""
返却
"""
def list_borrowed(request):
    user = request.user
    borrowed_books = user.borrowing_books.all()
    print('borrowed_books:', end='')
    print(borrowed_books)
    lending_status = LendingStatus.objects.filter(borrower_user=user)
    context = {
        'lending_status': lending_status,
    }


    return render(request, 'borrower/list_borrowed.html', context)

def list_returning(request):
    if request.method == 'POST':
        returning_status_id = request.POST.getlist('returning_status_id')
        print()
        print('returning_status_id:', end='')
        print(returning_status_id)
        # returning_books = []
        returning_status_list = []
        for i in returning_status_id:
            lendering_status = LendingStatus.objects.get(id=i)
            returning_status_list.append(lendering_status)
            # returning_book = lendering_status.book
            # returning_book.borrower_user.remove()
            # returning_book.lender_user.remove()
            # returning_book.is_retal = False
            # returning_book.save()
            # print(datetime.today())
            # lendering_status.returned_date = datetime.today()
            # lendering_status.is_returned = True
            # lendering_status.save()

            # returning_books.append(returning_book)
            # print(returning_books)
        print()
        print(returning_status_list)

        context = {
            'returning_status_list': returning_status_list,
        }
        return render(request, 'borrower/list_returning.html', context)

def confirm_returning(request):
    if request.method == 'POST':
        returning_user = request.user
        returning_status_id = request.POST.getlist('returning_status_id')
        print()
        print('returning_status_id:', end='')
        print(returning_status_id)
        returned_status_list = []
        for i in returning_status_id:
            lendering_status = LendingStatus.objects.get(id=i)
            lending_user = lendering_status.lender_user
            returning_book = lendering_status.book
            print('returning_user:', end='')
            print(returning_user)
            print('lending_user:', end='')
            print(lending_user)
            print()
            print(returning_user.borrowing_books.all())
            print(lending_user.lending_books.all())
            returning_user.borrowing_books.remove(returning_book, bulk=False)
            lending_user.lending_books.remove(returning_book, bulk=False)
            print()
            print(returning_user.borrowing_books.all())
            print(lending_user.lending_books.all())
            
            # returning_user.save()
            # lending_user.save()
            # returning_user.borrowing_books.remove(returning_book)
            # lending_user.lending_books.remove(returning_book)
            # returning_book.remove(returning_user, bulk=False)
            # returning_book.remove(lending_user, bulk=False)
            # returning_book.save()
            returning_book.is_rental = False
            returning_book.borrower_user = None
            returning_book.lender_user = None
            returning_book.save()
            print(datetime.today())
            
            lendering_status.is_returned = True
            lendering_status.save()
            returned_status_list.append(lendering_status)
        
        # 1人あたりの貸出上限の5冊を必ず下回るのでフラグ変更
        if returning_user.rental_limit == True:
            returning_user.rental_limit = False
            returning_user.save()
        
        borrowing_books = Books.objects.filter(borrower_user = returning_user)
        if len(borrowing_books) == 0:
            returning_user.is_borrowing = False
            returning_user.save()

        context = {
            'returned_status_list': returned_status_list,
        }
        return render(request, 'borrower/confirm_returning.html', context)

"""
履歴機能
"""
def rental_history(request):
    borrower_user = request.user
    status_history = LendingStatus.objects.filter(is_returned=True, borrower_user=borrower_user).order_by('-checkout_date')
    print(status_history)
    context = {
        'status_history': status_history,
    }
    return render(request, 'borrower/rental_history.html', context)