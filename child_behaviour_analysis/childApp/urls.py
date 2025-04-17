from django.conf.urls import url
from childApp import views
from django.urls import path

app_name = 'childApp'

urlpatterns = [
    path('', views.dataUploadView.as_view(), name='child'),
    #path('whats', views.WhatsappAnalaysis.as_view(), name = 'whats'),
    #path('result', views.finalresult.as_view(), name= 'result'),
    #path('success', views.Success.as_view(), name = 'success'),
    #path('fail',views.Failure.as_view(),name='fail'),
    #path('filenot',views.FileNotfound.as_view(), name='filenot'),
    #path('aboutus',views.AboutUs.as_view(), name='aboutus')
]
