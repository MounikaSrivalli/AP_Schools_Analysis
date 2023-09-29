import requests
from bs4 import BeautifulSoup
import pandas as pd

columns=['Name']

url3 = 'https://schools.org.in/andhra-pradesh/vizianagaram'
page3=requests.get(url3)
soup3 = BeautifulSoup(page3.text,'html.parser')
next_page3=soup3.find('table',{'class':'table-striped'})
project_href3 = [i['href'] for i in next_page3.find_all('a', href=True)]
district = [] 
for l in range(33,len(project_href3)):
    url2 = 'https://schools.org.in/'+project_href3[l]
    page2 = requests.get(url2)
    soup2 = BeautifulSoup(page2.text,'html.parser')
    next_page2=soup2.find('table',{'class':'table-striped'})
    project_href2 = [i['href'] for i in next_page2.find_all('a', href=True)]
    blocks = []
    for k in range(len(project_href2)):
        url = 'https://schools.org.in/'+project_href2[k]
        page = requests.get(url)
        soup = BeautifulSoup(page.text,'html.parser')
        next_page=soup.find('table',{'class':'table-striped'})
        project_href = [i['href'] for i in next_page.find_all('a', href=True)]
        schools = []
        for j in range(len(project_href)):
            website = 'https://schools.org.in/'+project_href[j]
            url1 = website
            page1 = requests.get(url1)
            soup1 = BeautifulSoup(page1.text,'html.parser')
            Village_Town = soup1.find_all('h2',{'class': 'text-primary'})
            for i in Village_Town:
                name = i.text
            schools.append(name)
        blocks.extend(schools)
    district.extend(blocks)
# state.extend(district)
# final.extend(state)
    # print(schools)
    final_data = pd.DataFrame(data=district,columns=columns)
    print(final_data)
    final_data.to_csv("D:/Mentorskool/Project School/Districts/VIZIANAGARAM/Vizianagaramnames2.csv",index=False)