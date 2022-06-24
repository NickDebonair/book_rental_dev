from django.urls import path
from . import views
app_name = 'book_rental_app'

urlpatterns = [
    # LOGIN_REDIRECT_URL
    path('index/', views.index, name='index'),

    # 管理者
    path('index_lender/', views.index_lender, name='index_lender'),
    path('list_large_category/', views.list_large_category, name='list_large_category'),
    path('create_large_category/', views.create_large_category, name='create_large_category'),
    path('list_small_category/<int:pk>/', views.list_small_category, name='list_small_category'),
    path('create_small_category/<int:pk>/', views.create_small_category, name='create_small_category'),

    path('select_large_category/', views.select_large_category, name='select_large_category'),
    path('select_small_category/<int:large_pk>/', views.select_small_category, name='select_small_category'),
    path('add_book/<int:large_pk>/<int:small_pk>/', views.add_book, name='add_book'),
    path('add_book_confirm/<int:pk>/', views.add_book_confirm, name='add_book_confirm'),

    path('list_books', views.list_books, name='list_books'),

    path('index_status/', views.index_status, name='index_status'),
    path('list_status/', views.list_status, name='list_status'),
    path('list_status_user/', views.list_status_user, name='list_status_user'),
    path('detail_status_user/<int:pk>/', views.detail_status_user, name='detail_status_user'),
    path('history_status_user/<int:pk>/', views.history_status_user, name='history_status_user'),

    # 利用者
    path('index_borrower/', views.index_borrower, name='index_borrower'),

    path('list_borrowing/', views.list_borrowing, name='list_borrowing'),
    path('permission_borrowing/', views.permission_borrowing, name='permission_borrowing'),
    path('confirm_borrowing/', views.confirm_borrowing, name='confirm_borrowing'),

    path('list_borrowed/', views.list_borrowed, name='list_borrowed'),
    path('list_returning/', views.list_returning, name='list_returning'),
    path('confirm_returning/', views.confirm_returning, name='confirm_returning'),

    path('rental_history/', views.rental_history, name='rental_history'),

]