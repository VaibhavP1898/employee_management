from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm, EmployeeForm
from .models import Employee

def home(request):
    total_employees = Employee.objects.count()
    employees_on_leave = Employee.objects.filter(on_leave=True).count()
    return render(request, 'home.html', {'total_employees': total_employees, 'employees_on_leave': employees_on_leave})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def edit_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'edit_employee.html', {'form': form})

@login_required
def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('dashboard')
    return render(request, 'delete_employee.html', {'employee': employee})


# Create Employee view
def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new employee to the database
            return redirect('dashboard')  # Redirect to dashboard after creating the employee
    else:
        form = EmployeeForm()

    return render(request, 'create_employee.html', {'form': form})

# Dashboard view (show employee list)
def dashboard(request):
    employees = Employee.objects.all()
    total_employees = employees.count()
    employees_on_leave = employees.filter(on_leave=True).count()
    return render(request, 'dashboard.html', {
        'employees': employees,
        'total_employees': total_employees,
        'employees_on_leave': employees_on_leave
    })

