# Generated by Django 3.0 on 2020-02-08 08:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='InfoUser',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('prefere', models.IntegerField()),
                ('ban', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Vaisseau',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=250)),
                ('empruter', models.BooleanField()),
                ('etat', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Emprunt',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('date_emprunt', models.DateTimeField()),
                ('date_retour', models.DateTimeField()),
                ('id_vaisseau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siteweb.Vaisseau')),
            ],
        ),
    ]