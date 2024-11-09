from django.db import models


class DiseaseAttributes(models.Model):
    diseaseNID=models.IntegerField(primary_key = True)
    diseaseid=models.CharField( max_length=255)
    diseasename=models.CharField( max_length=255)
    type=models.CharField(max_length=255) 
    
    def __str__(self):
        return self.name
    class Meta:
        managed = True 
        db_table = 'diseaseAttributes'
    
