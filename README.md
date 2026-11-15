# Blog Django

Proyecto base de un blog web desarrollado con Django.

## Descripción

Este repositorio contiene un blog sencillo construido con Django. Incluye la configuración base del proyecto (`blog_project`) y una aplicación llamada `posts`, que define las vistas, rutas, plantillas y archivos estáticos del sitio.

Por ahora los posts se generan como una lista fija dentro de la vista (todavía no hay modelos ni base de datos para las publicaciones).

## Requisitos

- Python 3.12 o superior (Django 6.1.2 no se instala en versiones anteriores).

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/diegoalvarezmeza/blog_django
```

Entrar a la carpeta del proyecto:

```bash
cd blog_django
```

Crear entorno virtual:

```bash
python -m venv venv
```

Activar entorno virtual:

En Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

En Linux o macOS:

```bash
source venv/bin/activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar el servidor:

```bash
python manage.py runserver
```

Abrir en el navegador: http://127.0.0.1:8000/

## Rutas disponibles

Las rutas de la app `posts` se incluyen en la raíz del proyecto desde `blog_project/urls.py`.

| URL         | Vista         | Nombre (`name`) | Plantilla                  | Descripción                                  |
|-------------|---------------|-----------------|----------------------------|----------------------------------------------|
| `/`         | `inicio`      | `inicio`        | `posts/inicio.html`        | Página de inicio del blog.                   |
| `/posts/`   | `lista_posts` | `lista_posts`   | `posts/lista_posts.html`   | Listado de posts (id, título y autor).       |
| `/acerca/`  | `acerca`      | `acerca`        | `posts/acerca.html`        | Información sobre el blog.                   |
| `/admin/`   | —             | —               | —                          | Panel de administración de Django.           |

## Vistas

Definidas en `posts/views.py`:

- **`inicio`**: renderiza la página de inicio.
- **`lista_posts`**: arma una lista de posts de ejemplo y la envía a la plantilla en el contexto `posts`:
  - `Mi primer post` — Ana
  - `Aprendiendo Django` — Luis
  - `Rutas y vistas` — Marta
- **`acerca`**: renderiza la página "Acerca de".

## Estructura de la app `posts`

```
posts/
├── views.py              # Vistas: inicio, lista_posts, acerca
├── urls.py               # Rutas de la app
├── templates/posts/
│   ├── base.html         # Plantilla base (header, navegación y footer)
│   ├── inicio.html
│   ├── lista_posts.html
│   ├── acerca.html
│   ├── detalle_post.html # Aún sin vista ni ruta asociada
│   └── contacto.html     # Aún sin vista ni ruta asociada
└── static/posts/
    ├── css/style.css
    └── js/main.js
```

Todas las páginas extienden `base.html`, que carga los estilos y muestra el menú de navegación con enlaces a Inicio, Posts y Acerca de usando `{% url %}`.

