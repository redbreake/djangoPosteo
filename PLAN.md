# Plan de Desarrollo: Aplicación Django con Autenticación y CRUD de Posteos

Este documento detalla el plan para construir una aplicación web utilizando el framework Django en Python. La aplicación incluirá funcionalidades de autenticación de usuarios (registro y login), un sistema para crear, leer, actualizar y eliminar (CRUD) posteos, y permisos especiales para usuarios administradores.

## Objetivo del Proyecto

Crear una plataforma donde los usuarios puedan registrarse, iniciar sesión, publicar contenido (posteos), y gestionar sus propias publicaciones. Los administradores tendrán la capacidad adicional de moderar el contenido eliminando cualquier posteo.

## Tecnologías Clave

*   **Framework:** Django (Python)
*   **Base de Datos:** SQLite (por defecto en Django)
*   **Frontend:** HTML, CSS (con plantillas de Django)

## Fases del Desarrollo

El proyecto se dividirá en las siguientes fases:

### Fase 1: Configuración Inicial del Proyecto

*   Crear el proyecto principal de Django (`djangoLogin`).
*   Crear una aplicación Django dentro del proyecto (ej: `posteos`).
*   Configurar el archivo `settings.py` para:
    *   Incluir la nueva aplicación (`posteos`).
    *   Asegurar la configuración de la base de datos SQLite.
    *   Configurar las URLs de autenticación de Django.
*   Configurar el archivo `urls.py` principal del proyecto para incluir las URLs de la aplicación `posteos` y las de autenticación.

### Fase 2: Modelos de Datos

*   Definir el modelo `Post` en `posteos/models.py`. Este modelo incluirá:
    *   `titulo` (CharField)
    *   `contenido` (TextField)
    *   `fecha_creacion` (DateTimeField, auto_now_add=True)
    *   `autor` (ForeignKey al modelo `User` de Django)

### Fase 3: Autenticación y Autorización

*   Implementar las vistas y URLs para el registro de usuarios. Se pueden usar las vistas integradas de Django (`django.contrib.auth.views`) o crear vistas personalizadas.
*   Configurar las vistas y URLs para el inicio y cierre de sesión utilizando las vistas integradas de Django.
*   Crear un superusuario para la administración inicial (`python manage.py createsuperuser`).
*   Implementar lógica en las vistas para restringir el acceso a funcionalidades CRUD solo a usuarios autenticados (`@login_required`).
*   Añadir lógica en las vistas de edición y eliminación para verificar si el usuario es el autor del posteo o un administrador.
*   Crear una vista específica o integrar en la lista de posteos la funcionalidad para que los administradores puedan eliminar cualquier posteo.

### Fase 4: Funcionalidad CRUD de Posteos

*   Crear vistas basadas en clases en `posteos/views.py` para:
    *   Listar todos los posteos (`ListView`).
    *   Ver el detalle de un posteo (`DetailView`).
    *   Crear un nuevo posteo (`CreateView`).
    *   Editar un posteo existente (`UpdateView`).
    *   Eliminar un posteo (`DeleteView`).
*   Asegurar que las vistas de edición y eliminación solo permitan la acción al autor o a un administrador.

### Fase 5: Formularios

*   Crear un `ModelForm` en `posteos/forms.py` para el modelo `Post` que se utilizará en las vistas de creación y edición.
*   Si se personaliza el registro, crear un formulario de registro adecuado.

### Fase 6: Templates (Plantillas HTML)

*   Crear las siguientes plantillas HTML en `posteos/templates/posteos/`:
    *   `base.html`: Plantilla base con estructura común.
    *   `landing_page.html`: Página de inicio con enlaces a login y registro.
    *   `registro.html`: Página para el registro de usuarios.
    *   `login.html`: Página para el inicio de sesión.
    *   `lista_posteos.html`: Muestra todos los posteos.
    *   `detalle_posteo.html`: Muestra un posteo individual.
    *   `formulario_posteo.html`: Formulario para crear o editar un posteo.
    *   `confirmar_eliminar_posteo.html`: Página de confirmación antes de eliminar.
*   Crear plantillas para las vistas de autenticación de Django si se usan las integradas (ej: `registration/login.html`).

### Fase 7: URLs (Enrutamiento)

*   Definir las rutas en `posteos/urls.py` para mapear las vistas CRUD y otras vistas de la aplicación.
*   Incluir `path('accounts/', include('django.contrib.auth.urls'))` en el `urls.py` principal para las URLs de autenticación integradas.

### Fase 8: Migraciones de Base de Datos

*   Ejecutar `python manage.py makemigrations` para crear los archivos de migración.
*   Ejecutar `python manage.py migrate` para aplicar las migraciones a la base de datos.

### Fase 9: Panel de Administración

*   Registrar el modelo `Post` en `posteos/admin.py` para permitir su gestión a través del panel de administración de Django.

## Diagrama de Flujo Simplificado

```mermaid
graph TD
    A[Usuario No Autenticado] --> B[Landing Page];
    B --> C[Login];
    B --> D[Registro];
    C --> E{Autenticación Exitosa?};
    D --> C; %% Redirigir a Login después del registro
    E -- Si --> F[Lista de Posteos];
    E -- No --> C; %% Volver a Login
    F --> G[Ver Posteo];
    F --> H[Crear Posteo];
    G --> I{Es Autor o Admin?};
    I -- Si --> J[Editar Posteo];
    I -- Si --> K[Eliminar Posteo];
    F --> L{Es Admin?};
    L -- Si --> M[Eliminar Cualquier Posteo];
    H --> F; %% Redirigir a lista después de crear
    J --> G; %% Redirigir a detalle después de editar
    K --> F; %% Redirigir a lista después de eliminar
    M --> F; %% Redirigir a lista después de eliminar
```

Este plan servirá como guía durante el proceso de implementación.