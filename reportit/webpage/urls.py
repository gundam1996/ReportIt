from django.conf.urls import include, url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    #url(r'^login/$', auth_views.login, name='login'),
    url(r'^login/$', auth_views.login, {'template_name': 'webpage/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^$', views.home, name = 'home'),
    url(r'^reporterSignup/$', views.reporterSignup, name = 'reporterSignup'),
    url(r'^agentSignup/$', views.agentSignup, name = 'agentSignup'),
    url(r'^account/profile/$', views.viewProfile, name = 'profile'),
    url(r'^account/dashboard/$', views.dashboard, name = 'dashboard'),
    url(r'^account/profile/$', views.viewProfile, name = 'profile'),
    url(r'^account/profile/edit$', views.editProfile, name = 'editprofile'),

    url(r'^account/submitConcern/', views.submitConcern, name = 'submitConcern'),
    url(r'^account/uploadVerification/', views.uploadVerification, name = 'uploadVerification'),
    url(r'^account/sign_s3?', views.sign_s3, name = 'sign_s3'),
    url(r'^account/viewSpecificConcern/', views.viewSpecificConcern, name = 'viewSpecificConcern'),
    url(r'^account/removeSpecificConcern/', views.removeSpecificConcern, name = 'removeSpecificConcern'),
    url(r'^account/editSpecificConcern/', views.editSpecificConcern, name = 'editSpecificConcern'),
    url(r'^account/viewConcern/', views.viewConcern, name = 'viewConcern'),
    url(r'^account/dashboard$', views.dashboard, name = 'dashboard'),
    url(r'^account$', views.dashboard, name = 'dashboard'),

    # url(r'^.*$', views.notFound, name = '404notFound'),

    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset_email_sent/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    #add for third party login
    url(r'^oauth/', include('social_django.urls', namespace='social')),

    url(r'^getallagents$', views.getAllAgents, name = 'dashboard'),

]