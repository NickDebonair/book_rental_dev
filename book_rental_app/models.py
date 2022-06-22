from django.db import models
from register.models import User
# Create your models here.

class LargeCategory(models.Model):
    name = models.CharField(max_length=25, verbose_name='Large Categroy name')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Large_Category'
        verbose_name = '大カテゴリー'
        verbose_name_plural = '大カテゴリー'


class SmallCategory(models.Model):
    large_category = models.ForeignKey(LargeCategory, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Large Categroy name')
    name = models.CharField(max_length=25, verbose_name='Small Categroy name')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Small_Category'
        verbose_name = '小カテゴリー'
        verbose_name_plural = '小カテゴリー'


class Books(models.Model):
    manage_id = models.IntegerField(verbose_name='書籍管理用ID', blank=True, null=True)
    id_in_category = models.IntegerField(verbose_name='カテゴリーにおけるID', blank=True, null=True)
    title = models.CharField(max_length=255, verbose_name='Book Title')
    category = models.ForeignKey(SmallCategory, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Small Categroy name')
    borrower_user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='book_borrower', verbose_name='本を借りた人')
    lender_user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='book_lender', verbose_name='貸出許可を出した人')
    is_rental = models.BooleanField(default=False, help_text='借りられたらTrue')

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'Books'
        verbose_name = '書籍情報'
        verbose_name_plural = '書籍情報'


class LendingStatus(models.Model):
    checkout_date = models.DateTimeField(auto_now_add=True, verbose_name='貸し出し日')
    due_date = models.DateField(verbose_name='返却予定日')
    return_date = models.DateTimeField(auto_now=True, verbose_name='返却日')
    book = models.ForeignKey(Books, on_delete=models.PROTECT, verbose_name='貸し出された書籍')
    borrower_user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='status_borrower', verbose_name='本を借りた人')
    lender_user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='status_lender', verbose_name='貸出許可を出した人')
    is_returned = models.BooleanField(default=False)

    def __str__(self):
        return self.checkout_date + ' / ' + self.book.title + ' / ' + self.borrower_user.last_name + self.borrower_user.first_name 
    
    class Meta:
        db_table = 'LendingStatus'
        verbose_name = '貸出状況'
        verbose_name_plural = '貸出状況'
