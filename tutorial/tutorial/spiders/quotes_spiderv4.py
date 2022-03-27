import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotesv4"
    start_urls = [
        "https://quotes.toscrape.com/page/1/",
    ]

    def parse(self, response):
        autores_pagina_link = response.css(".author + a")
        # autores_pagina_link = response.css("div.quote a::attr(href)").getall()
        yield from response.follow_all(autores_pagina_link, self.parse_autor)

        # proxima_pagina = response.css("li.next a::attr(href)").get()
        # if proxima_pagina is not None:
        #     yield response.follow(proxima_pagina, callback=self.parse)

        paginacao_links = response.css("li.next a::attr(href)").get()
        yield response.follow(paginacao_links, self.parse)

    def parse_autor(self, response):
        def extract_with_css(query):
            return response.css(query).get(default="").strip()

        yield {
            "nome": extract_with_css(".author-title::text"),
            "data_nascimento": extract_with_css(".author-born-date::text"),
            "bio": extract_with_css(".author-description::text"),
            "url": response.url,
        }
