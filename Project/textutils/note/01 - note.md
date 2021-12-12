## create views.py

first go to your project and create a views.py file, and comment it

```py
# i made this file called views.py
```

## what is urls.py and views.py

### urls.py

urls.py is a python file that represent our routes like "home route" etc

### views.py

views.py is also a python file that contain logical function

## import views in urls

first we need to import the views file in our urls to use the views

```py
from . import views

```

## Create our home route

```py
# urlpatterns = [
#     path("admin/", admin.site.urls),
#     path("", views.index, name="index")
# ]

# under the urlpatterns
    path("", views.index, name="index")
```

when our path hit the "" domain or home route, python send to views file and use the index function that why we use the <code>views.index</code> and we need to specify the name of our route <code>name="index"</code>

## return "hello world" to home route using the views file

we need to create a file called index, because we are specify the name index in url

- we need to send any thing using the http method so we have a method called httpResponse,
- first we need to import HttpsResponse
- create the function using the req argument
- in every views function we pass an argument called request or _req_
- return anything using the HttpResponse method **HttpResponse()**

```py

# i create this file - hari om
from django.http import HttpResponse

def index(req):
    return HttpResponse("hello world")

```

## create about route or endpoint

```py
# urls.py
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("about", views.about, name="about"),
]
```

```py
# views.py
# in views every function take a argument called req or request
def about(req):
    return HttpResponse("this is about page")
```
