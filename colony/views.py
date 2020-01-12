from django.shortcuts import render
from rest_framework import generics, permissions, status
from .serializers import CompanySerializer, FruitSerializer, VegetableSerializer, TagSerializer, PeopleSerializer, HyperlinkedPeopleSerializer, BriefPeopleSerializer, FavouriteFoodSerializer
from .models import Company, Fruit, Vegetable, Tag, People
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework.reverse import reverse 
from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

@api_view(['GET']) 
def api_root(request, format=None):
    return Response({
        'companies': reverse('company-list', request=request, format=format),
        'people': reverse('people-list', request=request, format=format),
        #'employees': reverse('employee-list', request=request, format=format) ,
    })

class CompanyList(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class FruitList(generics.ListCreateAPIView):
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class FruitDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fruit.objects.all()
    serializer_class =FruitSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class VegetableList(generics.ListCreateAPIView):
    queryset = Vegetable.objects.all()
    serializer_class = VegetableSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class VegetableDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vegetable.objects.all()
    serializer_class =VegetableSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class =TagSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class PeopleList(generics.ListCreateAPIView):
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class PeopleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = People.objects.all()
    serializer_class =PeopleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class EmployeeList(generics.ListAPIView):    
    serializer_class = HyperlinkedPeopleSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    lookup_url_kwarg = "company_id"

    def get_queryset(self):
        co_id = self.kwargs.get(self.lookup_url_kwarg)
        employees = People.objects.filter(company_id=co_id)
        return get_list_or_404(employees)

def to_bool(value):
    """
    Converts 'something' to boolean. Raises exception if it gets a string it doesn't handle.
    Case is ignored for strings. These string values are handled:
      True: 'True', "1", "TRue", "yes", "y", "t"
      False: "", "0", "faLse", "no", "n", "f"
    Non-string values are passed to bool.
    """
    if type(value) == type(''):
        if value.lower() in ("yes", "y", "true",  "t", "1"):
            return True
        if value.lower() in ("no",  "n", "false", "f", "0", ""):
            return False
        raise Exception('Invalid value for boolean conversion: ' + value)
    return bool(value)

class CommonFriends(APIView):
    """
    Returns the common friends of two person
    """
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, format=None, **kwargs):

        filterList = [ 'person1_index' , 'person2_index', 'eyeColor','has_died']
        filter = {}
        for f in filterList:
            filter[f] = kwargs.get(f)

        twoPeopleList = [filter['person1_index'], filter['person2_index'] ]
        twoPeople = People.objects.filter(index__in = (twoPeopleList))
        twoPeopleSerializer =  BriefPeopleSerializer(twoPeople, many=True)

        people1_friends = People.objects.filter(index=filter['person1_index']).values_list('friends', flat=True)
        people2_friends = People.objects.filter(index=filter['person2_index']).values_list('friends', flat=True)
      
        commonFriendIndexList = list( set(people1_friends).intersection(set(people2_friends)) )
        commonFriends = People.objects.filter(index__in = (commonFriendIndexList))
        commonFriends = commonFriends.filter(eyeColor = filter['eyeColor']).filter(has_died = to_bool(filter['has_died']))
  
        if  commonFriends.exists():
            response_status = status.HTTP_200_OK
            commonFriendSerializer =  BriefPeopleSerializer( commonFriends , many=True )
            common_friends_data = commonFriendSerializer.data

        else:
            response_status = status.HTTP_404_NOT_FOUND
            common_friends_data = 'Not found'

        return Response({
            'two_people': twoPeopleSerializer.data,
            'common_friends': common_friends_data, 
        }, status=response_status)

class FavouriteFood(APIView):    

    def get(self, request, format=None, **kwargs):
        index = kwargs.get('person_index')
        try:
            person = People.objects.get(index=index)
            return Response(  FavouriteFoodSerializer(person).data,  status=status.HTTP_200_OK)
        except People.DoesNotExist:
            return Response( { 'Not found people' : index },  status=status.HTTP_404_NOT_FOUND)
     
            
           
