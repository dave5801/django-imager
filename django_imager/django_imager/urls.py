"""django_imager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from imager_profile.views import home_view
from imager_profile import views
from imager_images.views import PhotoForm, AlbumForm, LibraryView, SinglePhotoView, SingleAlbumView, LogoutView, OneProfileView, PublicPhotosView, PublicAlbumsView, UpdatePhoto, UpdateAlbum, UpdateProfile
from django.contrib.auth import views as auth_views



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_view, name='homepage'),
    url(r'^login/$', auth_views.login, {'template_name': 'imager_profile/login.html'}, name='login'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name='activate'),
    url(r'^register/$', views.register_view, name='register'),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'^profile/$', views.profile_view, name='profile'),
    url(r'^images/photos/add/', PhotoForm.as_view(), name='add-photo'),
    url(r'^images/albums/add/', AlbumForm.as_view(), name='add-album'),
    url(r'^images/photos/', PublicPhotosView.as_view(), name='public-photos'),
    url(r'^images/albums/', PublicAlbumsView.as_view(), name='public-albums'),
    url(r'^images/library/$', LibraryView.as_view(), name='library'),
    url(r'^images/album/(?P<pk>\w)/edit', UpdateAlbum.as_view(), name='edit-album'),
    url(r'^profile/edit$', UpdateProfile.as_view(), name='edit-profile'),
    url(r'^logout/', LogoutView.as_view(), name='logout')
]


'''
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home_view, name='homepage')
]
'''