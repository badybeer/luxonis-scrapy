import scrapy
import json
import re

class SrealitySpider(scrapy.Spider):
    name = 'sreality'
    start_urls = ['https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&page=0&per_page=500']

    def parse(self, response):
        response_json = json.loads(response.text)
        for flat in response_json.get('_embedded', {}).get('estates', []):
            title = flat.get('name')
            image_url = flat.get('_links', {}).get('images', [])[0].get('href')

            # Cleaning up the title to remove excessive whitespace
            title = re.sub(r'\s+', ' ', title).strip() if title else 'No title'

            # Yielding each flat's title and image URL
            yield {
                'title': title,
                'image_url': image_url
            }
