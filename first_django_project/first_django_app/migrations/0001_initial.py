# Generated by Django 4.1.5 on 2023-01-28 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Gender', models.TextField(choices=[(1, '男'), (2, '女')])),
                ('Birthday', models.DateField()),
                ('Postalcode', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('Tell', models.IntegerField(blank=True, null=True)),
                ('Mail', models.EmailField(max_length=100)),
                ('Inquiry', models.TextField(choices=[(1, '商品について'), (2, '内容について'), (3, 'その他')])),
                ('FreeText', models.TextField(max_length=1000)),
            ],
        ),
    ]