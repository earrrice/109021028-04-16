import sys
import requests
from bs4 import BeautifulSoup

URL="https://search.books.com.tw/search/query/key/{0}/cat/all"


def urls(url,word):
    url1=url.format(word)
    return url1


def getURL(url):
    headers ={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0;Win64; x64) APPLWebKit/537.36 (KHTML,like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    }
    return requests.get(url,headers=headers)


def getWords(urls):
    r=getURL(urls)
    if r.status_code==requests.codes.ok:
        r.encoding="utf8"
        soup=BeautifulSoup(r.text,"html.parser")
        print("catching:")
        print("----------\n")
        return soup
    else:
        print("error")
        print("----------\n")
        return soup==None 

def wed_scraping_bot(url):
    booklist=[]
    print("retrive data from Internet...")
    soup = parse_html(r.text)
    if soup !=None:
        tag_item=soup.find_all(class_="box_1")
        for item in tag_item:
            book=[]
            book.append(item.find("img")["alt"])
            [isbn,price]=geet_price(item.find("a")["href"])
            book.append(isbn)
            book.append(price)
            print(book)
            time.sleep(3)


def geet_price(url):
    url1="http:"+url
    soup=parse_html(get_resouorce(url1))
    isbnStr=""
    if soup !=None:
        bd=soup.find(class_="bd")
        liList=bd.find_all("li")
        print("liList \n,liList")
        price=0
        priceUl=soup.find("ul",{"class":"price"})
        for liData in liData.text:
            print("liData\n\n",liData.text)
            if "ISBN" in liData.text:
                isbnStr=liData.text[5:]
        price=priceUl.find("li").text[3:-1]
        return [isbnStr,price]
    else:
        return [None,None]

if __name__ == "__main__":
    if len(sys.argv)>1:
        url=urls(URL,sys.argv[1])
        soup=getWords(url)
        print(soup)