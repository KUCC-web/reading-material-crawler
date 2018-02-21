import json

class FileInscriber:
    def __init__(self, _crawler):
        self.option_response_dict=_crawler.option_response_dict
        self.file_name=_crawler.file_name


    def inscribeFile(self):
        key_list=self.option_response_dict.keys()
        with open(self.file_name, 'a', encoding='utf-8') as f:
            for key in key_list:
                response_content = self.option_response_dict[key].read()
                data = json.loads(response_content.decode('utf-8'))
                items = data["items"]

                for item in items:
                    title = item["title"]
                    link = item["link"]
                    description = item["description"]

                    f.write(key + '\n')
                    json.dump(title, f, skipkeys=True, ensure_ascii=False, indent='\t')
                    f.write('\n')
                    json.dump(link, f, skipkeys=True, ensure_ascii=False, indent='\t')
                    f.write('\n')
                    json.dump(description, f, skipkeys=True, ensure_ascii=False, indent='\t')
                    f.write('\n')
                    f.write('\n')



         ###html 파일로 쓰기