# Generated by Django 3.2.5 on 2021-07-13 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_auto_20210713_1828'),
    ]

    operations = [
        migrations.CreateModel(
            name='testFieldsMoels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='nameTest', max_length=500)),
                ('code', models.IntegerField(db_column='codeTest', db_index=True)),
                ('constant', models.CharField(db_column='constantTest', default='constant field', editable=False, max_length=500)),
                ('error_messages', models.CharField(error_messages={'blank': 'داداجون ول کن مارو باشه', 'null': ' داداش نکن این کارو'}, max_length=500)),
                ('help_text', models.CharField(help_text='این متن برای کمک به توفقط والا', max_length=500)),
            ],
        ),
    ]
