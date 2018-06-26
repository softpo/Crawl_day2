import urllib
import urllib.request

url = 'http://www.sdfghjertyuidfghjcvbnghj.com'

try:
    response = urllib.request.urlopen(url=url)
except Exception as e:
    print(e)
#     发起联网请求
#   错误，发给服务器，log，方便程序员，修改代码


print(response.read().decode('utf-8'))