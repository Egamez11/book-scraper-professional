import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from urllib.parse import urljoin

# URL base del sitio
URL_BASE = "https://books.toscrape.com"
ARCHIVO_EXCEL = "libros.xlsx"

# Headers realistas
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'es-ES,es;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Referer': 'https://books.toscrape.com'
}

def scraper_libros():
    """
    Realiza web scraping a books.toscrape.com usando requests
    Extrae: Título, Precio y Disponibilidad
    Guarda los resultados en un archivo Excel
    """
    
    libros = []
    sesion = requests.Session()
    pagina = 1
    max_paginas = 50
    
    while pagina <= max_paginas:
        try:
            # Construir URL
            if pagina == 1:
                url = URL_BASE + "/"
            else:
                url = URL_BASE + f"/catalogue/page-{pagina}.html"
            
            print(f"Scrapeando página {pagina}: {url}")
            
            # Realizar petición GET
            response = sesion.get(url, headers=HEADERS, timeout=15, verify=True)
            response.raise_for_status()
            
            # Parsear el contenido HTML
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Encontrar todos los libros (artículos)
            articulos = soup.find_all('article', class_='product_pod')
            
            if not articulos:
                print("No hay más libros. Fin del scraping.")
                break
            
            # Extraer información de cada libro
            for articulo in articulos:
                try:
                    # Título
                    titulo_elemento = articulo.find('h3').find('a')
                    titulo = titulo_elemento.get('title', 'No disponible') if titulo_elemento else 'No disponible'
                    
                    # Precio
                    precio_elemento = articulo.find('p', class_='price_color')
                    precio = precio_elemento.text if precio_elemento else 'No disponible'
                    
                    # Disponibilidad
                    disponibilidad_elemento = articulo.find('p', class_='instock availability')
                    disponibilidad = disponibilidad_elemento.text.strip() if disponibilidad_elemento else 'No disponible'
                    
                    # Agregar a la lista
                    libros.append({
                        'Título': titulo,
                        'Precio': precio,
                        'Disponibilidad': disponibilidad
                    })
                    
                except Exception as e:
                    print(f"  ⚠ Error al extraer libro: {e}")
                    continue
            
            print(f"  ✓ {len(articulos)} libros extraídos de esta página")
            
            # Verificar si existe siguiente página
            siguiente = soup.find('li', class_='next')
            if not siguiente:
                print("No hay más páginas disponibles.")
                break
            
            # Pausa entre páginas
            time.sleep(1.5)
            pagina += 1
            
        except requests.exceptions.HTTPError as e:
            print(f"✗ Error HTTP (página {pagina}): {e}")
            if pagina == 1:
                print("  No se pudo acceder a la primera página.")
                break
            else:
                # Si no encontramos una página, probablemente no hay más
                print("Fin del scraping (página no encontrada).")
                break
        except Exception as e:
            print(f"✗ Error (página {pagina}): {e}")
            if pagina == 1:
                break
            else:
                time.sleep(5)
                pagina += 1
    
    sesion.close()
    
    # Crear DataFrame con los datos
    if libros:
        df = pd.DataFrame(libros)
        
        # Guardar en archivo Excel
        try:
            df.to_excel(ARCHIVO_EXCEL, index=False, sheet_name='Libros')
            print(f"\n✓ Archivo '{ARCHIVO_EXCEL}' creado exitosamente")
            print(f"✓ Total de libros extraídos: {len(libros)}")
            print(f"\nPrimeros 5 libros:")
            print(df.head())
            return True
        except Exception as e:
            print(f"Error al guardar el archivo Excel: {e}")
            return False
    else:
        print("No se extrajeron libros.")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("SCRAPER DE LIBROS - books.toscrape.com")
    print("=" * 60)
    scraper_libros()
