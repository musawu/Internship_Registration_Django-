from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.show,name='home'),
    path('register/',views.register,name='register'),
    path('existing/',views.existing,name='existing'),
    path('search/',views.search,name='search'),
    path('cancel/',views.cancel,name='cancel'),

]