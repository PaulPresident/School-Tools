import scrapy
from scrapy.http import FormRequest

class crawler(scrapy.Spider):
    name = 'login'
    start_urls = ['https://pamt-sapphire.k12system.com/CommunityWebPortal/Welcome.cfm']

    def parse(self, response):
        csrf_token = 'BE9A2E8ABEA6650585E801319060B1025753D5D5'
        yield FormRequest.from_response(response, formdata={'csrf_token': csrf_token, 'j_username': '2022sedrapo', 'j_password': '1016335', 'j_pin': '36415'}, callback=self.parse_after_login)

    def parse_after_login(self, response):
        # this most likely did not send me to the link idk tho
        # scrapy.Request(url='https://pamt-sapphire.k12system.com/CommunityWebPortal/Backpack/StudentClasses.cfm?STUDENT_RID=1106151')
        cum = str(response.body)
        print(cum) # prints the body
        cum = re.sub('\\n', ' ', cum)
        # i still do not know how to scrape fuck
        grade = response.xpath('/html/body/div[2]/table/tbody/tr[3]/td[2]/table/tbody/tr/td[2]/div[3]/table/tbody/tr[3]/td[1]').getall()
        print(grade)
        yield grade