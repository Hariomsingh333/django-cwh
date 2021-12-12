# Django Template

- first go settings.py
- find Templates array(list)
- see the "DIRS" is blank so fill with it ['template']

```py
# before
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

```

```py
#after

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

```

we just say to django: _"we have a folder called templates so go and see"_

- then create a folder called templates
- where the manage.py exist create there the templates folder
- in template create a file called index.html

  <br>

then go to views.py and import render

```py
# views.py
from django.shortcuts import render
```

- render is a python method that take argument called **req** or _request_
- them specify the template file name

```py
# html page
def index(req):
    return render(req, "index.html")
```
