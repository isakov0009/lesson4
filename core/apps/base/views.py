from django.shortcuts import render

# Create your views here.


def index(request):
    name ="tariel"
    age ="17"


    return render(request,"index.html", locals())