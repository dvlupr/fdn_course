import requests
from bs4 import BeautifulSoup

url = "https://wiki.python.org/moin/IntroductoryBooks"

response = requests.get(url)

dir(response)

print(response.headers)

content = response.content

soup = BeautifulSoup(content, 'lxml')

print(soup.prettify())

print(soup.title)
print(soup.title.string)

all_a = soup.find_all("a")

for x in all_a:
    print(x)

all_a_https = soup.find_all("a", "https")

all_a_https[0]

for x in all_a_https:
    print(x.attrs['href'])

soup.find_all("p", "line874")
soup.find_all("p", {"class": "line874"})

lines = soup.find_all("p", "line874")
for line in lines:
    a_tag = line.find("a")
    if a_tag is not None:
        print(a_tag.attrs['href'])

data = {}
for a in all_a_https:
    title = a.string.strip()
    data[title] = a.attrs['href']

print(data)
