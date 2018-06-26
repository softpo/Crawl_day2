import urllib
import urllib.request

# HttpHandler 类似

# proxies = {'http':'121.10.1.181:8080'}
proxies = {'http':'202.138.127.66:80'}

proxyHandler = urllib.request.ProxyHandler(proxies=proxies)

opener = urllib.request.build_opener(proxyHandler)

response = opener.open(fullurl='http://www.baidu.com/')

print(response.read().decode('utf-8'))