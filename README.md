# MonitoreoPy
Trabajo final - Master de ciencias de la información


El presente repositorio hace referencia a un modulo web para el monitoreo del entorno de la ciudad de Bogotá,
se encuentra desarrollado en python con framework Django, por lo que sera necesario instalar y configurar python para ser usado.


para correr la plataforma se debe:

1. hacer una rama del repositorio.
2. instalar pip - (https://bootstrap.pypa.io/get-pip.py) - si no se tiene instalado.
3. configurar las variables de entorno.
  ejemplo en consola WINDOWS:
  
  set PATH = C:\Python27\
  set PATH = C:\Python27\Scripts
   
4. en la terminal ubicar el repositorio y ejecutar en orden:

A) pip install -r requirements.txt
B) python manage.py runserver ó manage.py runserver (se iniciara un servidor en localhost:8000)

Las url's disponibles seran:

  localhost:8000/dispositivos
  localhost:8000/admin (user = admin, pass = admin)

