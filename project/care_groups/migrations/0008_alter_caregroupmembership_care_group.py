# Generated by Django 4.0 on 2022-01-08 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('care_groups', '0007_alter_caregroupmembership_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caregroupmembership',
            name='care_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to='care_groups.caregroup'),
        ),
    ]