from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    """Form used for both creating and updating an Employee."""

    class Meta:
        model = Employee
        fields = [
            'full_name',
            'email',
            'phone_number',
            'department',
            'designation',
            'salary',
            'date_of_joining',
            'profile_photo',
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Priya Sharma',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. priya.sharma@example.com',
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. +919876543210',
            }),
            'department': forms.Select(attrs={
                'class': 'form-select',
            }),
            'designation': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Software Engineer',
            }),
            'salary': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. 55000.00',
                'step': '0.01',
                'min': '0',
            }),
            'date_of_joining': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'profile_photo': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
        }

    def clean_full_name(self):
        full_name = self.cleaned_data['full_name'].strip()
        if len(full_name) < 3:
            raise forms.ValidationError('Full name must be at least 3 characters long.')
        return full_name

    def clean_salary(self):
        salary = self.cleaned_data['salary']
        if salary <= 0:
            raise forms.ValidationError('Salary must be greater than zero.')
        return salary
    
    
