#API: 네이버 (json)
#     RISS, DBpia (xml)
#파싱: Google

import naver_crawler



#프로그램 시작과 검색어 입력(main의 맨 처음)(이 단계에 조사 원하는 플랫폼도 받기)
print('자료조사 도우미에 오신 것을 환영합니다. 과제 팟팅팟팅\n'
      '검색어를 입력해주세요.')
keyword=input()
#프로그램 시작과 검색어 입력 끝

#naver 크롤러 실행
naver_crawler=naver_crawler.NaverCrawler(keyword)
naver_crawler.implementRequest()

