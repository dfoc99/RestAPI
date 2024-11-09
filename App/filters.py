import django_filters
from .models import DiseaseAttributes


def get_types():
    # Fetch choices from model
    types = DiseaseAttributes.objects.values_list('type', flat=True).distinct()
    
    # Create a list of tuples for choices
    choices = [(type, type) for type in types]
    
    return choices


class DiseaseFilter(django_filters.FilterSet):
    diseasename = django_filters.CharFilter(lookup_expr='icontains')
    type = django_filters.ChoiceFilter(choices=get_types())
    class Meta:
        model = DiseaseAttributes
        fields = ['type','diseasename','diseaseid',"diseaseNID"]
        exclude = ['diseaseid',"diseaseNID"]

