# 🍕 Gestión de Pedidos - Restaurante

Sistema web desarrollado con **Django** para la gestión de pedidos de un restaurante. Permite a los clientes registrarse, personalizar su perfil y realizar pedidos, mientras que los administradores gestionan el menú de forma dinámica y segura.

## 📹 Video de Demostración

Puedes ver un recorrido completo por las funcionalidades del sistema (Registro, CRUD de productos, Pedidos y Perfil) en el siguiente enlace:

👉 **[Ver Demo en Loom / YouTube](AQUI_PONES_TU_LINK)**

---

## 🚀 Funcionalidades Principales

### 👤 Gestión de Usuarios (Clientes)
* **Registro e Inicio de Sesión:** Autenticación segura solicitando nombre, apellido y email.
* **Perfil Personalizado:** Cada usuario puede subir y actualizar su **foto de perfil (Avatar)**, biografía y sitio web.
* **Pedidos:** Visualización del menú y realización de pedidos de forma sencilla.
* **Historial:** Acceso a los pedidos realizados anteriormente.

### 🛡️ Administración (Staff)
* **Gestión del Menú (CRUD):** Alta, Baja y Modificación de platos.
* **Contenido Enriquecido:** Uso de editor de texto (CKEditor) para descripciones detalladas y subida de imágenes para cada plato.
* **Seguridad:** Panel protegido; solo los administradores pueden ver los botones de edición y creación.

---

## 🛠️ Tecnologías Utilizadas

* **Back-end:** Python, Django 5.0.
* **Front-end:** HTML5, CSS3 (Diseño Responsive).
* **Base de datos:** SQLite.
* **Librerías Extra:**
    * `Pillow` (Gestión de imágenes y avatares).
    * `django-ckeditor` (Editor de texto enriquecido).

---

## ⚙️ Instalación y Ejecución

Sigue estos pasos para correr el proyecto localmente:

### 1. Clonar el repositorio
```bash
git clone https://github.com/lucasjimenez723/Proyecto-Python--Jimenez.git
cd "Proyecto-Python--Jimenez"

### 2. Crear y activar entorno virtual
En Windows:
python -m venv venv
venv\Scripts\activate

En Mac/Linux:
python3 -m venv venv
source venv/bin/activate

### 3. Instalar dependencias
pip install -r requirements.txt

### 4. Aplicar migraciones
python manage.py makemigrations
python manage.py migrate

### 5. Crear Superusuario (Administrador)
Necesario para poder agregar o editar platos en el menú.
python manage.py createsuperuser

### 6. Iniciar el servidor
python manage.py runserver

### 7. Acceso al Sistema
Ingresa a http://127.0.0.1:8000/.

Credenciales de prueba (Superusuario):

Usuario: (el que creaste en el paso 5)

Contraseña: (la que definiste)

### ✒️ Autor
Lucas - Proyecto Final Python Coderhouse - 2026