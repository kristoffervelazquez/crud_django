# companies/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Company
from .forms import CompanyForm

@login_required
def index(request):
    companies = Company.objects.all()
    return render(request, 'companies/index.html', {'companies': companies})

@login_required
def add_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('companies:index')
    else:
        form = CompanyForm()
    return render(request, 'companies/add_company.html', {'form': form})

@login_required
def edit_company(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('companies:index')
    else:
        form = CompanyForm(instance=company)
    return render(request, 'companies/edit_company.html', {'form': form})

@login_required
def delete_company(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == 'POST':
        company.delete()
        return redirect('companies:index')
    return render(request, 'companies/delete_company.html', {'company': company})
