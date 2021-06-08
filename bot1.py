import telepot
import time
import urllib3
import requests

import os
print(os.environ.get('http_proxy'))

# torport = 9050
# proxies={
#     'http':"socks5h://127.0.0.1:{}".format(torport),
#     'https':"socks5h://127.0.0.1:{}".format(torport)
# }

# r=requests.get('https://youtube.com', proxies=proxies)
# print(r)
# proxies = {
#  "http": "http://10.10.10.10:8000",
#  "https": "http://10.10.10.10:8000",
# }
# r = requests.get("http://toscrape.com", proxies=proxies)



# You can leave this bit out if you're using a paid PythonAnywhere account
# proxy_url = "http://proxy.server:3128"
# telepot.api._pools = {
#     'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
# }
# telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))
# end of the stuff that's only needed for free accounts

# set http_proxy=http://proxy.myproxy.com
# set https_proxy=https://proxy.myproxy.com

# bot = telepot.Bot('1258007118:AAEcye1ZFyIwn1BT9EdJ6Jo6cYNaQE4T11M')

# def handle(msg):
#     content_type, chat_type, chat_id = telepot.glance(msg)
#     print(content_type, chat_type, chat_id)

#     if content_type == 'text':
#         bot.sendMessage(chat_id, "You said '{}'".format(msg["text"]))


# bot.message_loop(handle)

# print ('Listening ...')

# # Keep the program running.
# while 1:
#     time.sleep(10)