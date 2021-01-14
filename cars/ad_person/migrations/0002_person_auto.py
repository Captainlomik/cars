# Generated by Django 3.1.5 on 2021-01-14 17:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ad_person', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person_auto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('car_type', models.CharField(choices=[('минивен', 'минивен'), ('универсал', 'универсал'), ('минивен', 'хэтчбек'), ('купе', 'купе'), ('внедорожник', 'внедорожник'), ('кабриолет', 'кабриолет'), ('пикап', 'пикап')], help_text='тип кузова', max_length=30, null=True)),
                ('price', models.IntegerField(null=True)),
                ('kilometrage', models.IntegerField(help_text='пробег', null=True)),
                ('color', models.CharField(blank=True, max_length=30, null=True)),
                ('gear_case', models.CharField(choices=[('автомат', 'автомат'), ('механика', 'механика')], default='механика', help_text='коробка передач', max_length=8)),
                ('engine', models.CharField(help_text='характеристики двигателя', max_length=30, null=True)),
                ('gear', models.CharField(choices=[('передний', 'передний'), ('задний', 'задний'), ('4х4', '4х4')], default='передний', help_text='Привод', max_length=8, null=True)),
                ('owner_count', models.IntegerField(null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('owner_info', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ad_person.person_information')),
            ],
        ),
    ]