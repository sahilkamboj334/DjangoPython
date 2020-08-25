from django.urls import path,include
from ServerUI import settings
from . import views
from .views import GenericView
urlpatterns = [
    path(r'',views.index,name='index'),  
    path(r'token',views.get_token,name='token'), 
    path(r'rest/index',views.rest_view,name='rest view'),
    path(r'rest/generic/index',GenericView.as_view(),name=' view'),
    path('add',views.add,name='add issue'),
    path(r'signup/',views.signup,name='signup'),   

]