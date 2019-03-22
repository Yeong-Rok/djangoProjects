"""secondproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name='home'), # blog.views의 home 함수를 호출하라
    path('blog/<int:blog_id>/', blog.views.detail, name='detail'),  # <int:blog_id>는 path-converter // 장고에서 여러 객체들을 다루는 계층적 url이 필요할 경우에 사용함 -> '지정한 converter type의 name변수를 view 함수로 넘겨라' )
    path('blog/new/', blog.views.new, name='new'),
    path('blog/create/', blog.views.create, name='create'),
    path('blog/<int:blog_id>/edit/', blog.views.edit, name='edit'),
    path('blog/<int:blog_id>/delete/', blog.views.delete, name='delete'),
]
