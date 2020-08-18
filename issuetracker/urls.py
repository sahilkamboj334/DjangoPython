from django.urls import path,include
from ServerUI import settings
from . import views
urlpatterns = [
    path(r'',views.index,name='index'),  
    path('add',views.add,name='add issue'),
    path(r'signup/',views.signup,name='signup'),   

]