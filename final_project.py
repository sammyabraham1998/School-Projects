#This final project compares the relevancy of 'COVID-19' and 'Long COVID' articles, and displays a graph about how often each is reported in the media.

import requests as rq, matplotlib.pyplot as plt, time

#Extract Data
url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json'
API_KEY = 'tb9GtnTQ4I0r6teHMmAmulDjBaZi3TjI'
params1 = {'query': 'Long COVID', 'api-key': API_KEY}
params2 = {'query': 'COVID-19', 'api-key': API_KEY}


years = ['2019', '2020', '2021', '2022', '2023']
years_count1 = []
years_count2 = []

for each in years:
    print(each)
    begin_date = each + '01' + '01'

    if each == '2023':
        end_date = each + '05' + '03'
    else:
        end_date = each + '12' + '31'
    
    params1 = {'query': 'Long COVID', 'api-key': API_KEY, 'begin_date':begin_date, 'end_date':end_date}
    params2 = {'query': 'COVID-19', 'api-key': API_KEY, 'begin_date':begin_date, 'end_date':end_date}
    response1 = rq.get('https://api.nytimes.com/svc/search/v2/articlesearch.json?fq=Long%20COVID&api-key=tb9GtnTQ4I0r6teHMmAmulDjBaZi3TjI', params1)
    print(each)
    response2 = rq.get('https://api.nytimes.com/svc/search/v2/articlesearch.json?fq=COVID-19&api-key=tb9GtnTQ4I0r6teHMmAmulDjBaZi3TjI', params2)
    print(each)
    years_count1.append(response1.json()['response']['meta']['hits'])
    years_count2.append(response2.json()['response']['meta']['hits'])
    time.sleep(30)

#Transform Data
fig, ax = plt.subplots()
ax.plot(years, years_count1)
ax.plot(years, years_count2)
plt.title("COVID-19 & Long COVID Articles Per Year")
plt.xlabel("Year")
plt.ylabel("Number of Relevant Articles")

#Load Data 
plt.savefig('COVID-19&Long_COVID_Relevancy.png')