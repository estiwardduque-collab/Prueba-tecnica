# Selenium + Python + POM Automation Project

## Descripción
Este proyecto automatiza el flujo de compra en el sitio de prueba [OpenCart](https://opencart.abstracta.us/index.php?route=common/home) utilizando **Selenium WebDriver**, **Python**, **Pytest**, y el patrón de diseño **Page Object Model (POM)**.

## Requisitos
- Python 3.x
- Google Chrome

## Instalación

1. Clonar el repositorio o descargar los archivos.
2. Crear un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```
3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Estructura del Proyecto

```
project/
│── config/
│     └── config.py        # Configuración global (URLs, Timeouts)
│
│── pages/                 # Page Objects
│     ├── base_page.py     # Métodos base
│     ├── home_page.py
│     ├── register_page.py
│     ├── login_page.py
│     ├── product_page.py
│     ├── cart_page.py
│     └── checkout_page.py
│
│── tests/                 # Tests ejecutables
│     ├── conftest.py      # Fixtures de Pytest (driver setup)
│     ├── test_register.py
│     ├── test_login.py
│     └── test_full_purchase_flow.py
│
│── utils/                 # Utilidades
│     ├── driver_factory.py
│     ├── generators.py    # Generación de datos de prueba
│     └── waits.py         # Manejo de esperas explícitas
│
└── requirements.txt
```

## Ejecución de Tests

Para ejecutar todos los tests con output detallado:

```bash
pytest -s -v
```

Para generar un reporte HTML (si pytest-html está instalado):

```bash
pytest -s -v --html=report.html
```

## Notas Técnicas
- **POM**: Se utiliza para separar la lógica de los tests de la estructura de la página, facilitando el mantenimiento.
- **Waits**: Se utilizan esperas explícitas (`WebDriverWait`) en `utils/waits.py` para asegurar estabilidad y evitar `time.sleep` duros siempre que sea posible.
- **Generators**: Se usa la librería `Faker` para crear usuarios y datos únicos en cada ejecución.
- **Manejo de Errores**: La clase `BasePage` captura excepciones comunes y toma screenshots automáticamente en la carpeta `screenshots/` si falla una interacción crítica.
