from paranuara import settings
from colony.resources import  CompanyResource, FruitResource, VegetableResource, TagResource, PeopleResource, FriendResource
from colony.models import  Company, Fruit, Vegetable, Tag, People, Friend
import tablib
import pandas as pd
import json

def run():
    with open("resources/companies.json", 'r') as f:
        company = f.read() 
        result = CompanyResource().import_data(tablib.Dataset().load(company), raise_errors=True, dry_run=False)

    with open("resources/fruits.json", 'r') as f:
        fruit = f.read() 
        result = FruitResource().import_data(tablib.Dataset().load(fruit), raise_errors=True, dry_run=False)

    with open("resources/vegetables.json", 'r') as f:
        vegetable = f.read() 
        result = VegetableResource().import_data(tablib.Dataset().load(vegetable), raise_errors=True, dry_run=False)

    #Tags could be changes as the people.json file changes

    df = pd.read_json( 'resources/people.json')
    TagSet = set('')
    for i in range(len(df.index)):
        TagSet = TagSet.union(set(df['tags'].iloc[i]))
    tags = list(TagSet)         # remove the dulicated items
    tags.sort()                 # sort the list

    with open('resources/tags.json', 'w', encoding='utf-8') as f:
        json.dump([{"index":count, "tagName": name} for count, name in enumerate(tags)] , f, ensure_ascii=False, indent=4)

    with open("resources/tags.json", 'r') as f:
        tag = f.read() 
        result = TagResource().import_data(tablib.Dataset().load(tag), raise_errors=True, dry_run=False)

    ### End tags
    
    with open("resources/people.json", 'r') as f:
        people = f.read() 
        result = PeopleResource().import_data(tablib.Dataset().load(people), raise_errors=True, dry_run=False)

    with open("resources/people.json", 'r') as f:
        friend = f.read() 
        result = FriendResource().import_data(tablib.Dataset().load(friend), raise_errors=True, dry_run=False)
