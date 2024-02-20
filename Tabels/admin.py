from django.contrib import admin
from Tabels.models import Month_Field,Taluk_Field,HeadAccount_Field,Tabel_Data



class AdminTabel_Data(admin.ModelAdmin):

    model = Tabel_Data
    
    fields = ['Taluk','Year','Month','Account']

    list_display = ['Taluk','Year','Month','Account']



# Register your models here.
admin.site.register(Month_Field)
admin.site.register(Taluk_Field)
admin.site.register(HeadAccount_Field)
admin.site.register(Tabel_Data ,  AdminTabel_Data)

