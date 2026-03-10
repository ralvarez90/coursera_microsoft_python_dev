import os

import scrapy


class MySpider(scrapy.Spider):
    # 1. Nombre único para identificar la araña
    name = 'my_spider'

    # 2. URLs donde empezará a buscar
    start_urls = ['https://espanol.yahoo.com/?p=us']

    # 3. Procesa la respuesta de la web
    def parse(self, response):
        # Extract the title of the page
        title = response.css('title::text').get()

        # Extract all the paragraph text
        paragraphs = response.css('p::text').getall()

        # Save results
        yield {
            'title': title,
            'paragraphs': paragraphs,
        }
