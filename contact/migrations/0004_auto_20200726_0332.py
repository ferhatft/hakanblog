# Generated by Django 3.0.3 on 2020-07-26 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20200725_0400'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(choices=[('Satmak', 'Satmak'), ('Satın Almak', 'Satın Almak'), ('Kiraya Vermek', 'Kiraya Vermek'), ('Kiralamak', 'Kiralamak'), ('Gayrimenkul Değerlemesi', 'Gayrimenkul Değerlemesi'), ('Arsa Yatırımı', 'Arsa Yatırımı'), ('Diğer', 'Diğer'), ('Talebiniz', 'Talebiniz')], default='Talebiniz', max_length=25),
        ),
    ]
