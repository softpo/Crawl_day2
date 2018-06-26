import urllib
import urllib.request

urllib.request.urlopen(url='http://www.baidu.com')


# Request
# 构建请求，就是为了添加header，伪装成浏览器，获取登陆之后才能获取的数据（Cookie）

# Hanlder 引入，就是为了能够使用代理

httpHandler = urllib.request.HTTPHandler()

# 打开一个网址
opener = urllib.request.build_opener(httpHandler)

# 使用opener访问网络数据  urllib.request.urlopen()
request = urllib.request.Request(url='http://www.baidu.com/')

# response = opener.open(fullurl='http://www.baidu.com/')
response = opener.open(request)

print(response.read().decode('utf-8'))