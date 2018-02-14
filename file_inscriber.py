import json

class FileInscriber:
    def __init__(self, response_content, option, file_name):
        self.response_content=response_content
        self.option=option
        self.file_name=file_name


    def inscribeFile(self):
        data = json.loads(self.response_content.decode('utf-8'))
        items = data["items"]
        for item in items:
            title = item["title"]
            link = item["link"]
            description = item["description"]
            with open(self.file_name, 'a', encoding='utf-8') as f:
                f.write(self.option + '\n')
                json.dump(title, f, skipkeys=True, ensure_ascii=False, indent='\t')
                f.write('\n')
                json.dump(link, f, skipkeys=True, ensure_ascii=False, indent='\t')
                f.write('\n')
                json.dump(description, f, skipkeys=True, ensure_ascii=False, indent='\t')
                f.write('\n')
                f.write('\n')

         ###html 파일로 쓰기