from django.conf.urls import url
from blog import views
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^admin/', admin.site.urls),
    # views.post_detail(pk=<num>)
    url(r'^post/(?P<pk>\d+)/$', views.post_detail),
]