# Generated by Django 5.1 on 2025-06-07 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saving_account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='featuredescription',
            name='feature',
        ),
        migrations.RemoveField(
            model_name='savingaccountpage',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='AccountFeature',
        ),
        migrations.DeleteModel(
            name='FeatureDescription',
        ),
        migrations.DeleteModel(
            name='SavingAccountPage',
        ),
    ]
