#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import requests
import json
import html2text
import os
import errno
import re
import StringIO
import urllib


###################################
## 아래 5개 정보만 본인 상황에 맞게 바꿔주세요
###################################

myblog = "jkpaper"       # 블로그 주소입니다. xxx.tistory.com
accesstoken = "abcdefg"  # 엑세스 토큰. 원래 엄청 깁니다
download_img = True      # 각 포스팅에 게재된 이미지도 다 다운받습니다. 원치 않으면 False 로 바꿔주세요

doc_no_min = 1      # 시작 문서 번호
doc_no_max = 269    # 종료 문서 번호
                    # 위와 같이 적은 경우엔 jkpaper.tistory.com/1 부터 jkpaper.tistory.com/269 사이의 269개 포스팅을 백업합니다.




h = html2text.HTML2Text()
h.ignore_links = True

def create_folder(filename):
    if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

def save_doc(r):
        
    link_list = []
    ref_list = []
    catid   = r['tistory']['item']['categoryId']
    docid   = r['tistory']['item']['id']
    date    = r['tistory']['item']['date']
    title   = r['tistory']['item']['title']
    content = r['tistory']['item']['content']
        
    if not catid:
        catid = 'no_category'
        
    folder = myblog + '/' + catid + '/' + docid
    filename = folder + '/' + date + '.md'
    create_folder(filename)

    try:
        final = h.handle(content).encode('utf8')
        
        
        buf = final.split('\n')
        
        for k, line in enumerate(buf):
            links = re.findall(r'!\[\]\((.*?)\)', line)

            newline = ''
            for l in links:
                link_list.append(l)
                i = len(ref_list)

                ref = '[link{}]:{}'.format(i, l)
                newline += '![][link{}]'.format(i)
                ref_list.append(ref)

            if len(links) > 0:
                buf[k] = newline

        buf.extend(ref_list)

        with open(filename, 'w') as f:
            f.write(title.encode('utf8') + '\n')
            f.write(date + '\n')

            for line in buf:
                f.write(line + '\n')


        if download_img:
            for k, link in enumerate(link_list):
                fillname = folder + '/' + str(k) + '.jpg'
                create_folder(fillname)
                urllib.urlretrieve(link, fillname)

    except UnicodeEncodeError as e:
        print e



def backup_blog(mn, mx):
    index = 0
    headers = {'Content-Type': 'application/json; charset=utf-8'} 
    url = "https://www.tistory.com/apis/post/read"

    for i in range(mn, mx):        
        parms = {'access_token': accesstoken,
                 'blogName': myblog,
                 'postId': i,
                 'output': 'json'}
               
        index += 1
        s = requests.get(url, headers=headers, params = parms)
    
        if s.status_code == 200:
            print i
            save_doc(s.json())
        else:
            print s.text
                    

if __name__ == "__main__": 
    backup_blog(doc_no_min, doc_no_max + 1)
    
