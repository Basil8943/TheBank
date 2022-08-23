from django.shortcuts import render, redirect
from .forms import ApplicationForm
from .models import Application, Branch, District


# Create your views here.
def create(request):
    form = ApplicationForm
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, "application.html",{'form':form})


def load_branches(request):
    district_id = request.GET.get('district_id')
    branches = Branch.objects.filter(district_id=district_id).all()
    return render(request, 'branches.html', {'branches': branches})
    # return JsonResponse(list(branches.values('id', 'name')), safe=False)
