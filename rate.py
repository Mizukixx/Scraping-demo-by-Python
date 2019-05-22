#coding:utf-8
import requests
import json

PURPLE  = '\033[35m'
RED     = '\033[31m'
CYAN    = '\033[36m'
GREEN   = '\033[92m'
BLUE    = '\033[94m'
ENDC    = '\033[0m'


r = requests.get('https://www.smbc.co.jp/ex/ExchangeServlet?ScreenID=real')
r.encoding = r.apparent_encoding
text = r.text
now    = text.split('<p class="tRight">')[1].split('</p>')[0]
doller   = text.split('<td class="tRight num">')[1].split('</td>')[0].replace(',','')
euro       = text.split('<td class="tRight num">')[3].split('</td>')[0].replace(',','')
pond = text.split('<td class="tRight num">')[5].split('</td>')[0].replace(',','')

#print(text)
print('今現在の日時：',now)
print ('1米ドルあたりのレート： ',doller,'円')
print ('1ユーロあたりのレート：', euro, '円')
print ('1英ポンドあたりのレート：', pond, '円')

a=open('sharesrate.csv','w')
a.write('日時,米ドル,ユーロ,英ポンド\n')
a.write(now+','+doller+','+euro+','+pond+'\n')
a.close()

