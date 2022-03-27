from subprocess import call
from tkinter.messagebox import YES
from pkg_resources import yield_lines
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotesv3"
    start_urls = [
        "https://quotes.toscrape.com/page/1/",
    ]

    def parse(self, response):
        for sitacao in response.css("div.quote"):
            # pegando o texto do span com class name text
            yield {
                # pegando o texto do span com class name text
                "texto": sitacao.css("span.text::text").get(),
                "autor": sitacao.css("small.author::text").get(),
                "tags": sitacao.css("div.tags a.tag::text").getall(),
            }
            proxima_pagina = response.css("li.next a::attr(href)").get()
            if proxima_pagina is not None:
                # proxima_pagina = response.urljoin(proxima_pagina)
                # yield scrapy.Request(proxima_pagina, callback=self.parse)

                yield response.follow(proxima_pagina, callback=self.parse)
