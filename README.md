# Workshop

## Instalación

### Windows:

Requisitos: Windows 7 o superior de 64bits

Descargar docker Installer: https://store.docker.com/editions/community/docker-ce-desktop-windows 

Doble click al instalador y seguir los pasos de instalación. Terminada la instalación, aceptar habilitar Hyper-V en caso de no estar habilitado.

Reiniciar el equipo, al iniciar, el icono de la ballenita aparecerá en la barra de notificaciones indicando que Docker está en funcionamiento.

Abrir Powershell e ir a la raiz del proyecto y ejecutar el siguiente comando:

```bash
docker-compose up
```

Al finalizar la instalación, docker solicitará permisos para compartir la unidad C.

Listo.

### Linux

```bash
docker-compose up
```

### OSX

```bash
docker-compose up
```

## Entrar al contenedor

```bash
docker-compose exec back sh
docker-compose exec front sh
```

## Si no tienes acceso a internet pero tienes las imágenes de Docker en tu máquina:

```bash
docker-compose -f docker-compose.alt.yml up
```

Visitar http://localhost:8080 para la aplicación principal.  

Visitar http://localhost:8000 para la API en GraphQL.  

Visitar http://localhost:8000/admin para el panel de administración de Django.


