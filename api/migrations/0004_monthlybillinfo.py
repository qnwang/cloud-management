# Generated by Django 2.1.2 on 2018-11-02 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20181101_1053'),
    ]

    operations = [
        migrations.CreateModel(
            name='MonthlybillInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('billingCycle', models.CharField(db_column='month', max_length=255)),
                ('productCode', models.CharField(db_column='product_code', max_length=255)),
                ('productName', models.CharField(db_column='product_name', max_length=255)),
                ('instanceId', models.CharField(db_column='instance_id', max_length=255)),
                ('instanceName', models.CharField(db_column='instance_name', max_length=255)),
                ('businessLine', models.CharField(db_column='business_line', max_length=255)),
                ('env', models.CharField(db_column='env', max_length=255)),
                ('regionId', models.CharField(db_column='region_id', max_length=255)),
                ('status', models.CharField(db_column='status', max_length=255)),
                ('subscriptionType', models.CharField(db_column='subscription_type', max_length=255)),
                ('pretaxAmount', models.FloatField(db_column='pretax_amount', max_length=255)),
                ('remark', models.CharField(db_column='remark', max_length=255)),
            ],
        ),
    ]