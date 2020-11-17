#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
import json
from bs4 import BeautifulSoup
import pandas as pd


# In[3]:


urls = [
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=ADAMS&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=ALLEGHENY&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=ARMSTRONG&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=BEAVER&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=BEDFORD&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=BERKS&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=BLAIR&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=BRADFORD&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=BUCKS&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=BUTLER&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=CAMBRIA&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=CAMERON&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=CARBON&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=CENTRE&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=CHESTER&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=CLARION&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=CLEARFIELD&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=CLINTON&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=COLUMBIA&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=CRAWFORD&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=CUMBERLAND&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=DAUPHIN&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=DELAWARE&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=ELK&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=ERIE&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=FAYETTE&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=FOREST&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=FRANKLIN&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=FULTON&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=GREENE&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=HUNTINGDON&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=INDIANA&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=JEFFERSON&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=JUNIATA&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=LACKAWANNA&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=LANCASTER&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=LAWRENCE&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=LEBANON&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=LEHIGH&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=LUZERNE&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=LYCOMING&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=MCKEAN&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=MERCER&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=MIFFLIN&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=MONROE&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=MONTGOMERY&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=MONTOUR&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=NORTHAMPTON&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=NORTHUMBERLAND&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=PERRY&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=PHILADELPHIA&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=PIKE&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=POTTER&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=SCHUYLKILL&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=SNYDER&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=SOMERSET&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=SULLIVAN&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=SUSQUEHANNA&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=TIOGA&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=UNION&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=VENANGO&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=WARREN&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=WASHINGTON&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=WAYNE&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=WESTMORELAND&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=WYOMING&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined",
    "https://www.electionreturns.pa.gov/api/ElectionReturn/GetCountyData?countyName=YORK&methodName=GetCountyData&electionid=undefined&electiontype=G&isactive=undefined"
]


# In[4]:


pennsylvania_jsons = []
for url in urls:
    result = requests.get(url, headers={'Content-Type': 'application/json'})
    pennsylvania_jsons.append(result.json())


# In[17]:


table = pd.DataFrame(columns=['County', 'Biden', 'Trump', 'Jorgenson', "Total", "Percent Biden", "Percent Trump", "Percent Jorgenson"])
for index, county_json in enumerate(pennsylvania_jsons):
    
    county_data = json.loads(county_json)
    county = list(county_data["Election"])[0]
    biden  = county_data["Election"][county][0]['President of the United States'][0]['Districts'][0]['Candidates'][0]['Votes']
    trump  = county_data["Election"][county][0]['President of the United States'][0]['Districts'][0]['Candidates'][1]['Votes']
    jorgenson = county_data["Election"][county][0]['President of the United States'][0]['Districts'][0]['Candidates'][2]['Votes']
    total = int(biden) + int(trump) + int(jorgenson)
    percentBiden = int(biden)/int(total)*100
    percentTrump = int(trump)/total*100
    percentJorgenson = int(jorgenson)/total*100
    table.loc[index] = (county, biden, trump, jorgenson, total, percentBiden, percentTrump, percentJorgenson)
    
table


# In[18]:


table.to_csv("pennsylvania_2020elections_counties.csv", encoding='utf-8')


# In[ ]:




