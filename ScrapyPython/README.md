# Introducción a Scrapy para Web Scraping

Vamos a utilizar **Scrapy** para extraer información de sitios web.  
Scrapy es una potente y popular biblioteca de Python especializada en **web scraping**.  
Sitio oficial: [https://www.scrapy.org/](https://www.scrapy.org/)

---

## ¿Qué es Scrapy?

Scrapy es un **framework** que permite desarrollar programas llamados **arañas** (*spiders*) para recorrer sitios web y extraer datos.  
Funciona principalmente sobre HTML estático. **No es compatible con JavaScript dinámico**, a menos que uses librerías adicionales.

### Ideal para:

- Sitios web estáticos
- API REST

---

## Proxies: ¿Qué son y por qué usarlos?

Los **proxies** son servidores intermediarios que enrutan nuestras solicitudes.  
Scrapy permite utilizar proxies mediante middlewares personalizados, lo cual es útil cuando:

- Queremos evitar bloqueos por parte del sitio web
- Tenemos múltiples spiders que acceden al mismo sitio

> Usar proxies ayuda a mantener nuestras arañas activas por más tiempo sin ser bloqueadas.

---

## Estructura de un Proyecto Scrapy

Al crear un proyecto Scrapy, se genera un repositorio con los siguientes archivos y carpetas clave:

### `spiders/`

Contiene las arañas (spiders). Cada archivo define una función de scraping para un sitio o sección específica.

### `items.py`

Define los **ítems** a recolectar. Funciona como un esquema de datos, útil para organizar y validar la información que extraemos.

### `pipelines.py`

Permite **procesar y transformar los datos** después del scraping.  
Se define una clase donde podemos:

- Limpiar texto
- Validar campos
- Convertir formatos

### `middlewares.py`

Intercepta y modifica solicitudes y respuestas antes o después de pasar por la araña.  
Ejemplos de uso:

- Añadir proxies
- Modificar headers
- Implementar rotación de agentes de usuario

---

## Respeto al archivo `robots.txt`

Los sitios web suelen tener un archivo `robots.txt` que indica qué partes del sitio pueden o no ser accedidas por bots.

Para consultarlo, agregá `/robots.txt` al final de la URL:



> Es buena práctica respetar las restricciones definidas en este archivo.

---

## Cómo ejecutar una araña

Desde la terminal, usamos el siguiente comando:

```bash
scrapy crawl nombre_de_la_spider

Para guardar los resultados en un archivo (CSV, JSON, XLSX, etc.):

scrapy crawl nombre_de_la_spider -o resultados.csv

Formatos soportados:

.csv

.json

.xml

.xlsx (requiere extensiones)


Paginación: Cómo automatizar la navegación entre páginas
Muchos sitios web muestran resultados distribuidos en varias páginas.
Por ejemplo: productos de Amazon en Black Friday.

¿Por qué es importante?
No queremos scrapear solo una página ni hacerlo manualmente. Necesitamos automatizar el cambio de página.

Estrategias:
1. HTML estático
Si el botón "Siguiente" es un enlace común, podemos capturarlo con XPath o selectores CSS dentro del método parse().

2. JavaScript dinámico
Si el botón no contiene un enlace (está generado con JavaScript), una solución más robusta es generar manualmente las URLs:

def start_requests(self):
    base_url = "https://ejemplo.com/pagina="

    for page in range(1, 10):
        yield scrapy.Request(url=f'{base_url}{page}', callback=self.parse)

Este enfoque evita depender de la estructura del HTML para la paginación y permite controlar cuántas páginas vamos a scrapear.

Consejo: Siempre empezá probando con una sola página para asegurarte de que la araña funciona correctamente. Luego incorporá la lógica de paginación.



Items: como usar items loaders. The main goal in scraping is to extract structured data from unstructured sources, typically, web pages. Spiders may return the extracted data as items, Python objects that define key-value pairs. Son como schemas o modelos para nuestros spiders.

https://docs.scrapy.org/en/latest/topics/items.html

Item Types
Scrapy supports the following types of items, via the itemadapter library: dictionaries, Item objects, dataclass objects, and attrs objects.

Con los items usamos Items Loaders : Item Loaders provide a convenient mechanism for populating scraped items. Even though items can be populated directly, Item Loaders provide a much more convenient API for populating them from a scraping process, by automating some common tasks like parsing the raw extracted data before assigning it.

In other words, items provide the container of scraped data, while Item Loaders provide the mechanism for populating that container.

Asi el flow general para crear modificaciones seria, crear una funcion en nuestro script de la spider con la modificacionm , uppercase, que queramos. Para hacerlo, usamos la clase de Item que creamos con las caracteristicas del schema o de la estructura de la data que vamos a buscar, asi en nuestra spider, directamente lo que hacemos es solamente completar los campos con las modificaciones y especificaciones que queremos para que la spider traiga la informacion. 

Recorda que el tipo de archivo que exportas es en el codigo cuando lo corres en terminal. Json, csv o etc.

Default Input and Output Processors: https://www.youtube.com/watch?v=1YWBxFp7yR8
An Item Loader contains one input processor and one output processor for each (item) field. The input processor processes the extracted data as soon as it’s received (through the add_xpath(), add_css() or add_value() methods) and the result of the input processor is collected and kept inside the ItemLoader. After collecting all data, the ItemLoader.load_item() method is called to populate and get the populated item object. That’s when the output processor is called with the data previously collected (and processed using the input processor). The result of the output processor is the final value that gets assigned to the item.

input processor always receive iterables.

Custom Item Loaders: cuando queremos usar la misma logica atraves de multiples archivos. Asi podemos utilizar la logica en otros entornos

PARA DEBUGEAR. EN TU SPIDER, CUANDO USAMOS EL yield LOADER.load_item() ( nuestro schema para el item loader con sus in y out processors) le agregamos item = loader.load_item()

Scrapy Shell For Debuging, sin tener que correr la arana: https://docs.scrapy.org/en/latest/topics/shell.html
It’s meant to be used for testing data extraction code, but you can actually use it for testing any kind of code as it is also a regular Python shell.

The shell is used for testing XPath or CSS expressions and see how they work and what data they extract from the web pages you’re trying to scrape. It allows you to interactively test your expressions while you’re writing your spider, without having to run the spider to test every change.