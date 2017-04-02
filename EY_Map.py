from bs4 import BeautifulSoup
import requests

country_city_dict = {}
map_url = "http://www.ey.com/Media/vwCodeLibraries/OfficeDirectory/$file/directory.xml"
bsObj = BeautifulSoup(requests.get(map_url).text, "html.parser")
countryObjs = bsObj.findAll("country")
for country in countryObjs:
    cityList = [cityObj.text for cityObj in country.findAll("city_name")]
    country_city_dict[country.country_name.text] = cityList

url = "http://www.ey.com/ourlocations"



