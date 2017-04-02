import requests
import re
from bs4 import BeautifulSoup

class Tencent(object):
    def __init__(self, comicID):
        self.original_url = "http://ac.qq.com/ComicView/index/id/{id}/cid/1".format(id=comicID)
        self.chapterList = self.getChapterList()

    def getChapterList(self):
        chapterList = []
        bsObj = BeautifulSoup(requests.get(self.original_url).text, "html.parser")
        for i in bsObj.findAll("a", {"title": re.compile("第[0-9]+话")}):
            chapterList.append((i["title"], i["href"]))
        return chapterList

    def getPicFromChapterUrl(self, chapterUrl):
        cha_bsObj = BeautifulSoup(requests.get(chapterUrl).text, "html.parser")
        pic_cover = re.findall(r'url = (.+?);', cha_bsObj.find("script").get_text())[0]



haizeiwang = Tencent(505430)


