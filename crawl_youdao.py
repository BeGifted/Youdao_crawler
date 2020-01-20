"""
有道翻译爬虫

Version: 0.1 
Author: gongyuandaye
"""

import requests
from lxml import etree
import json
import time

def crawl(url, data, headers):
    response = requests.post(url, data = data, headers = headers)
    html = response.text
    target = json.loads(html)
    print('翻译结果：%s' % target['translateResult'][0][0]['tgt'])

if __name__ == "__main__":
    url = 'http://fanyi.youdao.com/translate'
    while True:
        content = input("请输入需要翻译的内容(输入Z退出)：")
        if content == 'Z':
            break
        data = {
            'i': content,
            'from': 'AUTO',
            'to': 'AUTO',
            'smartresult': 'dict',
            'client': 'fanyideskweb',
            'doctype': 'json',
            'version': '2.1',
            'keyfrom': 'fanyi.web',
            'action': 'FY_BY_REALTlME'
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
        }
        crawl(url, data, headers)
        time.sleep(3)


