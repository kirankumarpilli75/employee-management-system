from django.db import models
from django.core.validators import RegexValidator, MinValueValidator
from django.urls import reverse


class Department(models.TextChoices):
    HR = 'HR', 'Human Resources'
    ENGINEERING = 'ENG', 'Engineering'
    SALES = 'SALES', 'Sales'
    MARKETING = 'MKT', 'Marketing'
    FINANCE = 'FIN', 'Finance'
    OPERATIONS = 'OPS', 'Operations'
    SUPPORT = 'SUP', 'Customer Support'


phone_validator = RegexValidator(
    regex=r'^\+?\d{7,15}$',
    message="Phone number must contain 7-15 digits and may start with '+'."
)


class Employee(models.Model):
    """Represents a single employee record."""

    # Employee ID is the auto-incrementing primary key (id) — exposed as
    # a friendly, zero-padded "EMP-0001" style code via the employee_code property.
    full_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, validators=[phone_validator])
    department = models.CharField(max_length=10, choices=Department.choices)
    designation = models.CharField(max_length=100)
    salary = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    date_of_joining = models.DateField()
    profile_photo = models.ImageField(
        upload_to='profile_photos/',
        blank=True,
        null=True,
        help_text='Optional. Square images look best.'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.full_name} ({self.get_department_display()})'

    @property
    def employee_code(self):
        """A human-friendly employee ID, e.g. EMP-0001."""
        return f'EMP-{self.id:04d}'

    def get_absolute_url(self):
        return reverse('employees:employee_detail', kwargs={'pk': self.pk})
