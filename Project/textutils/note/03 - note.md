# template trick
we can make a **base.html** template. Based on the template we can make many copy.

### base.html
```html
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}{% endblock title %}</title>
    <!-- CSS only -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
</head>
<body>
   {% block body %}{% endblock body %} 
</body>
<!-- JavaScript Bundle with Popper -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</html>
```
- in the title tag we use the block keyword for template another thing in there 
- and also in the body we use same trick

<br>

now based on the base.html template we can make so many template.

```html
<!-- index.html -->
{% extends 'base.html' %}
{% block title %}Home{% endblock title %}
{% block body %}
<h1>Home</h1>
<h4>enter your text here:
</h4>
<form action="">
  <textarea name="text" id="text" cols="70" rows="10"></textarea>
  <br>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
{% endblock body %}
```
- first we need to extends the base.html, to our index.html
- then use block keyword for title and write your own word
- same thing in the body
<br>

we can make many html page based on the **base.html** template