from django import forms

from register.models import User
from .models import Books, LargeCategory, SmallCategory

class LargeCategoryForm(forms.ModelForm):
    class Meta:
        model = LargeCategory
        fields = '__all__'
        labels = {
            'name': '',
        }


class SmallCategoryForm(forms.ModelForm):
    class Meta:
        model = SmallCategory
        fields = '__all__'
        labels = {
            'large_category': '',
            'name': '',
        }


class BooksForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'
        labels = {
            'manage_id': '',
            'id_in_category': '',
            'title': '',
            'category': '',
            'borrower_user': '',
            'lender_user': '',
            'is_rental': '',
        }



class LenderForm(forms.Form):
    lender = forms.ModelChoiceField(User.objects.filter(is_superuser=True),  label='', empty_label='選択してください', to_field_name='pk', required=True)