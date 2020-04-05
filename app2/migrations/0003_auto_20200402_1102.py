# Generated by Django 3.0.5 on 2020-04-02 05:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0002_appointment_installmenttype_maindept_maindesignation_scale_staff_stafftype_subdept_subdesignation_un'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank_Name',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(blank=True, max_length=20, null=True, unique=True)),
            ],
            options={
                'db_table': 'BANK_NAME',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(blank=True, max_length=20, null=True, unique=True)),
            ],
            options={
                'db_table': 'DEPARTMENT1',
            },
        ),
        migrations.CreateModel(
            name='Designation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(blank=True, max_length=20, null=True, unique=True)),
            ],
            options={
                'db_table': 'DESIGNATION1',
            },
        ),
        migrations.CreateModel(
            name='Designation_Nature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(blank=True, max_length=20, null=True, unique=True)),
            ],
            options={
                'db_table': 'DESIGNATION_NATURE',
            },
        ),
        migrations.CreateModel(
            name='EmployeeInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_NUMBER', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('SEQUENCE_NUMBER', models.CharField(blank=True, max_length=50, null=True)),
                ('TITLE', models.CharField(blank=True, max_length=50, null=True)),
                ('FIRST_NAME', models.CharField(blank=True, max_length=50, null=True)),
                ('MIDDLE_NAME', models.CharField(blank=True, max_length=50, null=True)),
                ('LAST_NAME', models.CharField(blank=True, max_length=50, null=True)),
                ('FATHER_NAME', models.CharField(blank=True, max_length=50, null=True)),
                ('INCREMENT_DATE', models.DateField()),
                ('DATE_OF_BIRTH', models.DateField()),
                ('DATE_OF_JOINING', models.DateField()),
                ('DATE_OF_RETIREMENT', models.DateField()),
                ('DESIGNATION_NAME', models.CharField(blank=True, max_length=50, null=True)),
                ('GENDER', models.CharField(blank=True, max_length=50, null=True)),
                ('TA', models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=False, null=True)),
                ('PT', models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=True, max_length=10, null=True)),
                ('QUARTER', models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=True, null=True)),
                ('RENT_FREE', models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=True, null=True)),
                ('QUARTER_ADDRESS', models.CharField(blank=True, max_length=50, null=True)),
                ('HANDICAP', models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=True, null=True)),
                ('SENIOR_CITIZEN', models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=True, null=True)),
                ('DESIGNATION', models.CharField(blank=True, max_length=50, null=True)),
                ('DEPARTMENT', models.CharField(blank=True, max_length=50, null=True)),
                ('STAFF_TYPE', models.CharField(blank=True, max_length=50, null=True)),
                ('APPOINTMENT', models.CharField(blank=True, max_length=50, null=True)),
                ('VACATIONAL', models.CharField(blank=True, max_length=50, null=True)),
                ('BANK_NAME', models.CharField(blank=True, max_length=50, null=True)),
                ('BANK_ACCOUNT_NUMBER', models.CharField(blank=True, max_length=50, validators=[django.core.validators.RegexValidator(message='INVALID ACCOUNT NUMBER', regex='^\\d{9,18}$')])),
                ('PF_NUMBER', models.CharField(blank=True, max_length=50, unique=True, validators=[django.core.validators.RegexValidator(message='INVALID PF NUMBER', regex='^[A-Z]{2}/[A-Z]{3}/\\d{5}/\\d{3}/\\d{7}$')])),
                ('PRAN_NUMBER', models.CharField(blank=True, max_length=50, unique=True, validators=[django.core.validators.RegexValidator(message='INVALID PF NUMBER', regex='^\\d{12,12}$')])),
                ('PAN_NUMBER', models.CharField(blank=True, max_length=50, unique=True, validators=[django.core.validators.RegexValidator(message='INVALID PAN NUMBER', regex='^([a-zA-Z]){5}([0-9]){4}([a-zA-Z]){1}?$')])),
                ('UNDER', models.CharField(blank=True, max_length=50, null=True)),
                ('LEVEL', models.CharField(blank=True, max_length=50, null=True)),
                ('BASIC', models.IntegerField()),
                ('PAY_STATUS', models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], default=False, null=True)),
                ('RULE', models.CharField(blank=True, max_length=50, null=True)),
                ('REMARK', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'EmployeeInformation',
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(blank=True, max_length=20, null=True, unique=True)),
            ],
            options={
                'db_table': 'GENDER',
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(blank=True, max_length=20, null=True, unique=True)),
            ],
            options={
                'db_table': 'LEVEL',
            },
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(blank=True, max_length=20, null=True, unique=True)),
            ],
            options={
                'db_table': 'RULE',
            },
        ),
        migrations.CreateModel(
            name='Staff_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(blank=True, max_length=20, null=True, unique=True)),
            ],
            options={
                'db_table': 'STAFF_TYPE',
            },
        ),
        migrations.CreateModel(
            name='Under',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(blank=True, max_length=20, null=True, unique=True)),
            ],
            options={
                'db_table': 'UNDER',
            },
        ),
        migrations.CreateModel(
            name='Vacational',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(blank=True, max_length=20, null=True, unique=True)),
            ],
            options={
                'db_table': 'VACATIONAL',
            },
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='APPOINT_NAME',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='APPOINT_NO',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='D1',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='D10',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='D11',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='D12',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='D13',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='D14',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='D15',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='D16',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='D17',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='D18',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='D19',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='D2',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='D20',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='D21',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='D22',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='D23',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='D24',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='D25',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='D26',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='D27',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='D28',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='D29',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='D3',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='D30',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='D4',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='D5',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='D6',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='D7',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='D8',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='D9',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='l1',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='l10',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='l11',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='l12',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='l13',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='l14',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='l15',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='l2',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='l3',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='l4',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='l5',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='l6',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='l7',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='l8',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='l9',
        ),
        migrations.AddField(
            model_name='appointment',
            name='NAME',
            field=models.CharField(blank=True, max_length=20, null=True, unique=True),
        ),
        migrations.AlterModelTable(
            name='appointment',
            table='APPOINTMENT',
        ),
    ]