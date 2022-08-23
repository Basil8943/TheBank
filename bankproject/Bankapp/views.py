from django.shortcuts import render
from applications.models import Branch
# Create your views here.

def home(request):
    branches=Branch.objects.all()
    return render(request,"home.html",{'branches':branches})

def detail(request,b_id):
    branch=Branch.objects.get(id=b_id)
    return render(request,"details.html",{'br':branch})

def kalpeta(request):
    branches = Branch.objects.all()
    return render(request,"branchinfo.html",{'br':branches})
def mananthvady(request):
    branches = Branch.objects.all()
    return render(request,"klptabranchinfo.html",{'brs':branches})
def bathery(request):
    branches = Branch.objects.all()
    return render(request,"branchinfo.html",{'br':branches})
def koduvally(request):
    branches = Branch.objects.all()
    return render(request,"branchinfo.html",{'br':branches})
def tmsry(request):
    branches = Branch.objects.all()
    return render(request,"branchinfo.html",{'br':branches})
def medc(request):
    branches = Branch.objects.all()
    return render(request,"branchinfo.html",{'br':branches})
def kaloor(request):
    branches = Branch.objects.all()
    return render(request,"branchinfo.html",{'br':branches})
def aluva(request):
    branches = Branch.objects.all()
    return render(request, "branchinfo.html", {'br': branches})
def kakkanad(request):
    branches = Branch.objects.all()
    return render(request, "branchinfo.html", {'br': branches})