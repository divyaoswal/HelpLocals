import scrapy


class CraigslistSpider(scrapy.Spider):
    name = "craigslist"

    def start_requests(self):
        urls = [
            "https://sfbay.craigslist.org/search/zip"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for post_url in response.css("li.result-row a.result-image::attr(href)").extract():
            yield scrapy.Request(url=response.urljoin(post_url), callback=self.parse_post_url)

        next_page = response.css("a.next::attr(href)").extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def parse_post_url(self, response):
        desc =  response.css('section#postingbody::text').extract()
        yield {
            "image_url": response.css('div.swipe-wrap img::attr(src)').extract_first(),
            "title": response.css('span#titletextonly::text').extract_first(),
            "location": response.css('span.postingtitletext small::text').extract_first(),
            "description": "".join(desc).strip().split("\n")        
        }
