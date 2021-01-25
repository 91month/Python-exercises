import urllib.request
#response=urllib.request.urlopen("http://placekitten.com/g/500/600")
rep=urllib.request.Request("http://placekitten.com/g/500/600")
response = urllib.request.urlopen(rep)#这句和上句等于上面注释掉的那句
A=response.geturl()#地址
B=response.info()
print(A,'\n',B)
cat_img = response.read()
with open('cat.jpg','wb') as f:
    f.write(cat_img)








