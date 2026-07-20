from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Avg, Q
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Employee, Department
from .forms import EmployeeForm


@login_required
def dashboard_view(request):
    """Dashboard showing summary stats, charts, and recently added employees."""
    total_employees = Employee.objects.count()
    recent_employees = Employee.objects.all()[:5]

    # Department-wise counts (used for both the sidebar list and the
    # Chart.js bar/pie charts). Kept as an ordered dict so chart labels
    # and chart data line up positionally.
    department_counts = {
        label: Employee.objects.filter(department=code).count()
        for code, label in Department.choices
    }
    chart_labels = list(department_counts.keys())
    chart_data = list(department_counts.values())

    # Total Departments: number of distinct departments that actually
    # have at least one employee assigned (not just defined choices).
    total_departments = Employee.objects.values('department').distinct().count()

    # Employees Added This Month
    now = timezone.now()
    employees_this_month = Employee.objects.filter(
        created_at__year=now.year,
        created_at__month=now.month,
    ).count()

    # Average Salary (rounded to 2 decimal places, 0 if no employees yet)
    average_salary = Employee.objects.aggregate(avg_salary=Avg('salary'))['avg_salary'] or 0
    average_salary = round(average_salary, 2)

    context = {
        'total_employees': total_employees,
        'total_departments': total_departments,
        'employees_this_month': employees_this_month,
        'average_salary': average_salary,
        'recent_employees': recent_employees,
        'department_counts': department_counts,
        'chart_labels': chart_labels,
        'chart_data': chart_data,
    }
    return render(request, 'dashboard/dashboard.html', context)


@login_required
def employee_list_view(request):
    """Lists all employees with search by name or department and pagination."""
    query = request.GET.get('q', '').strip()
    employees = Employee.objects.all()

    if query:
        employees = employees.filter(
            Q(full_name__icontains=query) |
            Q(department__icontains=query) |
            Q(designation__icontains=query)
        )

    paginator = Paginator(employees, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'query': query,
        'total_results': employees.count(),
    }
    return render(request, 'employees/employee_list.html', context)


@login_required
def employee_detail_view(request, pk):
    """Shows full details of a single employee."""
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employees/employee_detail.html', {'employee': employee})


@login_required
def employee_create_view(request):
    """Handles adding a new employee."""
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            employee = form.save()
            messages.success(request, f'Employee "{employee.full_name}" was added successfully.')
            return redirect('employees:employee_detail', pk=employee.pk)
        messages.error(request, 'Please correct the errors below.')
    else:
        form = EmployeeForm()

    return render(request, 'employees/employee_form.html', {
        'form': form,
        'title': 'Add Employee',
        'button_label': 'Save Employee',
    })


@login_required
def employee_update_view(request, pk):
    """Handles updating an existing employee."""
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, f'Employee "{employee.full_name}" was updated successfully.')
            return redirect('employees:employee_detail', pk=employee.pk)
        messages.error(request, 'Please correct the errors below.')
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'employees/employee_form.html', {
        'form': form,
        'title': 'Update Employee',
        'button_label': 'Update Employee',
        'employee': employee,
    })


@login_required
def employee_delete_view(request, pk):
    """Handles deleting an employee after confirmation."""
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        name = employee.full_name
        employee.delete()
        messages.success(request, f'Employee "{name}" was deleted successfully.')
        return redirect('employees:employee_list')

    return render(request, 'employees/employee_confirm_delete.html', {'employee': employee})