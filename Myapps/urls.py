from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/',views.about,name='about'),
    path('treatment/',views.treatment,name='treatment'),
    path('doctors/',views.doctors,name="doctors"),
    path('contact/',views.contact,name='contact'),

    path('register/',views.register,name='register'),
    path('login_page/',views.login_page,name='login_page'),
    path('logout_page/',views.logout_page,name='logout_page'),
    path('dhashboard/',views.dhashboard,name='dhashboard'),

    path('apoinmentbookdetails/',views.apoinmentbookdetails,name='apoinmentbookdetails'),
    path('pationdetails/',views.pationdetails,name='pationdetails'),
    path('datapations/',views.datapations,name='datapations'),
    path('success/',views.success,name='success'),

    path('item/<int:pk>/update/', views.update, name='update'),
    path('item/<int:pk>/delete/', views.delete, name='delete'),

    path('item/<int:pk>/updates/', views.updates, name='updates'),
    path('item/<int:pk>/deletes/', views.deletes, name='deletes'),
 
]