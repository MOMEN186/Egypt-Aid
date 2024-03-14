from rest_framework import serializers
from poorest.models import User,Government,School,Infrastructure,Center,Village,Medical,Holly_places,public_safety

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password']
        extra_kwargs={'password':{'write_only':True}}
        
class GovernmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Government
        fields='__all__'        
        
class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model=School
        fields='__all__'        


class InfrastructureSerializer(serializers.ModelSerializer):
    class Meta:
        model=Infrastructure
        fields='__all__'        

class CenterSerializer(serializers.ModelSerializer):
    class Meta:
        model=Center
        fields='__all__'        

class VillageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Village
        fields=['name','government','center','population']   

class MedicalSerializer(serializers.ModelSerializer):
    class Meta:
        model=Medical
        fields='__all__'        


class Holly_placesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Holly_places
        fields='__all__'        


class public_safetySerializer(serializers.ModelSerializer):
    class Meta:
        model=public_safety
        fields='__all__'    