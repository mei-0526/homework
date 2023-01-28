from django.db import models

# 性別選択
Gender_CHOICES = [
    ('男','男'),
    ('女','女'),
]

#お問い合わせ選択
Inquiry_CHOICES = [
    ('商品について', '商品について'),
    ('内容について', '内容について'),
    ('その他','その他'),
]

# モデルクラスを作成
# 項目定義
class People(models.Model):
	# 名前（必須・５０文字以内）
    Name     = models.CharField(
        max_length=50
        )
    #　性別（必須）
    Gender = models.TextField(
        choices=Gender_CHOICES
        )
    
    # 生年月日（必須）      
    Birthday = models.DateField(
        )
    #郵便番号(必須)
    Postalcode = models.IntegerField(
        )
    #住所（必須・２００文字）
    address = models.CharField(
        max_length=200
        )
    # 電話番号(任意)   
    Tell = models.IntegerField(
        blank=True, 
        null=True
        ) 
    # Email
    Mail = models.EmailField(
        max_length=100
        )
    #問い合わせの種類(選択式・必須) 
    Inquiry = models.TextField(
        choices = Inquiry_CHOICES
        )
    # 相談内容                     
    FreeText = models.TextField(
        max_length=1000)
    
    # テキスト表示
    def __str__(self):
    	return self.name

