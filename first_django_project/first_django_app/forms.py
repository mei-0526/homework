from django import forms
        
#モデルクラスを呼出
from .models import People

#フォームクラス作成
class Contact_Form(forms.ModelForm):

    class Meta():
        #モデルクラスを指定
        model = People

        #表示するモデルクラスのフィールドを定義
        fields = ('Name',
                  'Gender',
                  'Birthday',
                  'Postalcode',
                  'address',
                  'Tell',
                  'Mail',
                  'Inquiry',
                  'FreeText')

        #表示ラベルを定義
        labels = {'Name':"名前",
                  'Gender':'性別',
                  'Birthday':"生年月日",
                  'Postalcode':'郵便番号',
                  'address':'住所',
                  'Tell':"電話番号",
                  'Mail':"メール",
                  'Inquiry':'問い合わせの種類',
                  'FreeText':"相談内容",
        }