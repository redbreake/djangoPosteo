# djangoPosteo

Aplicación web desarrollada con Django que permite a los usuarios registrarse, iniciar sesión, crear, ver, editar y eliminar sus propios posteos. Incluye funcionalidades de administración para superusuarios.

## Características

*   **Autenticación de Usuarios:** Registro, inicio de sesión y cierre de sesión para usuarios normales y administradores.
*   **CRUD de Posteos:** Los usuarios autenticados pueden crear, ver, editar y eliminar sus propios posteos.
*   **Permisos de Administrador:** Los superusuarios pueden eliminar cualquier posteo y acceder a estadísticas de la aplicación.
*   **Estadísticas de Administración:** Página accesible solo para superusuarios que muestra el total de usuarios, posteos y visitas a páginas clave.
*   **Diseño Minimalista:** Interfaz de usuario limpia y sencilla.

## Configuración y Ejecución

Sigue estos pasos para configurar y ejecutar el proyecto localmente:

1.  **Clonar el repositorio:**

    ```bash
    git clone https://github.com/redbreake/djangoPosteo.git
    cd djangoPosteo
    ```

2.  **Crear y activar un entorno virtual:**

    ```bash
    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate

    # Para macOS y Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instalar las dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Aplicar las migraciones de la base de datos:**

    ```bash
    python manage.py migrate
    ```

5.  **Crear un superusuario (para acceso administrativo):**

    ```bash
    python manage.py createsuperuser
    ```
    Sigue las instrucciones en la terminal para crear el superusuario.

6.  **Ejecutar el servidor de desarrollo:**

    ```bash
    python manage.py runserver
    ```

## Uso

*   Abre tu navegador y ve a `http://127.0.0.1:8000/`.
*   Desde la página de inicio, puedes registrarte o iniciar sesión.
*   Una vez autenticado, serás redirigido a la lista de posteos (`/posteos/`).
*   Desde la lista de posteos, puedes crear nuevos posteos.
*   Haz clic en el título de un posteo para ver los detalles. Si eres el autor o un superusuario, verás opciones para editar o eliminar.
*   Si eres superusuario, verás un enlace a "Estadísticas" en la barra de navegación para acceder a `/admin/stats/`.
*   El panel de administración de Django está disponible en `http://127.0.0.1:8000/admin/`.

## Enlace del Repositorio

[https://github.com/redbreake/djangoPosteo.git](https://github.com/redbreake/djangoPosteo.git)