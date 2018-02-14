#크롤링 객체
import urllib.request
import urllib.parse
import file_inscriber
import json

class NaverCrawler:

    info_file='naver_info.json'
    site_of_crawling='네이버'

    def __init__(self, keyword):
        with open(self.info_file, encoding='utf-8') as f:
            info=json.load(f)
            self.option_arr=info["options"]
            self.option_url_list=info["options_url"]
            self.client_id=info["client_id"]
            self.client_secret = info["client_secret"]
            self.base_url=info["base_url"]
        self.display_arr=[]
        self.keyword = keyword
        self.keyword_url = urllib.parse.quote(self.keyword)
        self.file_name=self.site_of_crawling+' '+keyword+' 검색결과.txt'

        self.setDisplay()

    def setDisplay(self):
        iteration = 0
        while iteration < len(self.option_arr):
            print(self.option_arr[iteration])
            print('해당 자료를 얼마만큼 가져올까요?(가져온다면 10-100개 범위, 가져오지 않는다면 0을 입력해주세요.)')
            displayText = input()
            displayInput = int(displayText)
            while displayInput < 10 or displayInput > 100:
                if displayInput == 0:
                    break
                print('자료는 10개 이상 100개 이하로만 가져올 수 있습니다. 다시 입력해주세요.')
                print('해당 자료를 얼마만큼 가져올까요?(10-100개 범위)')
                displayText = input()
                displayInput = int(displayText)
            self.display_arr.append(displayInput)
            iteration += 1

    def makeRequest(self, idx):
        option=self.option_arr[idx]
        opt_url=self.option_url_list[idx]
        display=self.display_arr[idx]
        request_url=self.base_url+opt_url+'?query='+self.keyword_url+'&display='+str(display)
        request=urllib.request.Request(request_url)
        request.add_header('X-Naver-Client-Id', self.client_id)
        request.add_header('X-Naver-Client-Secret', self.client_secret)
        response=urllib.request.urlopen(request)
        rescode=response.getcode()
        if rescode==200:
            response_content=response.read()
            inscriber=file_inscriber.FileInscriber(response_content, option, self.file_name)
            inscriber.inscribeFile()
        else:
            print("Error Code:"+rescode)


    def implementRequest(self):
        for idx in range(len(self.option_arr)):
            if self.display_arr[idx]:
                self.makeRequest(idx)




