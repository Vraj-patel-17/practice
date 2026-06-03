from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
def fetch_website(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,"lxml")
    title=soup.title.string if soup.title else "not title found"
    if soup.body:
        for irr in soup.body(["script","style","img","input"]):
            irr.decompose()
        text=soup.body.get_text(separator="\n",strip=True)
    else:
        text=""
    return (title + "\n\n" + text)[:2_000]
def fetch_website_links(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'lxml')
    links = []

    for tag in soup.find_all("a", href=True):
        href = tag["href"]

        if href.startswith(("javascript:", "#", "mailto:", "tel:")):
            continue

        links.append(urljoin(url, href))

    return list(dict.fromkeys(links))
    #links=[link.get("href") for link in soup.find_all("a")]
    #return [link for link in links if link]