from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from employees.models import Employees
from employees.forms import EmployeeForm, DepartmentForm
from django.contrib.auth import logout

# Create your views here.
def hello(request):
    return HttpResponse("Hello World")

def list(request):
    return HttpResponse("Employees list")

'''
def create(request):
    return HttpResponse("Create an employee")
'''

'''
def update(request, id):
    return HttpResponse("Update an employee with id="+ id)
'''

def view(request):
    name = request.GET.get('name') or "n/a"
    return HttpResponse("Viewing the employee by username=" + name)


@csrf_exempt
def api(request):
    name = request.POST.get("name") or "n/a"
    email = request.POST.get("email") or "n/a"
    return JsonResponse(
        {'name':name,
        'email' :email}
        )

def welcome(request):
    data = {'pagetitle' : 'wfTutorials', 'header' : "Welcome to wftutorials"}
    return render(request, 'employees/index.html', data)

def faq(request):
    myDogs = ["bobby", "pepper", "sugar"]
    data = {'show': None, 'dogs': myDogs}
    return render(request, 'employees/faq.html', data)

def help(request):
    return render(request, 'employees/help.html')


def saveemployee(request):
    emp = Employees()
    emp.firstname = "Wynton"
    emp.lastname = "frannklin"
    emp.email = "wf@gmail.com"
    emp.department = "IT"
    emp.age = "25"
    emp.employeeid = "005"
    try:
        emp.save()
        return HttpResponse("Employee saved")
    except Exception as e:
        return HttpResponse(e)


''' Object by primary key
def display(request):
    emp = Employees.objects.get(pk=1)
    return HttpResponse("Employee name is: " + emp.firstname +  " " + emp.lastname)
'''

def display(request):
    emp = Employees.objects.get(email="james@gmail.com")
    return HttpResponse("Employee name is: " + emp.firstname +  " " + emp.lastname)

def remove(request):
    emp = Employees.objects.get(email="james@gmail.com")
    try:
        emp.delete()
        return HttpResponse("object deleted")
    except Exception as e:
        return HttpResponse(e)

'''
def update(request):
    emp = Employees.objects.get(pk=1)
    emp.age = "27"
    try:
        emp.save()
        return HttpResponse("object age updated to " + emp.age)
    except Exception as e:
        return HttpResponse(e)
'''

def create(request):
    if request.method == "POST":
        empForm = EmployeeForm(data=request.POST)
        if empForm.is_valid():
            empForm.save()
        return HttpResponse("Employee saved")
    else:
        empForm = EmployeeForm()
        return render(request,'employees/create.html', {'form':empForm})


def update(request, id):
    if request.method == "POST":
        emp = Employees.objects.get(pk=id)
        empForm = EmployeeForm(request.POST, instance=emp)
        if empForm.is_valid():
            empForm.save()
            return redirect(request.path)
    else:
        emp = Employees.objects.get(pk=id)
        empForm =  EmployeeForm(instance=emp)
        return render(request, 'employees/update.html',{'form':empForm})

def logout_view(request):
    logout(request)
    return HttpResponse("User logged out")