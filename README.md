# 티스토리 블로그 백업

지금 읽고 계시는 '마크다운'(md) 문서 포맷으로 블로그를 백업 받습니다. 아래 모든 과정은 터미널 기준으로 설명합니다.



사전 준비물
-----------
* 파이썬 
* 본인 블로그의 access token 



설치
------------

**파이썬 및 확장 모듈 설치**

    sudo apt-get install python
    sudo apt-get install pip
    sudo apt-get install build-essential python-dev
    sudo pip install html2text

[**backupBlog.py 파일 다운로드**][1]

  
  
  
  
실행 전 코드 세팅
-----------

**엑세스 토큰 얻기**

* [티스토리 클라이언트 등록][2]
* `서비스 url, callback 경로`에 블로그 주소 기입 
```
백업할블로그.tistory.com
```
* client id를 확인
* 주소 창에 아래 코드 붙여넣고 엔터
```
https://www.tistory.com/oauth/authorize?client_id=아이디&redirect_uri=http://사이트.tistory.com&response_type=token
```
 
* 아래와 같은 내용이 주소창에 뜨는데, '내 엑세스 토큰'을 복사합니다.
```
 http://jkpaper.tistory.com/#access_token=내 엑세스 토큰&state=
```
######주의: access_token은 일정시간 후에 만료되므로 코드 실행 중 access_token에러가 난다면 위 4번부터 반복
  
  
  
**backupBlog.py 파일 세팅**

* 백업할 폴더로 파일 옮김 
> backupBlog.py이 위치한 폴더에 'jkpaper' 폴더가 생기고 그 하위에 모두 복사합니다.
* text 에디터 등으로 **backupBlog.py** 파일 오픈
* 아래 부분만 바꾸고 저장
  
  ![backup_pre]
 
 
   
   
   
코드 실행
-----------

**터미널에서 아래 코드 입력**

  `python backupBlog.py`
  
  
  
**백업 중**
 
  > 위 코드를 입력하면 터미널에 아래 이미지처럼 백업받는 문서번호가 뜹니다.
  > error 메시지가 뜬 경우는 해당 문서가 없거나, 엑세스 토큰이 만료된 경우 등이 있습니다.

![backup_on] 



**백업 완료 후, 폴더 구조**


> 아래와 같이 폴더 구조가 생기고, 각 문서 폴더에 포스팅 및 이미지 등이 모두 위치합니다.
> `내 블로그명 - 카테고리 번호 - 문서 번호`

![backup_done] 

  


**백업 완료 후, 문서 구조**

  > 마크다운 문법입니다. 티스토리에 생성된 html은 매우 지져분하죠. 깨끗한 마크다운 문서를 원본으로 보관하길 강추합니다.
  > 문서 상단 첫줄,둘째줄에 제목과 작성일이 있습니다.
  
![doc_first]
	
  > 사진 링크는 깨끗하게 모두 참조 형식으로 문서 하단으로 밀었습니다.
    
![doc_last]



[1]:https://github.com/johnjkjung/backup-blogpost/blob/master/backupBlog.py
[2]:http://www.tistory.com/guide/api/manage/register

[doc_first]:http://cfile2.uf.tistory.com/image/99110D3359DB95412E90B9
[doc_last]:http://cfile1.uf.tistory.com/image/994C663359DB954109B1E7
[backup_pre]:http://cfile24.uf.tistory.com/image/9970703359DB9543074753
[backup_on]:http://cfile24.uf.tistory.com/image/9970C23359DB9542072649
[backup_done]:http://cfile21.uf.tistory.com/image/99A7573359DB95421CD93B
