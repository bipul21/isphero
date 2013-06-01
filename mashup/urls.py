from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'mashup.views.home', name='home'),
      url(r'^push','mashup.views.push',name='search'),
                       url(r'^reset','mashup.views.reset',name='reset'),
                       url(r'^changeColor','mashup.views.changeColor',name='changeColor'),
                       url(r'^showHead','mashup.views.showHead',name='changeColor')
                       
)
