from django.conf.urls import patterns, include, url

from django.contrib import admin
from registration.backends.default.views import RegistrationView
from customRegistration.forms import ExRegistrationForm
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoRegistration.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'accounts/register/$', 
    #    RegistrationView.as_view(form_class = ExRegistrationForm), 
    #    name = 'registration_register'),
    (r'^accounts/', include('registration.urls')),
)
