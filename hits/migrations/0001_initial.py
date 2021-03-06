# Generated by Django 3.2.6 on 2021-08-09 14:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('target_name', models.CharField(max_length=100)),
                ('state', models.CharField(choices=[('NotAssigned', 'NotAssigned'), ('Assigned', 'Assigned'), ('Failed', 'Failed'), ('Completed', 'Completed')], default='NotAssigned', max_length=15)),
                ('assigned_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_by', to=settings.AUTH_USER_MODEL)),
                ('hitman', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hitman', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
