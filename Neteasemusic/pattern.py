# encoding=utf8

import requests
from bs4 import BeautifulSoup
import re, time
import os, json
import base64
from Crypto.Cipher import AES
from pprint import pprint
import codecs

Default_Header = {
                    'Referer':'http://music.163.com/',
                    'Host':'music.163.com',
                    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
                    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    'Accept-Encoding':'gzip, deflate, sdch'
}

BASE_URL = 'http://music.163.com'

_session = requests.session()
_session.headers.update(Default_Header)

def getPage(pageIndex):
    pageUrl = 'http://music.163.com/discover/playlist/?order=hot&cat=全部&limit=35&offset='+pageIndex
    soup = BeautifulSoup(_session.get(pageUrl).text, "html.parser")
    songList = soup.findAll("a", {'class':'tit f-thide s-fc0'})
    for i in songList:
        playListID = i["href"]
        getPlayList(playListID)

def getPlayList(playListID="/playlist?id=635022539"):
    playListUrl = BASE_URL + playListID
    soup = BeautifulSoup(_session.get(playListUrl).text, "html.parser")
    songList = soup.findAll("ul", {"class":"f-hide"})[0]
    for song in songList.findAll("a"):
        songID = song["href"].split("=")[1]
        getComment(songID)
   
def getComment(songID):
    pass

def aesEncrypt(text, secKey):
    pad = 16 - len(text) % 16
    text = text + pad * str(chr(pad))
    encryptor = AES.new(secKey, 2, '0102030405060708')
    ciphertext = encryptor.encrypt(text)
    ciphertext = base64.b64encode(ciphertext)
    return ciphertext

def rsaEncrypt(text, pubKey, modulus):
    text = text[::-1]
    rs = int(codecs.getencoder("hex")(bytes(text, "utf-8"))[0].decode(), 16) ** int(pubKey, 16) % int(modulus, 16)
    return format(rs, "x").zfill(256)

def createSecretKey(size):
    return ("".join(map(str, list(os.urandom(size)))))[:16]

def getComment(songID="446945324"):
    songUrl = BASE_URL + '/weapi/v1/resource/comments/R_SO_4' + str(songID) + '/?csrf_token='
    headers = {'Cookie':'appver=1.5.0.75771','Referer':'http://music.163.com'}
    text = {'username':'', 'password':'', 'rememberLogin':'true'}
    modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
    nonce = '0CoJUm6Qyw8W8jud'
    pubKey = '010001'
    text = json.dumps(text)
    secKey = createSecretKey(16)
    encText = aesEncrypt((aesEncrypt(text, nonce).decode()), secKey)
    encSecKey = rsaEncrypt(secKey, pubKey, modulus)
    data = {'params':encText, 'encSecKey':encSecKey}
    req = requests.post(songUrl, headers=headers, data=data)
    print(req.text)



