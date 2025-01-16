import scrapy
import json

class WeatherSpider(scrapy.Spider):
    name = 'weather'
    allowed_domains = ['openweathermap.org']
    
    api_key = 'd0e8713563e5716c5103a0acfb1298cc'
    base_url = 'https://api.openweathermap.org/data/2.5/weather'

    cities = ['London', 'New York', 'Tokyo']
    
    def start_requests(self):
        for city in self.cities:
            url = f'{self.base_url}?q={city}&appid={self.api_key}&units=metric'
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        data = json.loads(response.body)

        yield {
            'Ciudad': data.get('name'),
            'Temperatura': data.get('main', {}).get('temp'),
            'Humedad': data.get('main', {}).get('humidity'),
            'Clima': data.get('weather', [{}])[0].get('description'),
        }