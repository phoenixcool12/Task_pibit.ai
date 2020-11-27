from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$',views.index, name = "index"),
    path('upload/', views.image_upload_view)
    #path('inc/<temp>/',views.inc, name = "inc"),
    #path('desc/<temp>/',views.desc, name = "desc"),
]