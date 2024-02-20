from django.contrib import admin
from django.urls import path
from Tabels import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('',views.Home_Page, name='index'),
    path('Details',views.AddDetails, name='Details'),
    path('ShowDetails',views.Show_Details, name='ShowDetails'),
    path('view_Data/<V_id>',views.view_Data, name='view_Data'),
    path('Export_Data',views.Export_Data, name='Export_Data'),
    path('Search_ExportData',views.Search_ExportData, name='Search_ExportData'),
    path('Search_Data',views.Search_Data, name='Search_Data'),
    path('exview',views.exview, name='exview'),
    path('export',views.export, name='export'),
    
]