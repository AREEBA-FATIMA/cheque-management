# Generated by Django 4.2.13 on 2025-07-16 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cheque', '0003_cheque_other_responsible_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cheque',
            name='other_responsible_name',
        ),
        migrations.RemoveField(
            model_name='cheque',
            name='received_by',
        ),
        migrations.RemoveField(
            model_name='cheque',
            name='responsible_person',
        ),
        migrations.AddField(
            model_name='cheque',
            name='received_by_cnic',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Received By CNIC'),
        ),
        migrations.AddField(
            model_name='cheque',
            name='received_by_contact',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Received By Contact'),
        ),
        migrations.AddField(
            model_name='cheque',
            name='received_by_name',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Received By Name'),
        ),
        migrations.AddField(
            model_name='cheque',
            name='received_by_project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='received_projects', to='cheque.project', verbose_name='Received By Project'),
        ),
        migrations.AddField(
            model_name='cheque',
            name='responsible_person_cnic',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Responsible Person CNIC'),
        ),
        migrations.AddField(
            model_name='cheque',
            name='responsible_person_contact',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Responsible Person Contact'),
        ),
        migrations.AddField(
            model_name='cheque',
            name='responsible_person_name',
            field=models.CharField(default='', max_length=100, verbose_name='Responsible Person Name'),
        ),
        migrations.AddField(
            model_name='cheque',
            name='responsible_person_project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='responsible_projects', to='cheque.project', verbose_name="Responsible Person's Project"),
        ),
    ]
