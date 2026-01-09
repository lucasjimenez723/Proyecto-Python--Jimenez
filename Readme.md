# Proyecto Final  
## Sistema de Gestión de Pedidos de Restaurante

---

### Autor  
**Lucas Santiago**

### Materia  
Programación en Python

### Tecnologías  
Python – Django

---

## 1. Introducción

El presente proyecto consiste en el desarrollo de una aplicación web para la **gestión de pedidos de un restaurante**, implementada utilizando el framework **Django**.  
El sistema permite administrar pedidos, productos y la relación entre ambos, contemplando cantidades y precios asociados a cada pedido.

El objetivo principal es aplicar los conceptos adquiridos durante la cursada, incluyendo el uso del patrón **Modelo–Vista–Template (MVT)**, la persistencia de datos y la correcta estructuración de un proyecto web.

---

## 2. Objetivos

### Objetivo general
Desarrollar un sistema web funcional que permita la gestión integral de pedidos de un restaurante.

### Objetivos específicos
- Implementar modelos de datos relacionados.
- Utilizar vistas para la lógica de negocio.
- Diseñar templates HTML para la presentación.
- Gestionar rutas mediante el sistema de URLs de Django.
- Utilizar el panel de administración de Django.
- Aplicar buenas prácticas de organización del código.

---

## 3. Tecnologías utilizadas

- **Lenguaje:** Python 3.11  
- **Framework:** Django 5  
- **Base de datos:** SQLite  
- **Frontend:** HTML5, CSS3  
- **Servidor de desarrollo:** Django Development Server  

---

## 4. Arquitectura del sistema

El sistema sigue el patrón **Modelo–Vista–Template (MVT)** propio de Django:

- **Modelo:** Define la estructura de los datos y su persistencia.
- **Vista:** Contiene la lógica que procesa las solicitudes del usuario.
- **Template:** Se encarga de la presentación de la información.

---

## 5. Modelado de datos

El sistema cuenta con los siguientes modelos principales:

### Producto
Representa los productos disponibles en el restaurante.

### Pedido
Representa un pedido realizado por un cliente.

### PedidoProducto
Tabla intermedia que relaciona pedidos y productos, almacenando:
- Cantidad de cada producto
- Precio unitario

Esta estructura permite modelar una relación **muchos a muchos** entre pedidos y productos.

---

## 6. Funcionalidades del sistema

- Visualización de listado de pedidos
- Creación de pedidos
- Visualización del detalle de un pedido
- Asociación de productos a un pedido
- Cálculo de cantidades y precios
- Eliminación de productos de un pedido
- Administración de datos mediante Django Admin

---

## 7. Estructura del proyecto


Proyecto Final-Python/
│
├── core/
│ ├── migrations/
│ ├── static/
│ │ └── core/
│ │ └── style.css
│ ├── templates/
│ │ └── core/
│ │ ├── base.html
│ │ ├── index.html
│ │ └── detalle_pedido.html
│ ├── admin.py
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│
├── restaurante_project/
│ ├── settings.py
│ ├── urls.py
│
├── db.sqlite3
├── manage.py
└── README.md


## ▶️ Cómo ejecutar el proyecto

1. Clonar el repositorio o descargar el proyecto

2. Crear entorno virtual:
   ```bash
   python -m venv venv

3. Activar entorno virtual:

venv\Scripts\activate

4. Instalar dependencias:

pip install django

5. Ejecutar migraciones:

python manage.py migrate

6. Crear superusuario:

python manage.py createsuperuser

7. Levantar el servidor:

python manage.py runserver

8. Abrir en el navegador:

http://127.0.0.1:8000/

🔐Acceso al panel de administración
http://127.0.0.1:8000/admin


Desde allí se pueden gestionar:

Productos

Pedidos

Relaciones Pedido–Producto

🎯 Objetivo del proyecto

Este proyecto fue desarrollado como trabajo final, con el objetivo de aplicar:

Patrón MVC (Model–View–Template)

Relaciones entre modelos

Manejo de errores

Ruteo con Django

Uso de templates y archivos estáticos

Buenas prácticas de organización

✍️ Autor

Lucas Santiago
Proyecto Final – Python / Django

📌 Estado del proyecto

✅ Funcional
🛠️ En mejora continua


---

Si querés, en el próximo mensaje podemos:
- adaptarlo **exacto a la consigna del profe**
- hacerlo más **técnico** o más **simple**
- o dejar una versión **ultra formal** tipo universidad 💼📘

Decime cómo lo vas a entregar y lo ajustamos.