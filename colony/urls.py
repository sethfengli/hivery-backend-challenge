from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from colony import views
from django.views.generic import TemplateView
from django.conf.urls import url, include
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('company/', views.CompanyList.as_view(), name='company-list'),
    path('company/<int:pk>/', views.CompanyDetail.as_view()),
    path('fruit/', views.FruitList.as_view()),
    path('fruit/<int:pk>/', views.FruitDetail.as_view()),
    path('vegetable/', views.VegetableList.as_view()),
    path('vegetable/<int:pk>/', views.VegetableDetail.as_view()),
    path('tag/', views.TagList.as_view()),
    path('tag/<int:pk>/', views.TagDetail.as_view()),
    path('people/', views.PeopleList.as_view(), name='people-list'),
    path('people/<int:pk>/', views.PeopleDetail.as_view(), name='people-detail'),
    path('employees/<int:company_id>/', views.EmployeeList.as_view(),  name='employee-list'),
    path('commonfriends/<int:person1_index>/<int:person2_index>/<str:eyeColor>/<int:has_died>/', views.CommonFriends.as_view()),
    path('favouritefood/<int:person_index>/', views.FavouriteFood.as_view()),
    path('', views.api_root),
    path('openapi-schema/', get_schema_view(
        title="paranura",
        description="API for all things …",
        version="1.0.0"
     ), name='openapi-schema'),
     url('openapi/', TemplateView.as_view(template_name="index.html")),
]