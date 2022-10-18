import sys
import requests
import pandas as pd
from bs4 import BeautifulSoup

if (len(sys.argv) < 2): sys.exit("Search string is missing")

search = sys.argv[1]
lastPage = int(sys.argv[2]) if len(sys.argv) == 3 else 1
url='https://scholar.google.com/scholar'
results = []

for page in range(1, lastPage + 1):
    params = {'q': sys.argv[1], 'page': page}
    response = requests.get(url, params)

    soup = BeautifulSoup(response.text, 'html.parser')

    articles = soup.findAll('div', attrs={"class":"gs_r gs_or gs_scl"})

    for article in articles:
        titleTag = article.select_one('.gs_ri .gs_rt a')
        descTag = article.select_one('.gs_ri .gs_rs')
        linkTag = article.select_one('.gs_or_ggsm a')

        articleDict = {
          'title': titleTag and titleTag.get_text(),
          'desc': descTag and descTag.get_text(),
          'link': linkTag and linkTag.get('href')
        }
        if (articleDict['title'] and articleDict['desc'] and articleDict['link']): results.append(articleDict)

df = pd.DataFrame(results)
df.to_csv('results.csv', index=False, encoding='utf-8')
