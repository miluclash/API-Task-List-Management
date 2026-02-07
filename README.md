# 🌿 Green Task Manager - API REST & Web App

[![Python](https://img.shields.io/badge/Python-3.13-2d6a4f?style=flat-square&logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-6.0-092e20?style=flat-square&logo=django)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DRF-API-ff4438?style=flat-square&logo=django)](https://www.django-rest-framework.org/)

Este proyecto es un **Gestor de Tareas Integral** desarrollado para el módulo de Desarrollo Web en Entorno Servidor (DWES). Combina una potente **API REST** para la gestión de datos y una **interfaz web minimalista** diseñada para la mejor experiencia de usuario.



## 🌟 Características Principales

* **Arquitectura Híbrida**: Funciona tanto como una API para otras aplicaciones como una web interactiva.
* **Gestión CRUD Completa**: Creación, visualización, edición y borrado de listas de tareas y tareas individuales.
* **Interfaz Minimalista**: Diseño basado en Bootstrap 5 con una paleta de colores verde relajante y moderna.
* **Relaciones Complejas**: Implementación de relaciones 1:N entre Listas y Tareas con integridad referencial (Borrado en cascada).
* **UX Mejorada**: Sistema de "Toggle" para marcar tareas completadas/pendientes sin salir de la vista principal.

## 🛠️ Tecnologías y Herramientas

* **Backend:** Python 3.13 & Django 6.0
* **API:** Django REST Framework (DRF)
* **Frontend:** HTML5, CSS3 (Custom Variables), Bootstrap 5, FontAwesome
* **Base de Datos:** SQLite (Perfecto para portabilidad y desarrollo)
* **Gestión de Entorno:** uv / pip

## 🚀 Instalación y Uso

Si quieres probar este proyecto localmente, sigue estos pasos:

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/tu-usuario/nombre-de-tu-repo.git](https://github.com/tu-usuario/nombre-de-tu-repo.git)
   cd nombre-de-tu-repo

2. **Crear e instalar dependencias:**
   # Si usas uv (recomendado)
    uv pip install -r requirements.txt
    # Si usas pip
    pip install -r requirements.txt

3. **Ejecutar migraciones:**
   python manage.py migrate

4. **Lanzar servidor:**
   python manage.py runserver

## 📁Estructura del Proyecto
  /appweb: Contiene la lógica de negocio, modelos, vistas y plantillas.
    
  /proyecto_archivos_base: Configuración central del proyecto Django.
  
  /templates/appweb: Interfaz de usuario (HTML/CSS).
  
  requirements.txt: Lista de dependencias del proyecto.
