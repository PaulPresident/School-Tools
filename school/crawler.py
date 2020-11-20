import scrapy

class crawler(scrapy.Spider):
    name = 'name'
    start_urls = ['https://pamt-sapphire.k12system.com/CommunityWebPortal/Welcome.cfm']

    def parse(self, response):
        scrapy.FormRequest.from_response(
            response,
            formdata={'j_username': '2022sedrapo', 'j_password': '1016335', 'j_pin': '36415'}
            # callback=self.after_login
        )

        grade = response.css('ul.StudentList li a.student::text').getall()
        yield {'grade': grade}