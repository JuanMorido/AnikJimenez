# Anik Jiménez Marulanda — Sitio web

Sitio estático personal alineado al **Manual de Marca Anik Jiménez**.

## Identidad

| Elemento | Uso en el sitio |
|---|---|
| Logo (firma) | `images/logo-anik.png` en nav, hero y footer |
| Tipografía principal | Helvetica (con Arial como respaldo), sin serifas |
| Tipografía especial | Allura (equivalente web a La Luxes Script) + logo oficial |
| Paleta | Beige `#FFF4E6`, Azul oscuro `#0E2A4E`, Azul mar `#006995`, Celeste `#38A7DE`, Baby blue `#B7CDE6`, Turquesa `#0FCDB6`, marrones de marca |

## Páginas

| Archivo | Contenido |
|---|---|
| `index.html` | Portada |
| `sobre.html` | Biografía, valores, misión, visión, propuesta, proyección |
| `libros.html` | Obra |
| `palabra.html` | Cita e impacto |
| `contacto.html` | Contacto |

## Formularios

Contacto, "Ahora es tu turno" y el formulario de "Descargar primer capítulo" (en Mis libros)
envían sus datos al correo con [Web3Forms](https://web3forms.com).
La clave de acceso va en `scripts/formularios.js` (`WEB3FORMS_CLAVE`).

## Datos

`ahoraestuturno/ciudades.json` alimenta el buscador de "Ciudad y país". Se genera con
`python3 project-config/generar-ciudades.py` a partir de [GeoNames](https://www.geonames.org) (CC BY 4.0).

## Vista local

```bash
python3 -m http.server 8080
```

## Despliegue

GitHub Pages desde `main`.
