import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class NhadatbanSpider(CrawlSpider):
    name = 'nhadatban'
    allowed_domains = ['alonhadat.com.vn']
    url = 'https://alonhadat.com.vn/nha-dat/can-ban/trang--{}.html'

    def start_requests(self):
        for i in range(1, 31458):
            yield scrapy.Request(self.url.format(i))
    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='content-item']/div/div[@class='ct_title']/a"),
             callback='parse_item', follow=True),

    )

    def parse_item(self, response):
        yield {
            'Tên ': response.xpath("//div[@class='content plp']/div/div/div/h1/text()").get(),
            'Địa chỉ': response.xpath("(//div[@class='content plp']/div/div/div[4]/span/text())[2]").get(),
            'Giá': response.xpath("(//div[@class='content plp']/div/div/div[3]/span/span[2]/text())[1]").get(),
            'Diện tích': response.xpath("(//div[@class='content plp']/div/div/div[3]/span/span[2]/text())[2]").get(),
            'Loại tin': response.xpath("//div[@class ='moreinfor1']/div/table//tr[2]//td[2]//text()").get(),
            'Loại BDS': response.xpath("//div[@class ='moreinfor1']/div/table//tr[3]//td[2]//text()").get(),
            'Pháp lý': response.xpath("//div[@class ='moreinfor1']/div/table//tr[3]//td[4]//text()").get(),
            'Chiêu ngang': response.xpath("//div[@class ='moreinfor1']/div/table//tr[4]//td[2]//text()").get(),
            'Chiêu dài': response.xpath("//div[@class ='moreinfor1']/div/table//tr[5]//td[2]//text()").get(),
            'url': response.url,
        }
