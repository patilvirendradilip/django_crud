from django.shortcuts import render
from .forms import StudentForm
from django.http import HttpResponse,HttpResponseRedirect
from .models import StudentModel
from django.db.models.query import QuerySet
# Create your views here.


def home_page(r):
    form = StudentForm()
    my_dict = {'form': form}
    if r.method == 'POST':
        form = StudentForm(r.POST)
        # print(form)
        if form.is_valid():
            print(form.cleaned_data)
            form.save(commit=True)
            return HttpResponse("<h1>Your Data is save successfully in Database !!!!!<br><a href='/student/show'>Ok</a></h1>")
        else:
            return HttpResponse("<h1>Error  !!!!!</h1>")
    return render(r, 'home/index.html', context=my_dict)


def show_page(r):
    data = StudentModel.objects.all()
    #data = StudentModel.objects.filter(id__exact=3) #| StudentModel.objects.filter(id__gt=4)
    #data = StudentModel.objects.filter(id__in=[3,5,6,7])
    #data = StudentModel.objects.filter(id__in=[3,5,6,7]) & StudentModel.objects.filter(email__endswith='gmail.com')
    #data = StudentModel.objects.all().order_by('name')#[2:3]
    # print(data, type(data))
    my_dict = {'data': data}
    return render(r, 'home/show.html', context=my_dict)


def home(r):
    return render(r, 'home/home.html')


def delete_page(r, id):
    data = StudentModel.objects.filter(id__exact=id)
    data.delete()
    return HttpResponseRedirect('/student/show')


def update_page(r, id):
    data = StudentModel.objects.get(id=id)
    if r.method == 'POST':
        form = StudentForm(r.POST, instance=data)
        if form.is_valid():
            print(form.cleaned_data)
            form.save(commit=True)
            return HttpResponse("<h1>Your Data is Updated successfully in Database !!!!!<br><a href='/student/show'>Ok</a></h1>")
        else:
            return HttpResponse("<h1>Error in Update !!!!!<br><a href='/student/show'>Ok</a></h1>")
    return render(r, 'home/update.html', context={'data': data})
