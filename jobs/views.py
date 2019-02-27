from django.shortcuts import render,get_object_or_404
from .models import Job
from .forms import ContactModelForm

from django.http import HttpResponseRedirect
from .models import ContactUser
from django.urls import reverse
# Create your views here.

def home(request):
    queryset = Job.objects.all()

    if request.method == 'POST':
        user         = request.POST['user']
        email        = request.POST['email']
        content      = request.POST['content']

        contact = ContactUser(user=user,email=email,content=content)
        contact.save()
        return HttpResponseRedirect(reverse('home') )
        print('Its working')

    context = {
        'jobs': queryset,
    }
    return render(request,'jobs/home.html',context)


# def contact(request,pk):
#     contact_inst = get_object_or_404(ContactUser, pk=pk)

#     # If this is a POST request then process the Form data
#     if request.method == 'POST':

#         # Create a form instance and populate it with data from the request (binding):
#         form = ContactModelForm(request.POST)

#         # Check if the form is valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
#             contact_inst.username = form.cleaned_data['username']
#             contact_inst.save()

#             # redirect to a new URL:
#             return HttpResponseRedirect(reverse('home') )
