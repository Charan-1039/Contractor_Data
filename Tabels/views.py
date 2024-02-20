from django.shortcuts import render,HttpResponse,redirect
from Tabels.models import Taluk_Field,Tabel_Data,Month_Field,HeadAccount_Field
import xlwt
# Create your views here.

def index(request):
    D=''
    Taluk    =   Taluk_Field.objects.all()
    Month = Month_Field.objects.all()
    HeadAccount    =   HeadAccount_Field.objects.all() 
    context  =   {'Taluk':Taluk,'Month_Field':Month,'HeadAccounr_Field':HeadAccount}
    return render(request,'Details.html',context)

def Home_Page(request):
    return render(request,'Home.html')

def Show_Details(request):
    Details     =   Tabel_Data.objects.all()
    context     =   {'Data':Details}
    return render(request,'ShowDetails.html',context)

def AddDetails(request):
    D=''
    P=''
    Taluk    =   Taluk_Field.objects.all()
    Month = Month_Field.objects.all()
    HeadAccount    =   HeadAccount_Field.objects.all() 
    if request.method =='POST':
        Title       =   request.POST.get('TITLE')
        Taluk       =   request.POST.get('TALUK')
        Month       =   request.POST.get('MONTH')
        Year        =   request.POST.get('YEAR')
        Acc         =   request.POST.get('ACC')
        save        =   Tabel_Data(Data_Title=Title,Taluk=Taluk,Month=Month,Account=Acc,Year=Year)
        save.save()
        D='Data Saved Scuessfully'
    else:
        P='Please Fill The Form'
    context  =   {'Taluk':Taluk,'Month_Field':Month,'HeadAccounr_Field':HeadAccount,'D':D,'P':P}
    return render(request,'Details.html',context)


def view_Data(request,V_id):
    data        =   Tabel_Data.objects.get(id=V_id)
    context     =   {'data':data}
    return render(request,'View_page.html',context)

def Export_Data(request):
    Taluk    =   Taluk_Field.objects.all()
    Month = Month_Field.objects.all()
    HeadAccount    =   HeadAccount_Field.objects.all() 
    if request.method =='GET':
        taluk       =   request.GET.get('TALUK')
        month       =   request.GET.get('MONTH')
        year        =   request.GET.get('YEAR')
        acc         =   request.GET.get('ACC')
        data        =   Tabel_Data.objects.filter(Taluk__icontains=taluk,Month__icontains=month,Year__icontains=year,Account__icontains=acc)
    else:
        pass
    context     =   {'data':data,'Taluk':Taluk,'Month_Field':Month,'HeadAccounr_Field':HeadAccount}
    return render(request,'ExportData.html',context)


def Search_Data(request):
    Taluk    =   Taluk_Field.objects.all()
    Month =     Month_Field.objects.all()
    HeadAccount    =   HeadAccount_Field.objects.all() 
    taluk       =   request.GET.get('TALUK')
    month       =   request.GET.get('MONTH')
    year        =   request.GET.get('YEAR')
    acc         =   request.GET.get('ACC')
    data        =   Tabel_Data.objects.filter(Taluk__icontains=taluk,Month__icontains=month,Year__icontains=year,Account__icontains=acc)

    context     =   {'data':data,'Taluk':Taluk,'Month_Field':Month,'HeadAccounr_Field':HeadAccount}
    return redirect(request,'ExportData.html',context)

def exview(request):
    return render(request,'exview.html')

def Search_ExportData(request):
    if request.method =='GET':
        Taluk       =   request.GET.get('TALUK')
        Month       =   request.GET.get('MONTH')
        Year        =   request.GET.get('YEAR')
        Acc         =   request.GET.get('ACC')
        # export(request,Taluk,Month,Year,Acc)
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="student.xls"'
 
        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Progress Report')
 
        # Sheet header, first row
        row_num = 0
 
        font_style = xlwt.XFStyle()
        font_style.font.bold = True
 
        columns = ['Data_Title', 'Taluk', 'Year','Month', 'Account']
 
        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)
 
        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()
 
        rows = Tabel_Data.objects.filter(Taluk__icontains=Taluk,Month__icontains=Month,Year__icontains=Year,Account__icontains=Acc).values_list('Data_Title', 'Taluk', 'Year', 'Month','Account')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)
 
        wb.save(response)
   

    return response


# #def export(request,Taluk,Month,Year,Acc):
#     response = HttpResponse(content_type='application/ms-excel')
#     response['Content-Disposition'] = 'attachment; filename="student.xls"'
#     taluk = Taluk
#     month = Month
#     year = Year
#     acc = Acc
#     wb = xlwt.Workbook(encoding='utf-8')
#     ws = wb.add_sheet('Progress Report')
 
#         # Sheet header, first row
#     row_num = 0
 
#     font_style = xlwt.XFStyle()
#     font_style.font.bold = True
 
#     columns = ['Data_Title', 'Taluk', 'Year','Month', 'Account']
 
#     for col_num in range(len(columns)):
#         ws.write(row_num, col_num, columns[col_num], font_style)
 
#         # Sheet body, remaining rows
#     font_style = xlwt.XFStyle()
 
#     rows = Tabel_Data.objects.filter(Taluk__icontains=taluk,Month__icontains=month,Year__icontains=year,Account__icontains=acc).values_list('Data_Title', 'Taluk', 'Year', 'Month','Account')
#     for row in rows:
#         row_num += 1
#         for col_num in range(len(row)):
#             ws.write(row_num, col_num, row[col_num], font_style)
 
#     wb.save(response)
   

#     return response

def export(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="student.xls"'
 
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Progress Report')
 
        # Sheet header, first row
    row_num = 0
 
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
 
    columns = ['Data_Title', 'Taluk', 'Year','Month', 'Account']
 
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
 
        # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
 
    rows = Tabel_Data.objects.all().values_list('Data_Title', 'Taluk', 'Year', 'Month','Account')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
 
    wb.save(response)
   

    return response
    

