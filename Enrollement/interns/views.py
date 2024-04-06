from django.shortcuts import render
from .forms import InternForm,SearchForm,CancelForm
from .models import Intern


# Create your views here.

def show(request):
    return render(request,'home.html')


def register(request):
    title = "New Interns Registration"
    form = InternForm(request.POST or None)

    if form.is_valid():
        fname = form.cleaned_data['Intern_fname']
        lname = form.cleaned_data['Intern_lname']
        email = form.cleaned_data['Intern_email']
        phone = form.cleaned_data['Intern_phoneNum']
        # picture = form.cleaned_data['Intern_profile_picture']

        p = Intern(
            Intern_fname=fname,
            Intern_lname=lname,
            Intern_email=email,
            Intern_phoneNum=phone,
            # Intern_profile_picture=picture

        )
        usedemail=Intern.objects.filter(Intern_email=email).exists() 
        print("Used Email",usedemail)
        if usedemail:
            return render (request,'ack.html',{"title":"You can't register more than once"})
        else:
            p.save()
            return render(request,'ack.html',{"title":"Registered Successfully"})

    context = {
        "title": title,
        "form": form,
    }
    return render(request,'register.html',context)




def existing(request):
    title="All Registered Interns"
    queryset = Intern.objects.all()

    context = {
        "title":title,
        "queryset":queryset,
    }

    return render(request,"existing.html",context)



def search(request):
    title = "Search Intern"
    form = SearchForm(request.POST or None)  # Initialize form for search criteria

    if form.is_valid():
        name = form.cleaned_data['Intern_fname']
        queryset = Intern.objects.filter(Intern_fname=name)  # Case-insensitive search
        context = {
            'title': title,
            'form': queryset,}
        return render(request, 'existing.html', context)
    
    context = {
            'title': title,
            'form': form,}
    return render(request, 'search.html', context)







#Cancel the registration
def cancel(request):
    title = "Delete Intern"
    form = CancelForm(request.POST or None) 

    if form.is_valid():
        phone = form.cleaned_data['Intern_phoneNum']
        queryset = Intern.objects.filter(Intern_phoneNum=phone)

        context = {
            'title': title,
            'form': queryset,}
       
        if queryset.exists():
            queryset.delete()
            return render(request,'cancel.html',{"title":"Deleted Successfully"})


    


