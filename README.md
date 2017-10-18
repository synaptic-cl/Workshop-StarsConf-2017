# Workshop

## Instalación

```bash
docker-compose up -d
```

Si no tienes acceso a internet pero tienes las imágenes de Docker en tu computador:

```bash
docker-compose -f docker-compose.alt.yml up -d
```

## Entrar al contenedor

```bash
docker-compose exec back sh
docker-compose exec front sh
```

Visitar http://localhost:8080 para la aplicación principal.  

Visitar http://localhost:8000 para la API en GraphQL.  

Visitar http://localhost:8000/admin para el panel de administración de Django.


