import urllib
import urllib.request
import os
# 115.28.67.91:16817

# 将用户名密码和ip保存到环境变量中

pw = os.environ.get('password')

proxyServer = os.environ.get('proxyServer')

user = os.environ.get('proxyuser')

print(pw,proxyServer,user)
proxies = {'http':'%s:%s@%s'%(user,pw,proxyServer)}

proxy_handler = urllib.request.ProxyHandler(proxies=proxies)


opener = urllib.request.build_opener(proxy_handler)

response = opener.open('http://www.baidu.com/')

print(response.read().decode('utf-8'))