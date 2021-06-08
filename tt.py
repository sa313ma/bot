import requests
import os
import logging

# def get_https_proxies():
#     url = 'https://free-proxy-list.net/'
#     response = requests.get(url)
#     parser = fromstring(response.text)
#     httpsProxies = set()
#     for i in parser.xpath('//tbody/tr')[:10]:
#         if i.xpath('.//td[7][contains(text(),"yes")]'):
#             #Grabbing IP and corresponding PORT
#             proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
#             httpsProxies.add(proxy)
#     return httpsProxies


# # Sadegh-khan: Get list of free-proxy (http) from free-proxy-list.net
# def get_http_proxies():
#     url = 'https://free-proxy-list.net/'
#     response = requests.get(url)
#     parser = fromstring(response.text)
#     httpProxies = set()
#     for i in parser.xpath('//tbody/tr')[:20]:
#         if i.xpath('.//td[7][contains(text(),"no")]'):
#             #Grabbing IP and corresponding PORT
#             proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
#             httpProxies.add(proxy)
#     return httpProxies

# proxies = get_https_proxies()
# print(proxies)
# httpProxies = get_http_proxies()
# print(httpProxies)





print(os.environ.get('http_proxy'))
print(os.environ.get('https_proxy'))


# os.environ['http_proxy'] ='localhost:9150'
# print(os.environ.get('http_proxy'))


proxies = {
    #'http': 'http://175.143.37.162:80',
    #'https': 'http://194.213.43.166:60530',
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050',
}

url = 'https://httpbin.org/ip'
url2 = 'https://telegram.org/'
url3 = 'http://example.org'
url4 = 'http://youtube.com'
 
r=requests.get(url3, proxies=proxies)
print(r)

s=requests.get(url, proxies=proxies)
print(s)

response = requests.get(url2,proxies=proxies)
print(response.json())



