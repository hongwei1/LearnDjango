"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

#The URL declarations for this Django project; a "table of contents" 
#Although you can put app `poll` to anywhere, but `mysite` is still the top level project, 
#all the settings are under this path.
#for this urls.py, this is the entrypoint of Django, first will search for urls here.
urlpatterns = [
    path('admin/', admin.site.urls),# should always use include(), this is the only exception. 
    #point the root URLconf for the poll.urls module.
    # the include() function allows referencing other URLconfs. 
    #   whenever Django encounters include(), it chops off whatever part of the URL matched up to that point.
    #   and sends the remaining string to the included URLconf for further processing.
    path('polls/', include('polls.urls'))
]
