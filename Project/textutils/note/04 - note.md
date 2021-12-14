# How to get string from fronted to backend 
we make a textarea in our home page and the action goes to"/removepunc" and the method was "GET", so we need to make this 
- when any one hit enter then show the text in "/removepunc" end point
<br>

1. we need to get the text in backend
```py
# get the text from home
djText = req.GET.get("text", "default")
```
2. then return to frontend

```py
    return HttpResponse(djText)
```
3. all def

```py
def removePunc(req):
    # get the text from home
    djText = req.GET.get("text", "default")
    # show the text value
    return HttpResponse(djText)
```