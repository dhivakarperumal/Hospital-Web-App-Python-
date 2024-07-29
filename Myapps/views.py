from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from .forms import userCustomForm,BookapoinmentdForm,PatientDetailForm
from .models import Bookapoinment,PatientDetail


def home(request):
    if request.method == 'POST':
        form = BookapoinmentdForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/success')  
    else:
        form = BookapoinmentdForm()
    return render(request,'index.html',{'form': form})

def about(request):
    return render(request,'About/about.html')

def doctors(request):
    return render(request,'Doctors/doctors.html')

def treatment(request):
    return render(request,'Treatment/treatment.html')

def contact(request):
    return render(request,'Contact/contact.html')


def dhashboard(request):
    return render(request,'Loginandregister/dhashboard.html')

def register(request):
    form=userCustomForm()
    if request.method=='POST':
        form=userCustomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login_page')
    return render(request,'Loginandregister/register.html',{'form':form})

def login_page(request):
    if request.user.is_authenticated:
        redirect('/')
    else:
        if request.method=='POST':
            name=request.POST.get('username')
            pwd=request.POST.get('password')
            user=authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                return redirect('/login_page')
    return render(request,'Loginandregister/login.html')

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("/dhashboard")

def apoinmentbookdetails(request):
    datas=Bookapoinment.objects.all()
    return render(request,'ApoinmentbookDetails/abook.html',{'datas':datas})

def success(request):
    return render(request,'success.html')

def pationdetails(request):
    if request.method == 'POST':
        form = PatientDetailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/success')  
    else:
        form = PatientDetailForm()
    return render(request,'PasantsDetails/pations.html', {'form': form})

def datapations(request):
    pdatas=PatientDetail.objects.all()
    return render(request,'PasantsDetails/pationsdatas.html',{'pdatas':pdatas})

# ##################################BookAppoinments

def update(request,pk):
    item = get_object_or_404(Bookapoinment, pk=pk)
    if request.method == 'POST':
        form = BookapoinmentdForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookapoinmentdForm(instance=item)
    return render(request,'index.html', {'form': form})



def delete(request, pk):
    item = get_object_or_404(Bookapoinment, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('home')
    return render(request, 'delete.html', {'item': item})


################################################ PationsDeatails

def updates(request,pk):
    item = get_object_or_404(PatientDetail, pk=pk)
    if request.method == 'POST':
        form = PatientDetailForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('pationdetails')
    else:
        form = PatientDetailForm(instance=item)
    return render(request,'PasantsDetails/pations.html', {'form': form})


def deletes(request, pk):
    item = get_object_or_404(PatientDetail, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('pationdetails')
    return render(request, 'delete.html', {'item': item})

    