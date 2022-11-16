# Generated by Django 4.1.3 on 2022-11-17 02:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_offbody_timestamp_alter_selfreport_timestamp'),
    ]

    operations = [
        migrations.CreateModel(
            name='SelfReportLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.BigIntegerField(db_index=True)),
                ('voluntary', models.BooleanField()),
                ('self_report', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.selfreport')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]