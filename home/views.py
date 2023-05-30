from django.shortcuts import render
from .models import Cart,About,Article

def home(request):
    data = {
        "card":Cart.objects.all(),
        "about":About.objects.all(),
        "article":Article.objects.all()
    }
    return render(request,'index.html',data)
