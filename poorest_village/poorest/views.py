from django.shortcuts import render
from .models import User,Government,School,Infrastructure,Center,Village,Medical,Holly_places
# Create your views here.

def index(request):
   
    if request.method == "POST":
         gov=request.POST["gov"]
         center=request.POST["center"]
         g=Government.objects.get(name=gov) 
         c=Center.objects.get(government=g.id)
         v=Village.objects.filter(center=c.id)
         school=School.objects.filter(village=v[0].id)
         print("-----------------index---------------")
         print(v)
         print(school)
     #     print(result.id)
     #     village=Village.objects.get(government=result.id)
     #     print(village)
     #     schools=School.objects.filter(government=result.id)
     #     print(schools[0].id,"school")
     #     hospitals=Medical.objects.filter(government=result.id)
         return render(request, "poorest/results.html")
    return render(request, "poorest/index.html")


