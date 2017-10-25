# Workshop

## Requisitos de Instalación

Docker: 
Link de [Descarga](https://docs.docker.com/docker-for-windows/install/) Windows.
Link de [Descarga](https://download.docker.com/mac/stable/Docker.dmg) Mac OS

Ubuntu
> $ sudo apt-get update
> 
> $ sudo apt-get install docker-ce

CentOS
> $ sudo yum install docker-ce


## Instalación de la Aplicación

## Linux / MacOs

Clonar el repositorio y ejecutar

```bash
docker-compose up
```

Click a <http://localhost:8080>: para la aplicación principal.  

Click a <http://localhost:8000>: para la API en GraphQL.  

Click a <http://localhost:8000/admin>: para el panel de administración de Django.

### Windows:

#### Windows 10 de 64bits
* Descargar [Docker Installer]( https://store.docker.com/editions/community/docker-ce-desktop-windows )
* Doble click al instalador y seguir los pasos de instalación. Terminada la instalación, aceptar habilitar **Hyper-V** en caso de no estar habilitado.
* Reiniciar el equipo, al iniciar, el icono de la ballenita aparecerá en la barra de notificaciones indicando que Docker está en funcionamiento.
* Abrir Powershell e ir a la raiz del proyecto y ejecutar el siguiente comando:

	 ```$ docker-compose up```
* Al finalizar la instalación, docker solicitará permisos para compartir la unidad C.

> En Windows es importante que en el archivo: docker-compose.yml se modifique "localhost" a la IP de la máquina

### En Caso de no tener acceso a internet

- Obtén el archivo workshop.zip que contiene los elementos necesarios y descomprímelo.
- Navega hasta el directorio resultante.

``` bash 
$ cd workshop
```

Ejecuta la siguientes instrucciones para proceder con la instalación

```bash

$ sh import_import_repo_and_containers.sh
$ docker-compose -f docker-compose.alt.yml up
```
El contenedor de la aplicación estará entonces funcionando.

### Ingresando al Contenedor

Deberás ejecutar los siguientes comandos según quieras acceder a la aplicación que sirve los datos a travez de GraphQL o a la aplicación que permite visualizarlos.

```bash
docker-compose exec back sh
docker-compose exec front sh
```
