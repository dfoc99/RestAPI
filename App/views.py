from django.shortcuts import render, redirect  
from .models import DiseaseAttributes
from .filters import DiseaseFilter
from .forms import DiseaseAttributesForm

# Import Pagination stuff
from django.core.paginator import Paginator


def home(request):
    return render(request,"App/home.html")

# Generate the page About with the html file about
def about(request):
    return render(request, "App/about.html")

def search(request):
    types = DiseaseAttributes.objects.values_list('type', flat=True).distinct()
    # Request parameters
    if request.method == 'GET':
        # get parameters from URL

        diseases = DiseaseAttributes.objects.all()
        myFilter  = DiseaseFilter(request.GET,queryset=diseases)
        diseases = myFilter.qs
        ordered_diseases = diseases.order_by('diseaseid')

        # Pagination
        p = Paginator(ordered_diseases,20)
        page = request.GET.get('page')
        page_obj = p.get_page(page)

        context = {
            "diseases":ordered_diseases,
            "myFilter":myFilter,
            "types":types,  
            "page_obj":page_obj,
        }
    
    else:
        # get parameters from the FORM
        diseases = DiseaseAttributes.objects.all()
        myFilter  = DiseaseFilter(request.POST,queryset=diseases)
        diseases = myFilter.qs
        ordered_diseases = diseases.order_by('diseaseid')
        
        # Pagination
        p = Paginator(diseases,20)
        page=1
        page_obj = p.get_page(page)

        context = {
            "diseases":ordered_diseases,
            "myFilter":myFilter,
            "types":types,  
            "page_obj":page_obj,
        }


    return render(request,'App/search.html',context=context)



# Adding CRUD operations 

def emp(request):  
    if request.method == "POST":  
        form = DiseaseAttributesForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = DiseaseAttributesForm 
    return render(request,'App/index.html',{'form':form})  


def show(request):  
    disease = DiseaseAttributes.objects.all()  
    return render(request,"App/show.html",{'disease':disease})  

def edit(request, diseaseNID): 
    disease = DiseaseAttributes.objects.get(diseaseNID=diseaseNID)  
    return render(request,'App/edit.html', {'disease':disease})  

def update(request, diseaseNID):  
    disease = DiseaseAttributes.objects.get(diseaseNID=diseaseNID)  
    form = DiseaseAttributesForm(request.POST, instance = disease)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")
    else:
        form = DiseaseAttributesForm(instance=disease)
    return render(request, 'App/edit.html', {'disease': form})  

def destroy(request, diseaseNID):  
    disease = DiseaseAttributes.objects.get(diseaseNID=diseaseNID)  
    disease.delete()  
    return redirect("/show")  