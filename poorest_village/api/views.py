from rest_framework.response import Response
from rest_framework.decorators import api_view
from poorest.models import User,Government,School,Infrastructure,Center,Village,Medical,Holly_places,public_safety
from .serializers import GovernmentSerializer,UserSerializer,SchoolSerializer,InfrastructureSerializer,CenterSerializer,VillageSerializer,MedicalSerializer,Holly_placesSerializer,public_safetySerializer
import django.apps
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
import json
from django.db.models import Count

@api_view(["get"])
def dashboard(request):
   
   dict={}
   for model in django.apps.apps.get_models():
    name = model.__name__
    count = model.objects.all().count()
    dict[name] = count
    print("{} rows: {}".format(name, count))
   return Response(dict) 

 
# def villages(request,id):
#     temp=Village.objects.filter(id=id).values()
#     print(temp)
#     dict={}
#     print(Village.objects.filter(id=id).values())
#     print("----------------village------------------")  
#     dict["name"]=Village.objects.filter(id=id).values("name")
#     print(temp[0].get("government_id"))
#     dict["government"]=GovernmentSerializer(Government.objects.filter(id=temp[0].get("government_id")),many=True).data
#     dict["schools"]=SchoolSerializer(School.objects.filter(village=id),many=True).data
#     dict["Medical"]=MedicalSerializer(Medical.objects.filter(village=id),many=True).data
#     dict["Holly_places"]=Holly_placesSerializer(Holly_places.objects.filter(village=id),many=True).data
#     dict["Infrastructure"]=InfrastructureSerializer(Infrastructure.objects.filter(village=id),many=True).data
#     return Response(dict)
@api_view(["get"])
def get_centers(request):
   print("------------------centers---------------")
   # serializer=CenterSerializer(Center.objects.all(),many=True).data
   centers=Center.objects.annotate(
        schools_count=Count('school'),
        medical_facilities_count=Count('medical'),
        infrastructures_count=Count('infrastructure'),
        villages_count=Count('village'),
        holly_places_count=Count("holly_places"),
        public_safety_count=Count("public_safety"),
      )
   centers_data=[] 
   
   for center in centers:
      government=GovernmentSerializer(center.government).data
      centers_data.append({
         "name":center.name,
         "government":government,
          "villages":center.villages_count,
         "schools":center.schools_count,
         "medical_facilities":center.medical_facilities_count,
         "infrastructures:":center.infrastructures_count,
         "public_safety":center.public_safety_count,
         "population":center.population
      })
   return Response(centers_data)


@api_view(["get"])
def get_all_villages(request):
    # Fetch all villages and annotate with counts for related entities to optimize database queries
    villages = Village.objects.annotate(
        schools_count=Count('school'),
        medical_facilities_count=Count('medical'),
        infrastructures_count=Count('infrastructure'),
        holly_places_count=Count("holly_places"),
        public_safety_count=Count("public_safety"),
        # Add annotation for holy places count if applicable
    )

    # Initialize an empty list to hold data for all villages
    villages_data = []

    for village in villages:
        # Serialize government data. This assumes that there's a direct ForeignKey relationship.
        government = GovernmentSerializer(village.government).data
        center=CenterSerializer(village.center).data
        # Append village data to the list
        villages_data.append({
            "name": village.name,
            "government": government,
            "center":center,
            "schools_count": village.schools_count,
            "medical_facilities_count": village.medical_facilities_count,
            "infrastructures_count": village.infrastructures_count,
            "population":village.population,
            # Include holy places count here once corrected
        })

    # Return the list of villages as a Response object
    return Response(villages_data)


@api_view(["get"])
def get_village(request, id):
    # Assuming Holly_places is a typo and you meant to use another model or serializer for Holy places.
    
    # Use get_object_or_404 for a single object retrieval to handle not found errors.
    village = get_object_or_404(Village.objects.prefetch_related('school_set', 'medical_set', 'infrastructure_set'), id=id)

    # No need to filter Government as select_related would have done, assuming a ForeignKey from Village to Government
    government = GovernmentSerializer(village.government).data

   #  schools = SchoolSerializer(village.school_set.all(), many=True).data
    schools=village.school_set.all().count()
   #  medical_facilities = MedicalSerializer(village.medical_set.all(), many=True).data
    medical_facilities=village.medical_set.all().count()
    # Assuming Holly_places should be handled similarly but with its respective model and serializer
   #  infrastructures = InfrastructureSerializer(village.infrastructure_set.all(), many=True).data
    infrastructures =village.infrastructure_set.all().count()
    # Construct the response dictionary
    response_dict = {
        "name": village.name,
        "government": government,
        "schools": schools,
        "Medical": medical_facilities,
        "Infrastructure": infrastructures,
        "population":village.population
        # Include Holly_places here once corrected
    }
    return Response(response_dict)

@api_view(["get"])
def get_schools(request):
   print("----------------schools------------------")
   # serializer=SchoolSerializer(School.objects.all(),many=True).data
   schools=School.objects.annotate()
   schools_data=[]
   for school in schools:
      governmnent=GovernmentSerializer(school.government).data
      center=CenterSerializer(school.center).data
      village=VillageSerializer(school.village).data
      schools_data.append({
         "name":school.name,
         "current_capacity":school.current_capacity,
         "capacity":school.capacity,
         "level":school.level,
         "Government":governmnent,
         "Center":center,
         "village":village
      })
   return Response(schools_data)

@api_view(["get"])
def get_medicals(request):
   print("-----------medical-----------------")
   # serializer=MedicalSerializer(Medical.objects.all(),many=True).data
   medicals=Medical.objects.annotate()
   medicals_data=[]
   for medical in medicals:
    government=GovernmentSerializer(medical.government).data
    center=CenterSerializer(medical.center).data
    village=VillageSerializer(medical.village).data
    medicals_data.append({
       "name":medical.name,
       "specilzation":medical.specialization,
       "capcity":medical.capacity,
       "Governmnet":government,
       "center":center,
       "village":village
       })
    
   return Response(medicals_data)

@api_view(["get"])
def get_holly_places(request):
   print("----------------Holly Places-------------------")
   # serializer=Holly_placesSerializer(Holly_places.objects.all(),many=True).data
   holly_places=Holly_places.objects.annotate()
   holly_places_data=[]
   
   for holly in holly_places:
      governmnet=GovernmentSerializer(holly.government).data
      center=CenterSerializer(holly.center).data
      village=VillageSerializer(holly.village).data
      holly_places_data.append({
         "name":holly.name,
         "type":holly.type,
         "capacity":holly.capacity,
         "governmnet":governmnet["name"],
         "center":center,
         "village":village
      })
      
   return Response(holly_places_data)

@api_view(["get"])
def get_infrastructures(request):
   print("-----------infrastructure----------------")
   # serializer=InfrastructureSerializer(Infrastructure.objects.all(),many=True).data
   infrastructures=Infrastructure.objects.annotate()
   infrastructure_data=[]
   for infrastructure in infrastructures:
      government=GovernmentSerializer(infrastructure.government).data
      center=CenterSerializer(infrastructure.center).data
      village=VillageSerializer(infrastructure.village).data
      print(village)
      infrastructure_data.append({ 
      "type":infrastructure.type,
      "capacity":infrastructure.capacity,
      "government":government,
      "center":center,
      "village":village,
      })
    
   return Response(infrastructure_data)

@api_view(["get"])
def get_population(request):
   print("---------population----------------")
   all_governments=Government.objects.annotate()
   all_villages=Village.objects.annotate()
   all_centers=Center.objects.annotate()
   population=0
   for village in all_villages:
      population+=village.population
      
   for center in all_centers:
      population+=center.population
      
   for government in all_governments:
    population+=government.population
        
   return Response(population)  


@api_view(["get"])
def get_public_safety(request):
   # serializer=public_safetySerializer(public_safety.objects.all(),many=True).data
   all_public_safety=public_safety.objects.annotate()
   public_safety_data=[]
   for public in all_public_safety:
      government =GovernmentSerializer(public.government).data
      center=CenterSerializer(public.center).data
      village=VillageSerializer(public.village).data
      public_safety_data.append({
         "type":public.type,
         "Government":government,
         "center":center,
         "village":village,
         "radius":public.radius
      })
      
   return Response(public_safety_data)

@api_view(["post"])
def login(request):
   if request.method == "POST":
    username=request.POST.get("username")
    password=request.POST.get("password")
    
    user=None
    if '@' in username:
      try:
       user=User.objects.get(email=username)
      except ObjectDoesNotExist:pass
      
      if not user: user=authenticate(username=username,password=password)
      
      if user:
         token,_=Token.objects.get(user=user)   
         return Response({'token': token.key}, status=status.HTTP_200_OK)
      
      return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
   
   
@api_view(["get"])
def logout(request):
   if request.method == 'POST':
        try:
            # Delete the user's token to logout
            request.user.auth_token.delete()
            return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["get"])
def admin_view(request):
    if User.is_staff: 
       print("-------------------admin--------------")
    return  HttpResponseRedirect("http://127.0.0.1:8000/admin/")