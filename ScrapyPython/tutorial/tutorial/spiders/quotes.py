import scrapy
from tutorial.items import QuoteItem, QuoteItemLoader



class QuotesSpider(scrapy.Spider):
    name = "quotes"     #Nombre de la spider
    start_urls = ['https://quotes.toscrape.com/']     #Que urls va a scrapear

    def start_requests(self):
        base_url = "https://quotes.toscrape.com/page/"

        for page in range(1, 11):
            print(page)
            yield scrapy.Request(url=f'{base_url}{page}', callback=self.parse)

    #Definimos como scrappy va encontrar las quotes. Usamos el CSS SELECTOR, en el inspect para seleccionar las partes que queremos.
    #Ver que tiene el html y saber que queremos pulear de eso. Por ejemplo algho generico es usar la clase.
    def parse(self, response):
        for quote in response.css('.quote'):                                    #Aca decimos que parte del css
            loader = QuoteItemLoader(item=QuoteItem(), selector=quote)        #En yield abrimos un objeto json y definimos variables dentro de esa quote.

            loader.add_css('quote','.text::text')             #Al ir por cada elemento que coincida con nuestra condicion, va a crear un array.
            loader.add_css('author','.author::text') 
            loader.add_css('tags','.tags .tag::text')     #Join permite unir los tags en un solo campo de un array con un separador seleccionado.
            item =  loader.load_item()
            yield item
        #Encontrar en el inspect la clase que sirva para identificar el boton de next o siguiente para la paginacion
        next_page = response.css('.next > a::attr(href)').get()   #Le parseamos el atributo que necesitammos
        # next_page_disabled = response.css('.next > a[disabled]').get()
        if next_page: 
        #and not next_page_disabled:
            yield response.follow(next_page, self.parse)
            
