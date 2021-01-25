import urllib.request
import requests
import urllib.parse
import json
import time
#有道翻译(带隐藏改进)          201713160123覃方圆制作
def Youdaoimprove():
    while True:
        
        content = input("翻译方式：自动检测\n请输入要翻译的内容：")
        #Network下的post文件查看
        url ='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
        #head={}
        #head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'
        data={}
        data['i']=content
        data['from']='AUTO'
        data['to']='AUTO'
        data['smartresult']='dict'
        data['client']='fanyideskweb'
        data['salt']='15594461036516'
        data['sign']='7c449d8a558ac97aaef2fb9288126fe3'
        data['ts']='1559446103651'
        data['bv']='f355c521b6e13c15aa35c72a097b7786'
        data['doctype']='json'
        data['version']='2.1'
        data['keyfrom']='fanyi.web'
        data['action']='FY_BY_REALTlME'

        data=urllib.parse.urlencode(data).encode('utf-8')

        req = urllib.request.Request(url,data)
        req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0')
        response=urllib.request.urlopen(req)
        
        html = response.read().decode('utf-8')

        #不能直接print(html)，需要处理后打印
        target= json.loads(html)
        target= target['translateResult'][0][0]['tgt']
        print("有道翻译结果:%s" %(target))
        time.sleep(3)

#百度翻译
def Baidu():
    content = input("请输入要翻译的内容：")
    url = "http://fanyi.baidu.com/basetrans"
    data = {
        "query":content,
        "from":"zh",
        "to":"en",
    }
    headers = {
        "User-Agent":"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36",
            }

    response = requests.post(url,data = data,headers = headers)
    # print response.request.url     #请求地址
    # print response.url              #响应地址
    # print response.request.headers  #请求头
    # print response.headers          #响应头
    print (response.content.decode('unicode-escape'))    #显示出来unicode的中文
    # print response.text        
print("201713160123覃方圆制作")
Youdaoimprove()


