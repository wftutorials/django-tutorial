from django.forms import ModelForm
from .models import Employees, Departments

class EmployeeForm(ModelForm):
    class Meta:
        model = Employees
        exclude = ('created_at','id')

class DepartmentForm(ModelForm):
    class Meta:
        model = Departments
        fields = ('name', 'code')