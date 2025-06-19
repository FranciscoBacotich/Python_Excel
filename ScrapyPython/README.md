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