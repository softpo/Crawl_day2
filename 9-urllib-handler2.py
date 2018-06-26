import urllib
import urllib.request

http_handler = urllib.request.HTTPHandler()


opener = urllib.request.build_opener(http_handler)
# 方式一，直接使用opener发起请求

# 方式二，将opener作为参数设置给urllib.request.urlopen
# opener去全局的联网请求
urllib.request.install_opener(opener)


# urllib.request.urlopen() 相当于使用opener.open()
response = urllib.request.urlopen('http://www.baidu.com/')
print(response.read().decode('utf-8'))