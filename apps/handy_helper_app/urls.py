from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^users/create$', views.create_user),
    url(r'^users/session/create$', views.create_session),
    url(r'^users/logout$', views.destroy_session),
    url(r'^jobs/new$', views.new_job),
    url(r'^jobs/create$', views.create_job),
    url(r'^jobs/(?P<id>\d+)$', views.show_job),
    url(r'^jobs/(?P<id>\d+)/edit$', views.edit_job),
    url(r'^jobs/(?P<id>\d+)/update$', views.update_job),
    url(r'^jobs/(?P<id>\d+)/delete$', views.delete_job),
    url(r'^users/jobs/(?P<id>\d+)/add$', views.add_job_to_user),
    url(r'^users/jobs/(?P<id>\d+)/remove$', views.remove_job_to_user)
]