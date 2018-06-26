import urllib
import urllib.request



import re

'''  <tr class="">
    <td class="country"><img src="./免费代理IP_HTTP代理服务器IP_隐藏IP_QQ代理_国内外代理_西刺免费代理IP_files/cn.png" alt="Cn"></td>
    <td>117.69.201.186</td>
    <td>23887</td>
    <td>安徽淮北</td>
    <td class="country">高匿</td>
    <td>HTTPS</td>
      <td>1分钟</td>
    <td>9分钟前</td>
  </tr>'''

pattern = r'<td>([\d\.a-zA-Z\/]+)</td>'

with open('./proxy.html',mode='r',encoding='utf-8') as fp:
    proxy = fp.read()
    p = re.compile(pattern=pattern)
    proxies = re.findall(pattern=p,string = proxy)

    print(proxies)
    print(len(proxies))