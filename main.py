import urllib
import bs4
import re
import requests
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import socket
import socks

socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 1081)
socket.socket = socks.socksocket


def main():
    response = urllib.request.urlopen('https://www.mattkaydiary.com/')
    html = response.read().decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    thumb = soup.find_all("div", class_="thumb")[0]
    todayUrl = thumb.a.attrs['href']
    todayResponse = urllib.request.urlopen(todayUrl)
    todayHtml = todayResponse.read().decode('utf-8')
    todayBs = BeautifulSoup(todayHtml, 'html.parser')
    result = todayBs.find_all(text=re.compile("https://drive.google.com"))
    urlResuT = todayBs.find_all(text=re.compile("vmess://"))
    urlAll = []
    for x in urlResuT:
        urlAll.append(str(x))
    # urlStr = ""
    # url = urlStr.join(urlAll)

    open("./url.txt", "w").writelines(urlAll)


    v2ray = ""
    v2ray = "".join(result[0])
    v2ray = v2ray[v2ray.index("http"):]
    v2rayTxt = requests.request("GET", v2ray, verify=False)
    with open('./v2ray.txt', 'w') as f:
        f.write(v2rayTxt.text)
    clash = ""
    clash = "".join(result[1])
    clash = clash[clash.index("http"):]
    clashTxt = requests.request("GET", clash, verify=False)
    with open('./clash.txt', 'w', encoding="utf-8") as f:
        f.write(clashTxt.text)


# 主函数入口
if __name__ == '__main__':
    main()
