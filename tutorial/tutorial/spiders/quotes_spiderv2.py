from subprocess import call
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotesv2"
    start_urls = [
        "https://quotes.toscrape.com/page/1/",
        "https://quotes.toscrape.com/page/2/",
    ]

    def parse(self, response):
        # PEGA O TEXTO DO TITULO USANDO CSS
        response.css("title::text").get()
        # PEGA O TEXTO DO TITULO USANDO CSS e expressões regulares
        response.css("title::text").re(r"(\w+) to (\w+)")
        response.css("title::text").re(r"Q\w+")

    def parse_1(self, response):
        # usando o XPATH
        # LINK DETALHADO DE COMO USAR O xpath
        # https://docs.scrapy.org/en/latest/topics/selectors.html#topics-selectors
        # http://zvon.org/comp/r/tut-XPath_1.html
        response.xpath('//title')
        response.xpath('//title/text()').get()

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        with open(filename, "wb") as f:
            f.write(response.body)
