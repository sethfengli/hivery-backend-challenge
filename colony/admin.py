from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Company, Fruit, Vegetable, Tag, People, Friend
from .resources import CompanyResource, FruitResource, VegetableResource, TagResource, PeopleResource, FriendResource

class CompanyAdmin(ImportExportModelAdmin):
    resource_class= CompanyResource

class FruitAdmin(ImportExportModelAdmin):
    resource_class= FruitResource

class VegetableAdmin(ImportExportModelAdmin):
    resource_class= VegetableResource

class TagAdmin(ImportExportModelAdmin):
    resource_class= TagResource

class PeopleAdmin(ImportExportModelAdmin):
    resource_class= PeopleResource

class FriendAdmin(ImportExportModelAdmin):
    resource_class= FriendResource

admin.site.register(Company, CompanyAdmin)
admin.site.register(Fruit, FruitAdmin)
admin.site.register(Vegetable, VegetableAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(People, PeopleAdmin, )
admin.site.register(Friend, FriendAdmin, )

