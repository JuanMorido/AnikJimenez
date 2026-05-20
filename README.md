# Anik Jiménez Marulanda — Sitio web personal

Sitio estático para la escritora colombiana Anik Jiménez Marulanda. Desplegado en GitHub Pages.

## Páginas

| Archivo | Ruta | Contenido |
|---|---|---|
| `index.html` | `/` | Inicio / portada |
| `sobre.html` | `/sobre.html` | Sobre la autora |
| `libros.html` | `/libros.html` | Libros publicados |
| `palabra.html` | `/palabra.html` | Cita destacada |
| `contacto.html` | `/contacto.html` | Formulario de contacto |

## Desarrollo local

Sin pasos de compilación. Abre los archivos directamente en el navegador o levanta un servidor estático:

```bash
python3 -m http.server 8080
```

Luego abre `http://localhost:8080`.

## Despliegue

El sitio se despliega automáticamente en GitHub Pages desde la rama `main`. No se requiere ningún paso de build.

Para configurarlo por primera vez: **Settings → Pages → Source → Deploy from branch → `main` / `(root)`**.
