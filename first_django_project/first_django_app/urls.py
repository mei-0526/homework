#path関数をインポート
from django.urls import path
# 同ディレクトリからview.pyをインポート
from . import views

#path関数(アクセスするアドレス、呼び出す処理)を追記
urlpatterns = [
    #path('', views.index, name='index'),
    path('formpage', views.FormView.as_view(),name="formpage"),
]