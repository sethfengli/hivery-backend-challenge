from rest_framework import serializers
from rest_framework.request import Request
from .models import Company, Fruit, Vegetable, Tag, People

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('index', 'name', )

class FruitSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Fruit
        fields = ('index','name', )

class VegetableSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Vegetable
        fields = ('index','name', )

class TagSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Tag
        fields = ('index','name', )

class PeopleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = People
        fields = ('_id',
                    'index', 
                    'guid',
                    'has_died',
                    'balance',
                    'picture', 
                    'age',
                    'eyeColor',
                    'name',
                    'gender',
                    'email', 
                    'phone', 
                    'address',
                    'about', 
                    'registered',
                    'tags',
                    'friends', 
                    'greeting', 
                    'favouriteFood', 
                    'favouriteFruit', 
                    'favouriteVegetable',
                    'company',  )

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

class BriefPeopleSerializer(DynamicFieldsModelSerializer):
          
    class Meta:
        model = People
        fields = ('name', 'age', 'address', 'phone')

class HyperlinkedPeopleSerializer (serializers.HyperlinkedModelSerializer):
    
    def __init__(self, *args, **kwargs):
        super(serializers.HyperlinkedModelSerializer, self).__init__(*args, **kwargs)
    
    class Meta:
        model = People
        fields = ('index', 'url', 'name', 'age', 'address', 'phone', 
                   'age', 'eyeColor', 'has_died',)

class FavouriteFoodSerializer(DynamicFieldsModelSerializer):
    
    class Meta:
        model = People
        fields = ('name', 'age', 'favouriteFruit','favouriteVegetable',)

    def to_representation(self, obj):
        representation = super().to_representation(obj)

        username = representation.pop('name')
        age =      representation.pop('age')   

        fruits = representation.pop('favouriteFruit')
        fruitNames =  Fruit.objects.filter(index__in = (fruits)).values_list('name', flat=True)
        
        vegetables = representation.pop('favouriteVegetable')
        vegetableNames =  Vegetable.objects.filter(index__in = (vegetables)).values_list('name', flat=True)
        
        representation['username'] = username
        representation['age'] = age
        representation['fruits'] = fruitNames
        representation['vegetables'] = vegetableNames

        return representation