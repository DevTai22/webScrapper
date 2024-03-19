from requests_html import HTMLSession
from bs4 import BeautifulSoup

s= HTMLSession()

searchterm = "#"
url= "https://www.amazon.com/?&tag=googleglobalp-20&ref=pd_sl_7nnedyywlk_e&adgrpid=159651196451&hvpone=&hvptwo=&hvadid=675114638556&hvpos=&hvnetw=g&hvrand=1687298044680113984&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1012872&hvtargid=kwd-10573980&hydadcr=2246_13649807&gad_source=1"

def get_data(url):
    r=s.get(url)
    r.html.render(timeout=20)
    soup=BeautifulSoup(r.html.html,"htmlparser")

    return soup

print(get_data(url))

def get_object(soup):
    products= soup.find_all("div",{"data-component-type": "s-search-result"})
    lista_diccionarios=[]
    for product in product:
        title=product.find("a",{"class":"a-link-normal a-text-normal"}).text[:25] 
        link="https://www.amazon.com/?&tag=googleglobalp-20&ref=pd_sl_7nnedyywlk_e&adgrpid=159651196451&hvpone=&hvptwo=&hvadid=675114638556&hvpos=&hvnetw=g&hvrand=1687298044680113984&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1012872&hvtargid=kwd-10573980&hydadcr=2246_13649807&gad_source=1"+product.find("a",{"class":"a-link-normal a-text-normal"})["href"]
        try:
            price=product.find("span",{"class": "a-price-whole"}).text
        except:
            price=0
        try:
            reviews=int(product.find("span",{"class":"a-size-base"}))
        except: 
            reviews=0

        acumulador={
            "title":title,
            "link":link,
            "price":price,
            "reviews":reviews

        }

        lista_diccionarios.append(acumulador)
    return lista_diccionarios

    
    _