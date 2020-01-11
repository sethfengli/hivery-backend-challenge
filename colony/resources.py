from import_export import resources
from .models import Company, Fruit, Vegetable, Tag, People, Friend
from import_export.fields import Field
from import_export.widgets import ManyToManyWidget, ForeignKeyWidget, DecimalWidget, DateTimeWidget, NumberWidget, IntegerWidget
from decimal import Decimal
from re import sub
import datetime


class CompanyResource(resources.ModelResource):
    
    class IndexWidget(IntegerWidget):
        """
        Widget for converting decimal fields.
        """
        def clean(self, value, row=None, *args, **kwargs):
            index = super().clean(value)
            if index is None:
                return None 
            else:
                return index + 1

    name = Field(attribute='name', column_name='company')
    index = Field(attribute='index', column_name='index', widget=IndexWidget())

    class Meta:
        model = Company
        import_id_fields = ('index')
        fields = ('index', 'company',)

class FruitResource(resources.ModelResource):
    
    name = Field(attribute='name', column_name='fruitName')

    class Meta:
        model = Fruit
        import_id_fields = ('index')
        fields = ('index', 'name',)

class VegetableResource(resources.ModelResource):
    
    name = Field(attribute='name', column_name='vegetableName')

    class Meta:
        model = Vegetable
        import_id_fields = ('index')
        fields = ('index', 'name',)

class TagResource(resources.ModelResource):
    
    name = Field(attribute='name', column_name='tagName')

    class Meta:
        model = Tag
        import_id_fields = ('index')
        fields = ('index', 'name',)

class PeopleResource(resources.ModelResource):

    class CurrencyStringToDecimalWidget(NumberWidget):
        """
        Widget for converting decimal fields.
        """
        def clean(self, value, row=None, *args, **kwargs):
            if self.is_empty(value):
                return None
            try:
                d = Decimal(sub(r'[^\d.]', '', value))
                return d
            except (ValueError, TypeError):
                raise ValueError("Enter a valid number.")
            
    class TimeZoneStringToDateTime(DateTimeWidget):
        """
        Widget for converting string with Time Zone fields.
        """
        def clean(self, value, row=None, *args, **kwargs):
            try:
                dt = datetime.datetime.fromisoformat(value)
                return dt
            except (ValueError, TypeError):
                raise ValueError("Enter a valid date/time.")

    class ListToManytoMany(ManyToManyWidget):
        """
        Widget for converting List to ManytoMany fields.
        """
        def clean(self, value, row=None, *args, **kwargs):
            if not value:
                return self.model.objects.none()
            if isinstance(value, (float, int)):
                ids = [int(value)]
            else:
                ids = filter(None, [i.strip() for i in value])
            return self.model.objects.filter(**{
                '%s__in' % self.field: ids
            })


    company=Field(attribute='company' , widget=ForeignKeyWidget(Company, field='index'), column_name='company_id')
    tags = Field(attribute='tags', widget=ListToManytoMany(Tag, field='name'), column_name='tags')
    favouriteFruit = Field(attribute='favouriteFruit', widget=ListToManytoMany(Fruit, field='name'), column_name='favouriteFood')
    favouriteVegetable = Field(attribute='favouriteVegetable', widget=ListToManytoMany(Vegetable,  field='name'), column_name='favouriteFood')
    balance = Field(attribute='balance', widget=CurrencyStringToDecimalWidget(), column_name='balance')
    registered = Field(attribute='registered', widget=TimeZoneStringToDateTime(), column_name='registered')
    
    class Meta:
        model = People
        import_id_fields = ('index')
        fields =('_id',
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
                'greeting',
                'favouriteFruit',
                'favouriteVegetable', 
                'company', )


class FriendResource(PeopleResource):
    
    class DictToManytoMany(ManyToManyWidget):
        """
        Widget for converting List to ManytoMany fields.
        """
        def clean(self, value, row=None, *args, **kwargs):
            if not value:
                return self.model.objects.none()
            if isinstance(value, (float, int)):
                ids = [int(value)]
            else:
                ids = filter(None, [ d['index'] for d in value])
            return self.model.objects.filter(**{
                '%s__in' % self.field: ids
            })

    friends = Field(attribute='friends', widget=DictToManytoMany(People, field='index'), column_name='friends') 

    class Meta:
        model = Friend
        fields =('_id',
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
            'greeting',
            'favouriteFruit',
            'favouriteVegetable', 
            'company'
            'friends', )