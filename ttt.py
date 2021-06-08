# import requests
# import logging
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters




# TOKEN='1258007118:AAEcye1ZFyIwn1BT9EdJ6Jo6cYNaQE4T11M'
# REQUEST_KWARGS={
#     'proxy_url': 'socks5://116.202.103.223:52433',
#     # Optional, if you need authentication:
#     # 'urllib3_proxy_kwargs': {
#     #     'username': 'PROXY_USER',
#     #     'password': 'PROXY_PASS',
#     # }
# }

# updater = Updater(TOKEN, request_kwargs=REQUEST_KWARGS)


import sys
from telegram.ext import Updater

TOKEN='1258007118:AAEcye1ZFyIwn1BT9EdJ6Jo6cYNaQE4T11M'
# Connecting through TOR@localhost

REQUEST_KWARGS={
    'proxy_url': 'socks5://116.202.103.223:52433',
    }
updater = Updater(TOKEN, request_kwargs=REQUEST_KWARGS)
pager = updater.bot
pager.send_message(chat_id=sys.argv[1], text=sys.argv[2])