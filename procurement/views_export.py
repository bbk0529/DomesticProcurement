from .models import Assay, ChangeLog
from django.http import HttpResponse
import xlwt
def export_data_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="data.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('data')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = [
        'SA_No',
        'Date',
        'Number_of_suppliers',
        'Type',
        'Details_1',
        'Details_2',
        'Description',
        'Category',
        'Updated_date',
        'Supplier1',
        'Supplier1_Fabricating_Goods',
        'Supplier1_Modification_of_free_offerd_item',
        'Supplier1_Qty',
        'Supplier1_Final_Unit_Price',
        'Supplier2',
        'Supplier2_Fabricating_Goods',
        'Supplier2_Modification_of_free_offerd_item',
        'Supplier2_Qty',
        'Supplier2_Final_Unit_Price',
        'Supplier3',
        'Supplier3_Fabricating_Goods',
        'Supplier3_Modification_of_free_offerd_item',
        'Supplier3_Qty',
        'Supplier3_Final_Unit_Price',
        'Supplier4',
        'Supplier4_Fabricating_Goods',
        'Supplier4_Modification_of_free_offerd_item',
        'Supplier4_Qty',
        'Supplier4_Final_Unit_Price',
        'Supplier5',
        'Supplier5_Fabricating_Goods',
        'Supplier5_Modification_of_free_offerd_item',
        'Supplier5_Qty',
        'Supplier5_Final_Unit_Price',
        'Supplier6',
        'Supplier6_Fabricating_Goods',
        'Supplier6_Modification_of_free_offerd_item',
        'Supplier6_Qty',
        'Supplier6_Final_Unit_Price',
        'Supplier7',
        'Supplier7_Fabricating_Goods',
        'Supplier7_Modification_of_free_offerd_item',
        'Supplier7_Qty',
        'Supplier7_Final_Unit_Price',
        'Supplier8',
        'Supplier8_Fabricating_Goods',
        'Supplier8_Modification_of_free_offerd_item',
        'Supplier8_Qty',
        'Supplier8_Final_Unit_Price',
    ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Assay.objects.all().values_list(
        'SA_No',
        'Date',
        'Number_of_suppliers',
        'Type',
        'Details_1',
        'Details_2',
        'Description',
        'Category',
        'Updated_date',
        'Supplier1',
        'Supplier1_Fabricating_Goods',
        'Supplier1_Modification_of_free_offerd_item',
        'Supplier1_Qty',
        'Supplier1_Final_Unit_Price',
        'Supplier2',
        'Supplier2_Fabricating_Goods',
        'Supplier2_Modification_of_free_offerd_item',
        'Supplier2_Qty',
        'Supplier2_Final_Unit_Price',
        'Supplier3',
        'Supplier3_Fabricating_Goods',
        'Supplier3_Modification_of_free_offerd_item',
        'Supplier3_Qty',
        'Supplier3_Final_Unit_Price',
        'Supplier4',
        'Supplier4_Fabricating_Goods',
        'Supplier4_Modification_of_free_offerd_item',
        'Supplier4_Qty',
        'Supplier4_Final_Unit_Price',
        'Supplier5',
        'Supplier5_Fabricating_Goods',
        'Supplier5_Modification_of_free_offerd_item',
        'Supplier5_Qty',
        'Supplier5_Final_Unit_Price',
        'Supplier6',
        'Supplier6_Fabricating_Goods',
        'Supplier6_Modification_of_free_offerd_item',
        'Supplier6_Qty',
        'Supplier6_Final_Unit_Price',
        'Supplier7',
        'Supplier7_Fabricating_Goods',
        'Supplier7_Modification_of_free_offerd_item',
        'Supplier7_Qty',
        'Supplier7_Final_Unit_Price',
        'Supplier8',
        'Supplier8_Fabricating_Goods',
        'Supplier8_Modification_of_free_offerd_item',
        'Supplier8_Qty',
        'Supplier8_Final_Unit_Price',
    )
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response



def export_log_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="changeLog.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('changeLog')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = [
            'SA_No',
            'DateTime',
            'User',
            'Field',
            'Before',
            'After',
    ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = ChangeLog.objects.all().values_list(
            'SA_No',
            'DateTime',
            'User',
            'Field',
            'Before',
            'After',

    )
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response
