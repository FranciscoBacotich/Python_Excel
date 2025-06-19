import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"     #Nombre de la spider
    start_urls = ['https://quotes.toscrape.com/']     #Que urls va a scrapear

    #Definimos como scrappy va encontrar las quotes. Usamos el CSS SELECTOR, en el inspect para seleccionar las partes que queremos.
    #Ver que tiene el html y saber que queremos pulear de eso. Por ejemplo algho generico es usar la clase.
    def parse(self, response):
        for quote in response.css('.quote'):                                    #Aca decimos que parte del css
            yield{                                                              #En yield abrimos un objeto json y definimos variables dentro de esa quote.
                'quote': quote.css('.text::text').get(),                        #Al ir por cada elemento que coincida con nuestra condicion, va a crear un array.
                'author':quote.css('.author::text').get(),                      #Podemos usar otras clases para definir las variables.
                'tags': quote.css('.tags .tag::text').getall(),
            }

        #Encontrar en el inspect la clase que sirva para identificar el boton de next o siguiente para la paginacion
        next_page = response.css('.next > a::attr(href)').get()   #Le parseamos el atributo que necesitammos
        if next_page:
            next_page_url = response.urljoin(next_page)     #Porque urlJoin: toma el url de la respuesta y lo une con el de next page
            yield scrapy.Request(next_page_url, callback=self.parse)    #Se llama asi misma pero con el nuevo url.
