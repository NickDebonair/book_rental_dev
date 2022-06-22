from django.urls import path
from . import views
app_name = 'book_rental_app'

urlpatterns = [
    # LOGIN_REDIRECT_URL
    path('index/', views.index, name='index'),
    # 管理者
    path('index_lender/', views.index_lender, name='index_lender'),

    # 利用者
    path('index_borrower/', views.index_borrower, name='index_borrower'),
]