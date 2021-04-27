import requests
from bs4 import BeautifulSoup

resp = requests.get(
  url='https://en.wikipedia.org/wiki/List_of_painters_by_name'
)
soup = BeautifulSoup(resp.content, 'html.parser')

links = soup.find(id="bodyContent").find_all("a")

plinks = []
for link in links:
  try:
    if link['href'].find("/wiki/List_of_painters_by_name_beginning_with") != -1:
      plinks.append(link['href'])
  except:
    print()
 

artists = []

def get_artists(url, artists):
  print(url)
  count = 0
  resp = requests.get(
    url="https://en.wikipedia.org" + url
  )
  soup = BeautifulSoup(resp.content, 'html.parser')
  links = soup.find(id="bodyContent").find_all("a")
  for link in links:
    try:
      if link['href'].find("/wiki/") != -1 and link['href'].find("List_of") == -1 and link['href'].find("Category") == -1:
        artists.append(link['title'])
        count += 1
    except:
      pass
  print(f"Added {count} lines\n")    
      
for plink in plinks:
  get_artists(plink, artists)      
 
f = open("artists.txt", "w")
for artist in artists:
  f.write(f"{artist}\n")
f.close()
