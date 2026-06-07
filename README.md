# 🚀 Data Extraction & Automation: Professional Web Scraper (1,000+ Records)

Este proyecto es una solución automatizada de extracción de datos (Web Scraping) desarrollada en **Python**. Está diseñada para extraer de forma masiva información estructurada de catálogos web dinámicos, procesarla eficientemente y exportarla de forma limpia a formatos de negocio listos para su análisis (**Microsoft Excel / CSV**).

Ideal para optimizar la recopilación de datos, monitoreo de precios, análisis de la competencia y nutrición de bases de datos para CRM sin intervención manual.

---

## 🎯 Solución de Negocio (Business Value)
* **Automatización Extrema:** Reemplaza horas de copiado y pegado manual por un proceso de ejecución en un solo clic que extrae la información completa en segundos.
* **Manejo de Paginación Avanzada:** Capacidad para navegar de forma autónoma a través de múltiples páginas (50+ páginas analizadas de forma consecutiva).
* **Control de Restricciones (Anti-Ban Ready):** Implementación de tiempos de espera inteligentes (*delay*) y cabeceras personalizadas (*User-Agents*) para emular el comportamiento humano y evitar bloqueos por parte del servidor web.
* **Estructuración de Datos Limpia:** Limpieza automática de caracteres especiales y símbolos de moneda, asegurando que los datos numéricos estén listos para fórmulas y gráficos en Excel.

---

## 🛠️ Stack Tecnológico
* **Lenguaje:** Python 3.10+
* **Extracción:** `BeautifulSoup4`, `Requests` (Manejo de peticiones HTTP y parsing de HTML).
* **Procesamiento de Datos:** `Pandas` (Limpieza, estructuración y manipulación de DataFrames).
* **Exportación:** `OpenPyXL` (Generación de hojas de cálculo nativas `.xlsx`).

---

## 📊 Datos Extraídos e Impacto
El script navega automáticamente y genera una base de datos estructurada con las siguientes variables por cada registro:
1. **Título del Producto:** Sanitizado y formateado.
2. **Precio:** Convertido a formato numérico limpio para análisis financiero.
3. **Disponibilidad/Stock:** Estado actual del inventario en tiempo real.

### 📸 Evidencia del Resultado
*(Inserta aquí la captura de tu tabla de Excel que me pasaste para que el cliente vea el resultado visual inmediato)*
`![Resultado en Excel](https://github.com/Egamez11/book-scraper-professional/raw/main/resultado.png)` *(O la ruta donde subas la imagen)*

---

## 🚀 Instalación y Uso

Si deseas probar el script localmente, sigue estos pasos:

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/Egamez11/book-scraper-professional.git](https://github.com/Egamez11/book-scraper-professional.git)
   cd book-scraper-professional
