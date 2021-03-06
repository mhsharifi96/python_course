# Generated by Django 3.2.5 on 2021-07-14 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0011_alter_taskmodels_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='taskmodels',
            options={},
        ),
        migrations.AlterModelOptions(
            name='testfieldsmoels',
            options={'ordering': ['DateTimeField'], 'verbose_name': 'تسک', 'verbose_name_plural': 'تسک ها'},
        ),
        migrations.AddField(
            model_name='testfieldsmoels',
            name='verbose_name',
            field=models.CharField(default='', max_length=500, verbose_name='توضیح اضافی'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='testfieldsmoels',
            name='help_text',
            field=models.CharField(help_text='این متن برای کمک به توفقط والا', max_length=500),
        ),
    ]
