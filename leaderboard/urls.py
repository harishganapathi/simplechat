from django.conf.urls import url
from . import views 



urlpatterns = [ 
    url(r'^$',views.landingpage , name='score_list'),
    url(r'^create$',views.create,name= 'create'),
    url(r'^.*signup$' , views.signup ,name='signup'),
    url(r'^.*signin$', views.signin, name='signin'),
    url(r'^.*signout/$', views.signout, name="signout"),
    url(r'^join$',views.join,name = 'join'),
    url(r'^.*sendmessage$', views.sendmessage, name='sendmessage'),
    url(r'^.*broadcast$', views.broadcast, name='broadcast'),
    ]


