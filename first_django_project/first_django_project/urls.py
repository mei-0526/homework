"""first_django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
# Include関数をインポート
from django.urls import include

# path関数でApp_Folder内のurls.pyを読み込むために、include関数を記述
urlpatterns = [
    path('admin/', admin.site.urls),                    # 管理画面のPath
    path('first_django_app/', include('first_django_app.urls'),name="formpage"),    # アプリケーション管理フォルダのurls.pyと関連づけるpath
]
