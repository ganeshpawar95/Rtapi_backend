from rest_framework import serializers 
from .models import Project,Scan
 
 
class ProjectSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Project
        fields = ('id',
                  'projectname',
                  'description',
                  'targeturl',
                  'logfile',
                  'connectiontimout',
                  'sendtimeout',
                  'receivetimeout')
class ScanSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Scan
        fields = ('id',
                  'projectname',
                  'testmode',
                  'scandatetime',
                  )
        
