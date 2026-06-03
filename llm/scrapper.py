from bs4 import BeautifulSoup
import requests
def fetch_website(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html-parser')
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
    soup=BeautifulSoup(response.content,'html-parser')
    links=[link.get("href") for link in soup.find_all("a")]
    return [link for link in links if link]