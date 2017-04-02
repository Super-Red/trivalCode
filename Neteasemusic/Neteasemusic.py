#-*-encoding:-utf-8-*-

"""
Author:     Super_Red
Date:       3/27/2017
Describe:   Download and display the most funny comment from NetEaseMusic
"""

import requests
from bs4 import BeautifulSoup
import json

def getCommentsFromMusicID(musicID="456310390"):
    url = "http://music.163.com/song?id={musicID}".format(musicID=musicID)
    r = requests.get(url)
    print (r.text)

id1 = "456310390"
url1 = "http://music.163.com/weapi/v1/resource/comments/R_SO_4_456310390?csrf_token=333778e65c07cb35088ec2165cf3b990"
id2 = "34497630"
url2 = "http://music.163.com/weapi/v1/resource/comments/R_SO_4_34497630?csrf_token=852f492db32a870d125a08b80a0d3171"


