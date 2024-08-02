
# 3b

## Gestión de Inventarios
Esta documentación describe cómo crear una aplicación en Python utilizando el framework Django para gestionar productos e inventarios. La aplicación expone una API REST y un job que dispara alertas cada x tiempo cuando el stock de un producto es bajo. Además, incluye pruebas unitarias y está empaquetada en un contenedor Docker.

## Requisitos
- Python 3.8+
- Django 4.0+
- Docker
- PostgreSQL
- Celery
- Flower (Monitoreo)

## Configuración de desarrollo

### Clonar el repositorio
```bash
git clone https://github.com/GerardoX1/3b-system.git
cd 3b-system
```

### Crear y activar un entorno virtual
```bash
python3 -m venv venv
source venv/bin/activate # En Windows usa venv\Scripts\activate
```

### Instalar dependencias
```bash
pip install -r requirements.txt
```

### Configuración de la aplicación
#### Configuración de Django
Asegúrate de configurar tu base de datos en `settings.py` según tus necesidades.

### Migraciones
Ejecuta las migraciones de la base de datos:
```bash
python manage.py migrate
```

### Ejecutar el servidor de desarrollo
```bash
python manage.py runserver
```

### Job de alerta de stock bajo
El job se ejecuta cada 5 min y dispara una alerta (log en la consola) cuando el stock de un producto es inferior a 10.

### Ejecutar pruebas unitarias
```bash
pytest
```

## Dockerización
Con Docker configurado en tu PC, lo único que tienes que hacer es ejecutar el comando:
```bash
docker-compose up
```

## Servicios en Docker
- Aplicación Web: Disponible en [http://localhost:8000](http://localhost:8000)
- Base de Datos PostgreSQL (disponible en local)
- Redis
- Celery
- Flower (disponible en [http://localhost:5555](http://localhost:5555))

## Contribuir
Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request en el repositorio.

## Información Personal
### Sobre Mí
Soy esclavo moderno de dos gatos asi que necesito más dinerito 🐈‍⬛🐈💵

### Contacto
- **Nombre**: Luis Gerardo Fosado Baños
- **Email**: [yeralway1@gmail.com](mailto:yeralway1@gmail.com)
- **LinkedIn**: [www.linkedin.com/in/gerardo-fosado-0ab957165](https://www.linkedin.com/in/gerardo-fosado-0ab957165)
- **GitHub**: [https://github.com/GerardoX1](https://github.com/GerardoX1)

Si deseas más información o discutir cualquier idea de proyecto, no dudes en contactarme.
