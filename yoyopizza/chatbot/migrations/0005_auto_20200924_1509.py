# Generated by Django 3.1.1 on 2020-09-24 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0004_auto_20200924_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placeorder',
            name='Offers',
            field=models.CharField(choices=[('buy 2 get 1 free', 'Buy 2 in NonVeg Pizza get 1 in Veg Pizza free'), ('buy 3 get 1 dessert', 'Buy 3 Pizza get any Dessert free')], max_length=100),
        ),
        migrations.AlterField(
            model_name='placeorder',
            name='Phone_Number',
            field=models.CharField(default='+91', max_length=15),
        ),
    ]