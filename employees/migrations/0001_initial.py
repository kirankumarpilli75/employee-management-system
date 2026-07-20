import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(
                    max_length=15,
                    validators=[django.core.validators.RegexValidator(
                        message="Phone number must contain 7-15 digits and may start with '+'.",
                        regex='^\\+?\\d{7,15}$'
                    )]
                )),
                ('department', models.CharField(choices=[
                    ('HR', 'Human Resources'),
                    ('ENG', 'Engineering'),
                    ('SALES', 'Sales'),
                    ('MKT', 'Marketing'),
                    ('FIN', 'Finance'),
                    ('OPS', 'Operations'),
                    ('SUP', 'Customer Support'),
                ], max_length=10)),
                ('designation', models.CharField(max_length=100)),
                ('salary', models.DecimalField(
                    decimal_places=2,
                    max_digits=10,
                    validators=[django.core.validators.MinValueValidator(0)]
                )),
                ('date_of_joining', models.DateField()),
                ('profile_photo', models.ImageField(
                    blank=True,
                    help_text='Optional. Square images look best.',
                    null=True,
                    upload_to='profile_photos/'
                )),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
