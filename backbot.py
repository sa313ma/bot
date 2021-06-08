# import urllib.request

# # with urllib.request.urlopen('http://www.telegram.org/') as f:print(f.read(300))


# # with urllib.request.urlopen('http://www.python.org/') as f:print(f.read(100).decode('utf-8'))


# f = urllib.request.urlopen('http://www.python.org/')
# print(f.read(100).decode('utf-8'))



# import urllib3
# http = urllib3.PoolManager()
# r = http.request('GET', 'http://httpbin.org/robots.txt')
# r.status
# print(r.status)
# r.data
# print(r.data)

# r = http.request('POST','http://httpbin.org/post', fields={'hello': 'world'})
# print(r.headers)

# print(r)
