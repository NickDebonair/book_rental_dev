from django.contrib import admin
from .models import *
from django import forms

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)


# ※このModelForm無意味※
class MyModelForm(forms.ModelForm):
    due_date = forms.DateInput()

    class Meta:
        model = LendingStatus
        fields = '__all__'

    def get_initial_for_field(self, field, field_name):
        if field_name == 'rating':
            if self.instance:
                return self.instance.get_due_date()
            return None
        return super().get_initial_for_field(field, field_name)


class LendingStatusAdmin(admin.ModelAdmin):
    form = MyModelForm
    readonly_fields = ('checkout_date', 'returned_date')


# admin.site.register(Country, CountryAdmin)



# class LendingStatusAdmin(admin.ModelAdmin):
#     readonly_fields = ('checkout_date', 'returned_date', 'due_date')
    
#     def due_date(self, instance):
#         return instance.get_due_date()


admin.site.register(LargeCategory)
admin.site.register(SmallCategory)
admin.site.register(Books, BookAdmin)
admin.site.register(LendingStatus, LendingStatusAdmin)