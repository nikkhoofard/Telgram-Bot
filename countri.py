import requests
import json


def country(countri_name):
    count = countri_name
    url = "http://api.countrylayer.com/v2/name/"
    url +=count
    acces_key = {'access_key':'24a4c156eb0dc6ee992ca797ec65bd6f'}
    response = requests.get(url,params=acces_key).json()
    json_data = response
    
    name = json_data[0]["name"]
    capital = json_data[0]["capital"]
    region = json_data[0]["region"]
    final = 'country name is %s , the capitel is %s and the region is %s' %(name,capital,region)
    return final
    












