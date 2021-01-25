import urllib.request
import os
import time
import re

global page_num
def url_open(url):
    rep=urllib.request.Request(url)
    rep.add_header('user-agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0')
    response = urllib.request.urlopen(url)
    html = response.read()
    
    return html

def get_page(url):
    print("Anime pictures and wallpapers图片爬虫下载系统")
    print("Ps:页面不存在时，已打印错误")
    page = input("请输入图片序列（1-599000）：")#599503
    return page

def get_number_range():
    number_range=input("请输入图片编号的范围(0-20):")
    return number_range


def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_addrs = []

    a = html.find('get_image')
    while a!= -1:
        b = html.find('.jpg',a,a+255)
        if b != -1:
            #print('+++++++')#测试
            tou='https://anime-pictures.net/pictures/get_image'
            wei=html[a+9:b+4]
            
            index = tou+wei
            #index.replace('\n','')#去掉多余的\n\t\t\t\t\t\t\t\t
            #index.replace('\t','')
            #print('*****')#测试
            #re.sub('[\n\t]','',index)
            
            #print(index)#测试
            img_addrs.append(index)
        else:
            b=a+9
        a = html.find('get_image',b)
    #print(img_addrs)#测试
    
    return img_addrs

def save_imgs(folder,img_addrs):
    
    for each in img_addrs:
        filename = each.split('/')[-1]
        
        with open(filename,'wb') as f:
            img = url_open(each)
            f.write(img)
    
def downloadpic(folder='Pic',pages=5):
    
    url = "https://anime-pictures.net/"
    global page_num
    page_num = int(get_page(url))
    pages = int(get_number_range())
    
    for i in range(pages):
        page_num -= i
        page_url = url +'pictures/view_post/'+str(page_num) +'?lang=en'
        try:
            img_addrs = find_imgs(page_url)
            if img_addrs!=[]:
                save_imgs(folder,img_addrs)
                print(page_num,'\n','该编号的图已经保存到Pic文件夹')
                
                time.sleep(1)
            else:
                continue
        except urllib.error.URLError as e:
            print(e)
            
if __name__ == '__main__':
    downloadpic()
