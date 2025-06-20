# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import MapCompose, Join, TakeFirst
from scrapy.loader import ItemLoader

#Items features:
#Parte de la practica de Items y Items loaders Definimos una funcion para hacer uppercase a nuestra data y la ponemos en nuestro item.
#Es best practice de definir los Items y sus procesadores aca y no en la spider. Escabilidad y prolijidad.

def to_uppercase(value):
    return value.upper()

class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class QuoteItem(scrapy.Item):
    quote = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field(input_processor = MapCompose(to_uppercase), output_processor = Join(', '))

    #Porque usar estos items, en lugar de diccionarios como hicimos en quote -> yield{'quote': quote.css('.text::text').get()}
    #Porque los items nos permiten mantener y escalar el proceso.

class QuoteItemLoader(ItemLoader):
    default_output_processor = TakeFirst()