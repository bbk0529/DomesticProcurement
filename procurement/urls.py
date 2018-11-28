from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static
# import views

urlpatterns=[
    path('',views.listAssay, name='listAssay'),
    path('approvalPlan', views.approvalPlan, name='approvalPlan'),
    path('changeLog',views.changeLog, name='changeLog'),
    path('setting',views.setting, name='setting'),
    path('approvalPlanQuery', views.approvalPlanQuery, name='approvalPlanQuery'),
    path('approvalPlanCreate', views.approvalPlanCreate, name='approvalPlanCreate'),
    path('assayQuery',views.assayQuery, name='assayQuery'),
    path('updateQuery',views.updateQuery, name='updateQuery'),
    path('deleteRecord',views.deleteRecord, name='deleteRecord'),
    url(r'^export/xls/data/$', views.export_data_xls, name='export_data_xls'),
    url(r'^export/xls/log/$', views.export_log_xls, name='export_log_xls'),
    url('import_data_xls', views.import_data_xls, name='import_data_xls'),
    # url(r'^uploads/simple/$', views.upload, name='upload'),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
