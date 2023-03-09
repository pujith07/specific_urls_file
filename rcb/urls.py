from django.urls import path
from rcb.views import *

app_name='nothing'

urlpatterns=[
    path('kholi/',kholi,name='kholi'),
    path('abd/',abd,name='abd'),
]