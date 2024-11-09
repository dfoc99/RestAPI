from django import forms  
from .models import DiseaseAttributes 

class DiseaseAttributesForm(forms.ModelForm):  
    class Meta:  
        model = DiseaseAttributes
        fields = "__all__"  