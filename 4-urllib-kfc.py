import urllib
import urllib.request
import urllib.parse

# ajax post
url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=pid'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}

# get
url_get = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=pid&cname=&pid=31&pageIndex=8&pageSize=10'

'''
cname=&pid=31&pageIndex=8&pageSize=10
'''




if __name__ == '__main__':

    city = input('请输入查询城市：')

    page = int(input('请输入查询多少页：'))

    for p in range(1,page+1):
        form = {'cname': city,
                'pid': 31,
                'pageIndex': p,
                'pageSize': 50}
        form = urllib.parse.urlencode(form).encode('utf-8')
        request = urllib.request.Request(url=url,data=form,headers=headers)

        response = urllib.request.urlopen(request)

        content = response.read().decode('utf-8')

        with open('./download/肯德基第%d页.json'%(p),mode='wb') as fp:
            fp.write(content.encode('utf-8'))