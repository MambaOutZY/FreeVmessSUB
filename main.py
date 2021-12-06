import urllib
import bs4
import re
import requests
from bs4 import BeautifulSoup
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



def main():
    resp = requests.get("https://hello.stgod.com/clash/proxies?nc=CN,c=HK,TW,JP&speed=20,100&type=vmess")
    with open('./v2ray.txt', 'w', encoding="utf-8") as f:
        f.write(resp.text)

    resp = requests.get("https://hello.stgod.com/clash/proxies?nc=CN,c=HK,TW,JP&speed=20,100&type=ss")
    with open('./ss.txt', 'w', encoding="utf-8") as f:
        f.write(resp.text)
    resp = requests.get("https://hello.stgod.com/clash/proxies?nc=CN,c=HK,TW,JP&speed=20,100&type=ssr")
    with open('./ssr.txt', 'w', encoding="utf-8") as f:
        f.write(resp.text)
    resp = requests.get("https://hello.stgod.com/clash/proxies?nc=CN,c=HK,TW,JP&speed=20,100&type=trojan")
    with open('./trojan.txt', 'w', encoding="utf-8") as f:
        f.write(resp.text)

# 主函数入口
if __name__ == '__main__':
    main()
