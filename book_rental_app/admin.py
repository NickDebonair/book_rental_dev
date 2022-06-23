from django.contrib import admin
from .models import *
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)

class LendingStatusAdmin(admin.ModelAdmin):
    readonly_fields = ('checkout_date', 'returned_date')

admin.site.register(LargeCategory)
admin.site.register(SmallCategory)
admin.site.register(Books, BookAdmin)
admin.site.register(LendingStatus)