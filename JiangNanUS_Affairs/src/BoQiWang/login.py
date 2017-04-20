import urllib.request
import http.cookiejar
import json



#加入对cookies的支持
cookieJarInMemory = http.cookiejar.CookieJar();
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookieJarInMemory));
urllib.request.install_opener(opener);

url_login='http://www.boqii.com/site/User/usercenter'
#创建Request对象
request = urllib.request.Request(url_login)
#添加数据
#添加http header
request.add_header('Host', 'www.boqii.com')
request.add_header('Connection', 'keep-alive')
request.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.8.2000 Chrome/30.0.1599.101 Safari/537.36')
request.add_header('Content-Type','application/x-www-form-urlencoded')
request.add_header('DNT','1')
request.add_header('Referer','http://www.pocketuni.net/')
#还需要解码
#request.add_header('Accept-Encoding','gzip,deflate')
request.add_header('Accept-Language','zh-CN')

#POST_Data
post_data = {'action' : 'login',
'username' : '18861823199',
'password' : 'woaiwojia',
'password' : 'userpassword',
'remember' : '0',
'verify' : 'xua0',
}
post_data_code= urllib.parse.urlencode(post_data).encode(encoding='UTF8')
#发送请求
response = urllib.request.urlopen(request,data=post_data_code,timeout=60)
#保存网页内容
context = response.read().decode('UTF8')
#输出网页内容
print(context)

    




