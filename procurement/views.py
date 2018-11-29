from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Assay, ChangeLog
import datetime
import decimal
from .views_updateQuery import *
from .views_export import *
from .views_import import *

from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .models import Document
from .forms import DocumentForm


@csrf_exempt
def deleteRecord(request) :
    SA_No=request.POST.get('SA_No')
    print(SA_No*100)
    Assay.objects.filter(SA_No=SA_No).delete()
    As=Assay.objects.all()
    ipAddress=get_client_ip(request)

    if request.user.username=='buyer' or 'cjlee' or 'ejkim' or 'shji':
        ChangeLog.objects.create(
            SA_No=SA_No,
            DateTime=datetime.datetime.now(),
            User=request.user.username,
            Field="Deleted",
            Before='',
            After='',
        )

        return render(
            request, 'procurement/approvalPlan.html',{
            'assayList' : As,
            'ipAddress' : ipAddress
            }
        )



    else:
        return redirect('/')

# Create your views here.
# As=Assay.objects.order_by('SA_No')[:20]#
# ############################################
# def setting(request):
#     ipAddress=get_client_ip(request)
#     if request.user.username=='buyer':
#         return render(
#             request, 'procurement/setting.html',{
#             'assayList' : As,
#             'ipAddress' : ipAddress
#             }
#         )
#     else:
#         return redirect('/')


#######################################
# MAIN default                        #
#######################################
def approvalPlan(request):
    As=Assay.objects.all()
    ipAddress=get_client_ip(request)

    if request.user.username=='buyer' or 'cjlee' or 'ejkim' or 'shji':

        # if request.method == 'GET':
        #     SA_No=request.GET['SA_No'].strip()
        #     print("READ ASSAY___",SA_No)
        #     Ass=Assay.objects.get(SA_No=SA_No)


        return render(
            request, 'procurement/approvalPlan.html',{
            'assayList' : As,
            'ipAddress' : ipAddress
            }
        )
    else:
        return redirect('/')
####################################################
def listAssay(request) :
    As=Assay.objects.all()
    ipAddress=get_client_ip(request)
    if request.user.is_authenticated:
        return render(
            request, 'procurement/assayList.html',{
            'assayList' : As,
            'ipAddress' : ipAddress
        })
    else:
        return redirect('login')
def assayQuery(request) :
    As=Assay.objects.all()
    if request.method=='GET':
        print("request.method = GET ///assay Query")
        SA_No=request.GET['SA_No'].strip()
        Ass=Assay.objects.get(SA_No=SA_No)
        print(SA_No)

    return render(
        request, 'procurement/assayListDetail.html',{
            'Assay' : Ass,
            'assayList' : As
    })
def approvalPlanQuery(request):
    As=Assay.objects.all()
    if request.method == 'GET':
        SA_No=request.GET['SA_No'].strip()
        print("READ ASSAY___",SA_No)
        Ass=Assay.objects.get(SA_No=SA_No)

    return render(
        request,
        'procurement/approvalPlanBody.html',{
            'Assay' : Ass,
            'assayList' : As
        }
    )
def approvalPlanCreate(request):
    return render(
        request,
        'procurement/approvalPlanBody.html',{
        }
    )
#########################################################
def changeLog(request):
    ipAddress=get_client_ip(request)
    if request.user.username=='buyer' or 'cjlee' or 'ejkim' or 'shji':
        changeLog=ChangeLog.objects.order_by('-DateTime','SA_No')
        return render(
            request, 'procurement/changeLog.html',{
            'changeLog' : changeLog,
            'ipAddress' : ipAddress
        })
    else:
        return redirect('/')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

import pandas as pd
def setting(request):
    print('simple load')
    if request.method == 'POST' and request.FILES['myfile']:
        print('post received')
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)

        uploaded_file_url = fs.url(filename)
        return render(request, 'procurement/setting.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'procurement/setting.html')
