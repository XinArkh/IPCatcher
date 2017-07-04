import requests
from bs4 import BeautifulSoup
def getip():
    session = requests.Session()
    headers = {"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Accept-Encoding":"gzip, deflate, sdch",
                "Accept-Language":"zh-CN,zh;q=0.8",
                "Cache-Control":"max-age=0",
                "Connection":"keep-alive",
                "Cookie":"ASPSESSIONIDSABACQDQ=OJPBFCMAPLBPCGINJOEJMGNC",
                "Host":"ip.myhostadmin.net",
                "Referer":"https://www.baidu.com/link?url=F67AnYGoj7ahIXm-iOKeZFGV095NIX06iGJHHCPVswSEFQ8snVoRlQY4hRFptayI&wd=&eqid=aac8acde00794b3c0000000258919a9f",
                "Upgrade-Insecure-Requests":"1",
                "User-Agent":"Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
    url = "http://ip.myhostadmin.net/"
    req = session.get(url, headers = headers)
    bsObj = BeautifulSoup(req.text)
    ipAddress = bsObj.find("h1", {"class":"STYLE1"}).get_text()
    return ipAddress