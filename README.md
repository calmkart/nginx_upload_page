# mupload首页

------

## 部署指南

```shell
git clone 
#用mupload后台的requirement.txt即可
gunicorn -w4 -b 0:9527 runserver:app

```

注意，环境是python2    
请配合nginx-upload使用:       
https://github.com/calmkart/nginx_upload       
http://www.calmkart.com/?p=278      
