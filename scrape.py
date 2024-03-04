from bs4 import BeautifulSoup as bs
import pandas as pd 
import requests

stars_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

page = requests.get(stars_url)
soup = bs(page.text,'html.parser')
star_table = soup.find('table')

temp_list =[]

rows = star_table.find_all('tr')

for tr in rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

star_names = []
star_distance = []
mass = []
radius = []
lum = []

print(len(temp_list))

for i in range(1,len(temp_list)):
    star_names.append(temp_list[1])
    star_distance.append(temp_list[3])
    mass.append(temp_list[5])
    radius.append(temp_list[6])
    lum.append(temp_list[7])

df2 = pd.DataFrame(list(zip(star_names,star_distance,mass,radius,lum)),columns = ['star_names','distance','mass','radius','luminousity'])
df2.to_csv('stars.csv')