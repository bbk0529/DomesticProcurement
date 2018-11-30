import pandas as pd
from .models import Assay, ChangeLog
import datetime
from django.http import HttpResponse, JsonResponse

def import_data_xls(request):
    uploaded_file_url=request.GET['uploaded_file_url'].strip()
    print(uploaded_file_url)

    df=pd.read_excel('/dev/DomesticProcurement' + uploaded_file_url, dtype="object")
    print(df)
    df=df.fillna('')
    Assay.objects.all().delete()
    df.columns=[
        'SA_No',
        'Date',
        'Number_of_suppliers',
        'Type',
        'Details_1',
        'Details_2',
        'Description',
        'Category',
        'Updated_date',
        'Supplier1','Supplier1_Fabricating_Goods','Supplier1_Modification_of_free_offerd_item','Supplier1_Qty','Supplier1_Final_Unit_Price',
        'Supplier2','Supplier2_Fabricating_Goods','Supplier2_Modification_of_free_offerd_item','Supplier2_Qty','Supplier2_Final_Unit_Price',
        'Supplier3','Supplier3_Fabricating_Goods','Supplier3_Modification_of_free_offerd_item','Supplier3_Qty','Supplier3_Final_Unit_Price',
        'Supplier4','Supplier4_Fabricating_Goods','Supplier4_Modification_of_free_offerd_item','Supplier4_Qty','Supplier4_Final_Unit_Price',
        'Supplier5','Supplier5_Fabricating_Goods','Supplier5_Modification_of_free_offerd_item','Supplier5_Qty','Supplier5_Final_Unit_Price',
        'Supplier6','Supplier6_Fabricating_Goods','Supplier6_Modification_of_free_offerd_item','Supplier6_Qty','Supplier6_Final_Unit_Price',
        'Supplier7','Supplier7_Fabricating_Goods','Supplier7_Modification_of_free_offerd_item','Supplier7_Qty','Supplier7_Final_Unit_Price',
        'Supplier8','Supplier8_Fabricating_Goods','Supplier8_Modification_of_free_offerd_item','Supplier8_Qty','Supplier8_Final_Unit_Price',
    ]
    for i,v in df.iterrows() :
        print(i)
        Assay.objects.update_or_create(
                    SA_No=v['SA_No']                        ,
                    defaults={
                        'SA_No':v['SA_No'],
                        'Date':v['Date'],
                        'Number_of_suppliers':v['Number_of_suppliers'],
                        'Type':v['Type'],
                        'Details_1':v['Details_1'],
                        'Details_2':v['Details_2'],
                        'Description':v['Description'],
                        'Category':v['Category'],
                        'Updated_date':v['Updated_date'],

                        'Supplier1':v['Supplier1'],
                        'Supplier1_Fabricating_Goods':v['Supplier1_Fabricating_Goods'],
                        'Supplier1_Modification_of_free_offerd_item':v['Supplier1_Modification_of_free_offerd_item'],
                        'Supplier1_Qty':v['Supplier1_Qty'],
                        'Supplier1_Final_Unit_Price': v['Supplier1_Final_Unit_Price'],

                        'Supplier2':v['Supplier2'],
                        'Supplier2_Fabricating_Goods':v['Supplier2_Fabricating_Goods'],
                        'Supplier2_Modification_of_free_offerd_item':v['Supplier2_Modification_of_free_offerd_item'],
                        'Supplier2_Qty':v['Supplier2_Qty'],
                        'Supplier2_Final_Unit_Price': v['Supplier2_Final_Unit_Price'],

                        'Supplier3':v['Supplier3'],
                        'Supplier3_Fabricating_Goods':v['Supplier3_Fabricating_Goods'],
                        'Supplier3_Modification_of_free_offerd_item':v['Supplier3_Modification_of_free_offerd_item'],
                        'Supplier3_Qty':v['Supplier3_Qty'],
                        'Supplier3_Final_Unit_Price': v['Supplier3_Final_Unit_Price'],

                        'Supplier4':v['Supplier4'],
                        'Supplier4_Fabricating_Goods':v['Supplier4_Fabricating_Goods'],
                        'Supplier4_Modification_of_free_offerd_item':v['Supplier4_Modification_of_free_offerd_item'],
                        'Supplier4_Qty':v['Supplier4_Qty'],
                        'Supplier4_Final_Unit_Price': v['Supplier4_Final_Unit_Price'],

                        'Supplier5':v['Supplier5'],
                        'Supplier5_Fabricating_Goods':v['Supplier5_Fabricating_Goods'],
                        'Supplier5_Modification_of_free_offerd_item':v['Supplier5_Modification_of_free_offerd_item'],
                        'Supplier5_Qty':v['Supplier5_Qty'],
                        'Supplier5_Final_Unit_Price': v['Supplier5_Final_Unit_Price'],

                        'Supplier6':v['Supplier6'],
                        'Supplier6_Fabricating_Goods':v['Supplier6_Fabricating_Goods'],
                        'Supplier6_Modification_of_free_offerd_item':v['Supplier6_Modification_of_free_offerd_item'],
                        'Supplier6_Qty':v['Supplier6_Qty'],
                        'Supplier6_Final_Unit_Price': v['Supplier6_Final_Unit_Price'],

                        'Supplier7':v['Supplier7'],
                        'Supplier7_Fabricating_Goods':v['Supplier7_Fabricating_Goods'],
                        'Supplier7_Modification_of_free_offerd_item':v['Supplier7_Modification_of_free_offerd_item'],
                        'Supplier7_Qty':v['Supplier7_Qty'],
                        'Supplier7_Final_Unit_Price': v['Supplier7_Final_Unit_Price'],


                        'Supplier8':v['Supplier8'],
                        'Supplier8_Fabricating_Goods':v['Supplier8_Fabricating_Goods'],
                        'Supplier8_Modification_of_free_offerd_item':v['Supplier8_Modification_of_free_offerd_item'],
                        'Supplier8_Qty':v['Supplier8_Qty'],
                        'Supplier8_Final_Unit_Price': v['Supplier8_Final_Unit_Price'],
                    }
        )

    ChangeLog.objects.create(
        SA_No=99999,
        DateTime=datetime.datetime.now(),
        User=request.user.username,
        Field="Imported and Initialized",
        Before='',
        After='',
    )

    return HttpResponse('')
