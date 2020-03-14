# Getting Started with Django Web development

This tutorial focuses on create a web app with the Python framework Django. Lets get
started.

## Introduction

If you head to their website [https://www.djangoproject.com/](https://www.djangoproject.com/)
django is described as a "Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design". Lets install this framework so we can begin
developing applications.

## Installation

To intsall Django you need to have Python install on your computer. Then you can run the following command

```bash
python -m pip install Django
```

This will instlal Django on your computer.

## Creating a Project

Head to the root directroy where you want to create your project folder and run the following
command

```bash
django-admin startproject djangotutorial
```

Where `djangotutorial` can be replaced with the foldername of the project you want to get started.

[dj_installation.png]

### Creating an App

Now that you have a project started you can create a app within the project.
To do this run the following command

```bash
python manage.py startapp employees
```

Where `employees` can be changed to reflect the name of the app you want to create.

### Running your App

To run the app you just created you can use the following command

```bash
python manage.py runserver 8080
```

This will run a server you can access the link via `http://localhost:8080`.

[dj_install_complete.png]

## Creating a hello world app

Lets create our hello world app. To do this we need to create a route
an send some information from the server to the browswer.

In our `employees` directory we head to the `views.py` file. This is where we can
send information to the broswer. We create  a function called `hello`.

```python
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("Hello World")

```

We use the `HttpResponse` function to send **Hello World** to the browser.

In our `employees` directory we then create a file called `urls.py`. This will have
our urls paths for the app.

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.hello, name="hello")
]
```

In our main project `urls.py` we need to import our app `urls.py` file.

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('employees/', include('employees.urls'))
]
```

From above we do two main things. First we get the `include` function.

```python
from django.urls import path, include
```

Then we add a new path using `include` to add our `employees.urls` file.

```python
path('employees/', include('employees.urls'))
```

Now we can access this via `http://localhost:8080/employees/`. This path will direct to the
views function `hello` and it has a shortcut name as `hello`.

You can view the results below.

[dj_hello_world.png]

## Routing

In the above hello world example we learnt about routing. Lets dig a little deeper into
routing.

Lets create a new route called `list` in `urls.py`.

```python
urlpatterns = [
    path('', views.hello, name="hello"),
    path('list/', views.list, name="emp_list")
]
```

In our `views.py` we create the `list` function.

```python
def list(request):
    return HttpResponse("Employees list")
```

[dj_routing_list.png]

Lets crate one more route called `create`.

```python
path('create/', views.create, name="emp_create")
```

Now in our views we add the `create` function.

```python
def create(request):
    return HttpResponse("Create an employee")
```

So we can access this path via `http://localhost:8080/employees/create/`.

### Parameters

Lets get data from the url via parameters. First we create a route in
`urls.py`

```python
path('update/<id>/', views.update, name="emp_update")
```

Notice how we add the `<id>`. This is the placeholder for the paramter we will be
passing.

In the `view.py` we can create the update function.

```python
def update(request, id):
    return HttpResponse("Update an employee with id="+ id)
```

In the `update` function we pass the `id` parameter and we return it in the
`HttpResponse` function.

The results can be seen below.

[dj_routing_paramter.png]

Lets try another type of route. We create a simple route. 

```python
path('view/', views.view, name="emp_view")
```

Now in our `views.py` we add the `view` function

```python
def view(request):
    name = request.GET.get('name') or "n/a"
    return HttpResponse("Viewing the employee by username=" + name)
```

In the above example we are not using any placeholders. Instead
we are taking the `name` parameter if it exists directly from the
`GET` request.

The results are shown below.

With no name we can see

[dj_no_param.png]

With a name in the paramter we can see the results

[dj_name_param.png]

## Controllers and Rendering Views

Controllers in `Django` are called **views**. Views contain the logic of our application. 
Templates hold our `html` elements.

Lets create a `help` view with some `html` content

```python
def help(request):
    return HttpResponse("<h1>This is a help view</h1>")
```

[dj_help_view.png]

### Redirection

We can redirect our views using the `redirect` function.
First we import it from `django.shortcuts`

```python
from django.shortcuts import render, redirect
```

Then in our `help` function we can do

```python
def help(request):
    return redirect("hello")
```

Note **hello** is the shortcut name we gave the hello path as seen below here

```python
path('', views.hello, name="hello"),
```

The results can be seen below

[dj_route_redirect.gif]

### Getting POST Data

We can give POST data from the `request` object.
We can create a new route, we will call it api in the `urls.py` file

```python
path('api/', views.api, name="emp_api")
```

Now in the `views.py` file we create the function `api`.

```python
#import JsonResponse first at the top of the files
from django.http import HttpResponse, JsonResponse

def api(request):
    return JsonResponse({'name':'hello'})
```

Now we use postman to check out route `http://localhost:8080/employees/api`.

[dj_api_test.png]

Now lets try sending some `POST` data and getting it in our `view`. 
Lets modify  the `api` function to look like

```python
@csrf_exempt
def api(request):
    name = request.POST.get("name") or "n/a"
    email = request.POST.get("email") or "n/a"
    return JsonResponse(
        {'name':name,
        'email' :email}
        )
```

In the above sample we use `request.POST.get("param")` to retrieve the POST data.
The annotation `@csrf_exempt` is used to bypass `CSRF` protection. 

> Disable `CSRF` should not be dont in production site. Unless you know what your are doing.

To use the `@csrf_exempt` annotation we had to import it at the top of the `views.py` file.

```python
from django.views.decorators.csrf import csrf_exempt
```

Now using `Postman` we can test this route.

[dj_post_request.png]

### Rendering HTML content

Lets look at how we can render HTML files. First head to the `settings.py` file
in your base directory and make sure you app in in the list of installed applications.

[app_installed.png]

Once that is done we can create a templates directory inside our app directory.
It will take the format as shown below

```
/templates/employees/index.html
```

This means you may have to create two folders. One called `templates` and the other would be
the same as your app. In my case `employees`. Then you can create the `index.html` file and
add your `html` content.

```html
<h1>Hello World</h1>
<p>Welcome to wfTutorials</p>
```

Now in our views we create the `welcome` function.

```python
def welcome(request):
    return render(request, 'employees/index.html')
```

Pretty simple. When we head to `http://localhost:8080/employees/welcome/` we can see
the output.

[dj_render_html.png]

### Passing data to templates

Say we wanted to display some dynamic content we could pass data from our views to our
templates. To do this lets create an dictionary.

```python
data = {'pagetitle' : 'wfTutorials', 'header' : "Welcome to wftutorials"}
```

Now we will pass this to our template as the third arugment in the `render` function.

```python
def welcome(request):
    data = {'pagetitle' : 'wfTutorials', 'header' : "Welcome to wftutorials"}
    return render(request, 'employees/index.html', data)
```

Its that simple. Now in our template we can access these values using `{{ }}` double curly braces.

```html
<title>{{ pagetitle }}</title>
<h1>{{ header }}</h1>
<p>Welcome to wfTutorials</p>
```

The result is shown below.

[dj_passing_data.png]

## Working with templates

Lets see what we can do with templates. First we can primary template for
all or some of your templates. So we don't have to rewrite the same code over and over.

In our `templates` directory we create a file called `primary.html`. This is our primary template.

```html
<html>

<h1>This is the Primary layout</h1>


<div style="padding:15px; background: #fcfcfc; border: 1px solid red;">
 {% block content %}
 {% endblock %}
</div>

<footer>
<p> This is a template file footer</p>
</footer>
</html>
```

Take note of the following section with `{% block content %}`

```
 {% block content %}
 {% endblock %}
```

Other templates that extends the `primary.html` template will be placed with this content
block.

Now in our `views.py` we create our view

```python
def faq(request):
    return render(request, 'employees/faq.html')
```

Now lets add our `html` to `faq.html`

```html
{% extends "primary.html" %}

{% block content %}

<h4>This is the faq template</h4>
<p>Some text goes here</p>

{% endblock %}
```

In our `faq.html` we first extend our view using the `primary.html` layout. Then we
create a block content section.

The results can be seen below.

[dj_primary_layout.png]

### Multiple Content Blocks

You can add multiple content blocks in your layouts if you wish.
Below we change `primary.html` to add a second `content2` block.

```html
<html>

<h1>This is the Primary layout</h1>


<div style="padding:15px; background: #fcfcfc; border: 1px solid red;">
 {% block content %}
 {% endblock %}
</div>

<div>
{% block content2 %}
 {% endblock %}
</div>
<footer>
<p> This is a template file footer</p>
</footer>
</html>
```

Then in our `faq.html` template we can add more data to this content block.


```html
{% extends "primary.html" %}

{% block content %}

<h4>This is the faq template</h4>
<p>Some text goes here</p>

{% endblock %}


{% block content2 %}

<h4>Second Content Block</h4>
<p>Some text goes here</p>

{% endblock %}
```

The results are shown below.

[dj_multiple_content_blocks.png]

### Conditionals

We can use conditionals within our templates lets see how. In our `faq.html` template we 
add the following code

```html
{% if show %}
<p>Some text goes here</p>
{% else %}
<p>No text goes here</p>
{% endif %}
```

Above if `show` we output a certain type of text else we output a default
text.

In our `views.py` we can send the data to our template

```python
def faq(request):
    data = {'show': None}
    return render(request, 'employees/faq.html', data)
```

[dj_conditional_layout.png]

### Working with Loops

We can use loops within our templates. Lets see how. In our `faq.html` we can add

```html
<ul>
{% for dog in dogs %}
    <li> {{ dog }} </li>
{%  endfor %}
</ul>
```

We are using the expression `{% for x in y %}` where `y` is the list and `x` is the 
a element in the list. We can use the double curly braces to access the element.

In our view we can see how we pass this data.

```python
def faq(request):
    myDogs = ["bobby", "pepper", "sugar"]
    data = {'show': None, 'dogs': myDogs}
    return render(request, 'employees/faq.html', data)
```

The results is shown below.

[dj_layouts_loops.png]

### Using external assets

We can work with external assets like css frameworks by first create a static folder in our
employees directory. Within the static folder we create a employees directory and within that
folder we add bootstrap.css. Check the picture below to get an idea.

[dj_static_path.png]

Once we have our `bootstrap.css` file we can create a new layout to use. We call it
the `secondary.html`.

```html
{% load staticfiles %}
<html>

<head>
  <link href="{% static 'employees/bootstrap.css' %}" rel="stylesheet">
</head>

<body>
{% block content %}

{% endblock %}
</body>

</html>
```

Using `{% load staticfiles %}` loads the files from the directory so we can access them.
We can then link to them as shown below

```html
<link href="{% static 'employees/bootstrap.css' %}" rel="stylesheet">
```

Now in our views we create a new function.

```python
def help(request):
    return render(request, 'employees/help.html')
```

In in our `help.html` we add some bootstrap structures and ofcourse extend the `secondary.html` layout.

```html
{% extends "secondary.html" %}


{% block content %}

<div class="container">

<div class="row">

    <div class="col">
    <h1>Help view</h1>
        <div class="alert alert-success">
        A simple primary alert—check it out!
        </div>
        <div class="alert alert-warning">
        A simple secondary alert—check it out!
        </div>

        <ul class="list-group">
        <li class="list-group-item">Cras justo odio</li>
        <li class="list-group-item">Dapibus ac facilisis in</li>
        <li class="list-group-item">Morbi leo risus</li>
        <li class="list-group-item">Porta ac consectetur ac</li>
        <li class="list-group-item">Vestibulum at eros</li>
        </ul>
    </div>

</div>

</div>

{% endblock %}
```

The results we can see below.

[dj_static_files.png]

## Models, Database and Migrations

Lets see how we can work with the database in Django. First lets create a model. Head to the `models.py` file and start creating your model as a class.

In the `models.py` file add the code below

```python
class Employees(models.Model):
    firstname = models.CharField(max_length=125)
    lastname = models.CharField(max_length=125)
    department = models.CharField(max_length=50)
    employeeid = models.IntegerField()
    email = models.CharField(max_length=65)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
```

This is our model. We will be created an employees table with the following field
names. You can view fmore field types [here](https://docs.djangoproject.com/en/3.0/ref/models/fields/#model-field-types).

Now when you are finish adjusting your model you can run the following command

```bash
python manage.py migrate
```

[dj_run_migrations.png]

Once this is done you would have your models created in your database. 

### Using an MySQL Database

Django uses sqlite to start but you could always change this. In your `settings.py` file you will see

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

You just need to update this dictionary to the right configuration for your MySQL or
any other database. Check out [this](https://stackoverflow.com/questions/19189813/setting-django-up-to-use-mysql) stackoverflow question to learn more.

### Saving data to your model

Lets see how we can save data to your models. First you need and
sqlite browswer. Check one out [here](https://sqlitebrowser.org/).

Then open your `db.sqlite3` database with it to see an overview of the records you created
so far.

[dj_sqlite_db.png]

Now lets create a view to save our data. 

```python
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
```

In the above code we create the `saveemployee` function. It creates and model

```python
emp = Employees()
```

then it adds some default values and uses `emp.save()` to save the data.

We use `try` and `except` to test for errors.

In our `urls.py` we can add this new route

```python
path('save/',views.saveemployee, name="emp_save")
```

Now when we test this we can see the results.

[dj_save_employee.png]

If you have any errors they will be displayed.

[dj_save_employee_error.png]

You can view the insert data using the sqlite browswer.

[dj_inserted_data.png]

### Displaying data from your model

We can find an row from the database using `objects`. In our new view `display`

```python
def display(request):
    emp = Employees.objects.get(pk=1) # get the employee object
    return HttpResponse("Employee name is: " + emp.firstname +  " " + emp.lastname)
```

[dj_view_model_data.png]

#### Getting an object by email

We can do the same thing for any other attribute of the table. For eg the `email`

```python
def display(request):
    emp = Employees.objects.get(email="james@gmail.com")
    return HttpResponse("Employee name is: " + emp.firstname +  " " + emp.lastname)
```

#### Deleting an object

We can delete an object using `model.delete()` lets see how

```python
def remove(request):
    emp = Employees.objects.get(email="james@gmail.com")
    try:
        emp.delete()
        return HttpResponse("object deleted")
    except Exception as e:
        return HttpResponse(e)
```

We create a new view called `remove` that calls the delete function on
`emp.delete()`.

#### Updating an object

We can change the data of an object and save it. This will update the object.

```python
def update(request):
    emp = Employees.objects.get(pk=1)
    emp.age = "27"
    try:
        emp.save()
        return HttpResponse("object age updated to " + emp.age)
    except Exception as e:
        return HttpResponse(e)
```

[dj_update_model.png]

## Working with Forms

Using forms we have a more intutitve way of woring with our models. It creates
an abstraction so we do need to work with models directely. Lets see how.
In our employees directory create a file called `forms.py`.

Add the imports that we need

```python
from django.forms import ModelForm
from .models import Employees, Departments
```

Now we can get started created our forms.

In `forms.py` we add the following code

```python
class EmployeeForm(ModelForm):
    class Meta:
        model = Employees
        exclude = ('created_at','id')

class DepartmentForm(ModelForm):
    class Meta:
        model = Departments
        fields = ('name', 'code')
```

Using the `Meta` class you need to either add an `exclude` or `fields` option.
Exclue says what attributes to remove from the form. With fields you choose
what options you want to be shown in the form.

Now in our `views.py` we import our forms.

```python
from employees.forms import EmployeeForm, DepartmentForm
```

then we create a view for display the form.

```python
def create(request):
    empForm = EmployeeForm()
    return render(request,'employees/create.html', {'form':empForm})
```

In our `create.html` we can render our form using the `secondary.html` layout so we can
use bootstrap

```html
{% extends "secondary.html" %}

{% block content %}
<div class="container">
<h1>Create an Employee</h1>
<form action="{% url 'emp_create' %}" method="post">
  {% csrf_token %}
  {{ form.as_p }}
        <button type="submit" class="btn btn-primary">Submit</button>
</form>
</div>

{% endblock %}
```

Of important note is `form.as_p` we could have just used `form` but using `form.as_p` wraps
each element in a `p` element. Learn more [here](https://docs.djangoproject.com/en/3.0/topics/forms/).

Some other things to note

* The `url "emp_create"` creates a url from the shorthand name
* The `csrf_token` line is required to submit the form.
* If you are not using layout templates you dont need to add the `extends` or `block content` sections.

The results is shown below

[dj_create_employee_form.png]


### Saving form data to database

Now that we have our form up and running. We create going to submit the form and save
our data.

We modify our `views.py` function called `create` to accept a post request.

```python
def create(request):
    if request.method == "POST":
        empForm = EmployeeForm(data=request.POST)
        if empForm.is_valid():
            empForm.save()
        return HttpResponse("Employee saved")
    else:
        empForm = EmployeeForm()
        return render(request,'employees/create.html', {'form':empForm})
```

Above if the `request.method` is post we load the data from the request into our `EmployeeForm`.
Then if the form is valid we save it. Otherwise we display the form.

[dj_submit_form.png]

The results can be seen from the DB browser.

[dj_form_submit_results.png]


### Updating data using forms

Lets see how we can update our database using a form. First we update our `update` view in
`views.py`.

```python
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
```

Lets review this code. First note we added the `id`

```python
def update(request, id):
```

in the function call. This means this is required. Of course our route in `urls.py` reflects this.

```python
path('update/<id>/', views.update, name="emp_update"),
```

The first section in the `update` function contains an `if` statement check for
a `POST` request. We the load the employee model and then we add the POST data
and the model in the `EmployeeForm` constructure.

```python
emp = Employees.objects.get(pk=id)
empForm = EmployeeForm(request.POST, instance=emp)
```

This way the form knows its needs to update and not create. Learn more [here](https://docs.djangoproject.com/en/3.0/topics/forms/modelforms/#the-save-method). The rest is **rote**. Just
check for validation and save. We return a redirect using the `request.path`. 

If there is not `POST` request we just load the employee form from the employee model and display
the current data in the model.

```python
emp = Employees.objects.get(pk=id)
empForm =  EmployeeForm(instance=emp)
```

In our `update.html` template note the `request.path` in the form action paramter.

```html
<form action="{{ request.path }}" method="post">
  {% csrf_token %}
  {{ form.as_p }}
        <button type="submit" class="btn btn-primary">Submit</button>
</form>
```

We use `request.path` so we can main the `id` parameter when we submit the form.

So we can see the results below.

[dj_update_form_database.gif]

## Authentication and Access Control

TO get started with authentication we need to have a login view. With Django this process
is made quite easy. Lets head to our `urls.py` file. First we need to import some views.
At the top add this code

```python
from django.contrib.auth.views import LoginView
```

Above we import the `LoginView` from django. Now we can add path in our `urls.py` file add the following lines

```python
path('login/',LoginView.as_view(template_name="employees/login.html"),name="emp_login")
```

Above we add the `login` path and we direct this path to the `LoginView`. We have to provide
a `template_name` in the `LoginView.as_view()` function. We choose `login.html` lets create
this.

```html
<h1>Login Page</h1>
```

Our `login.html` file is simple for now. Lets test this and see what happens

>Note we did not add any views in `views.py` we did all this in `urls.py` file.

[dj_simple_login_view.png]

### Authenticating a user

Lets finish the login view. In `login.html` add the following content.

```html
<h1>Login Page</h1>
<form role='form' action="{% url 'emp_login' %}" method="post">
    {% csrf_token %}
    <p>Please Login</p>
    {{ form.as_p}}
    <button type="submit" class="btn btn-success">Sign in</button>
</form>
<br><br>
```

We have access to a login form in this `login.html` template so we display it. The `post` url
is our login url. 

[dj_login_view_final.png]

Currently we have no users so the form will no work as it should. But
it already comes with validation.

[dj_login_attempt.png]

### Loging out a user

Lets work on logging out users. We can head to the `views.py` file and create a new
view.

```python
def logout_view(request):
    logout(request)
    return HttpResponse("User logged out")
```

As seen above we have `logout_view`. We are using a `logout` function that we imported.

```python
from django.contrib.auth import logout
```

We need to now add the `url` path in the `urls.py`

```python
path('logout/',views.logout_view,name="emp_logout")
```

[dj_logout_view.png]



