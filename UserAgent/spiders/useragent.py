import scrapy
from UserAgent.items import UseragentItem


class UseragentSpider(scrapy.Spider):
    name = 'useragent'
    allowed_domains = ['useragentstring.com']
    start_urls = [
        'https://www.useragentstring.com/pages/useragentstring.php'
    ]

    def parse(self, response, **kwargs):
        links = response.xpath('//*[@id="auswahl"]//a[@class="unterMenuTitel"]/@href').extract()
        for link in links:
            if not link.strip().endswith('/pages/All/'):
                yield response.follow(link.strip(), callback=self.parse_item)

    def parse_item(self, response):
        item = UseragentItem()
        item['category'] = response.xpath('//*[@id="liste"]/h2/text()').get().lstrip('List of all ')
        h4_sites = response.xpath('//*[@id="liste"]/h4')
        for h4_site in h4_sites:
            sites = h4_site.xpath('following-sibling::ul[1]/li/a')
            for site in sites:
                item['link'] = site.xpath('@href').extract().strip()
                item['useragent'] = site.xpath('text()').extract_first().strip()
                yield item
