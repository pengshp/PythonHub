import requests
import json
import sys

# sys.reload()
# reload(sys)

# sys.setdefaultencoding('utf8')
# sys.setdefaultencoding('utf8')
# url='https://httpbin.org/post'
url = 'http://passport.elecfans.com/login?'
# url='http://bbs.elecfans.com/member.php?mod=logging&action=login'
s = requests.Session()
mydata = {'account': '1723549711@qq.com', 'password': 'xxxxxxxx'}
header = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0'}
req = s.post(url, data=mydata, headers=header)
# print("登录成功！")
# print(req.text.decode('utf-8'))
