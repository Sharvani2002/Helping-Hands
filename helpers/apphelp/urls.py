from django.conf.urls import url
from apphelp import views
from django.conf import settings
from django.conf.urls.static import static

# SET THE NAMESPACE!
app_name = 'apphelp'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)