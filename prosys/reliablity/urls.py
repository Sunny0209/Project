from django.urls import path
from . import views


urlpatterns = [
    path('upload.html/',views.predictor,name='predictor'),
    path('result.html/',views.result,name='result'),
    path('',views.home,name='home')
]