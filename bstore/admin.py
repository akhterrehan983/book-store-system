from django.contrib import admin
from bstore.models import U_table
# Register your models here.

class U_tableAdmin(admin.ModelAdmin):
    list_display=['isbno','price']
admin.site.register(U_table,U_tableAdmin)
# admin.site.register(U_table)