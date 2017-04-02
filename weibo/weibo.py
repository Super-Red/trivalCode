#-*-encoding:utf-8-*-

import requests
from bs4 import BeautifulSoup
import json
import csv

Default_Header = {
                    'Referer':'http://www.dianping.com',
                    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
                    'Host':'www.dianping.com'
}

_session = requests.session()
_session.headers.update(Default_Header)

def Main():
    BASIC_URL = "http://www.dianping.com/search/keyword/15/0_%E9%85%92%E5%BA%97"
    count = 0
    for i in range(508):
        url = BASIC_URL + "/p" + str(i+1)
        soup = BeautifulSoup(_session.get(url).text, "html.parser")
        hotelList = soup.findAll("div", {"class":"txt"})
        startList = [div.a.text for div in soup.findAll("div", {"class":"tag-addr"})]
        for i in range(len(hotelList)):
            meanPriceObj = hotelList[i].findAll("a", {"class":"mean-price"})[0]
            if not meanPriceObj.b:
                continue
            avePrice = meanPriceObj.b.text
            hotelID = meanPriceObj["href"].replace("/shop/", "")
            hotelName = hotelList[i].findAll("h4")[0].text
            hotelStart = startList[i]
            commentList = findComment(hotelID)
            data = [hotelID, hotelName, hotelStart, avePrice] + commentList
            writeListToFile(data)
            count += 1
            print ("成功保存:\t{count}\t{name}".format(count=count, name=hotelName))

def findComment(hotelID):
    url = "http://www.dianping.com/hotel/pc/hotelReview?shopId=" + hotelID
    result = json.loads(requests.get(url).text)["data"]
    commentList = [result["reviewCountAll"], ]
    for i in range(5):
        commentList.append(result["reviewCountStar"+str(5-i)])
    return commentList

def writeListToFile(data):
    with open("weiboXiamen.csv", "a", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(data)

Main()


