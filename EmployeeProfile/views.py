from django.shortcuts import render,redirect
from .models import *
from .forms import *

def show_details(request,id):
    employees = EmployeeDetails.objects.get(id=id)
    print(employees.name)
    return render(request,"index.html",{'employees':employees})

def employee_list(request):  
    employees = EmployeeDetails.objects.all()  
    return render(request,"employee_list.html",{'employees':employees})

def create_profile(request):  
    if request.method == "POST":  
        form = EmployeeDetailsForm(request.POST, request.FILES)
        if form.is_valid():  
            form.save()
            return redirect('EmployeeProfile:employee_list')
      
    else:  
        form = EmployeeDetailsForm()  
    return render(request,'create_profile.html',{'form':form}) 


def edit_profile(request, id):  
    employee = EmployeeDetails.objects.get(id=id)  
    form = EmployeeDetailsForm(request.POST,request.FILES, instance = employee)  
    print(form)
    if form.is_valid():  
        form.save()  
        return redirect('EmployeeProfile:employee_list')  
    return render(request, 'edit.html', {'employee': employee}) 

def delete_profile(request, id):  
    employee = EmployeeDetails.objects.get(id=id)  
    employee.delete()  
    return redirect('EmployeeProfile:employee_list') 
