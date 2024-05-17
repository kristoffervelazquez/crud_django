from django.shortcuts import render, redirect, get_object_or_404

from contacts.models import Contact
from .forms import ContactForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    query = request.GET.get('q')
    if query:
        contacts = Contact.objects.filter(name__icontains=query)
    else:
        contacts = Contact.objects.all().order_by('id')
    return render(request, 'contacts/index.html', {'contacts': contacts})

@login_required
def add_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = ContactForm()
    return render(request, 'contacts/add_contact.html', {"form": form})

@login_required
def edit_contact(request, id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/edit_contact.html', {"form": form})

@login_required
def delete_contact(request, id):
    contact = get_object_or_404(Contact, id=id)
    if request.method == 'POST':
        contact.delete()
        return redirect('index')
    return render(request, 'contacts/delete_contact.html', {'contact': contact})


