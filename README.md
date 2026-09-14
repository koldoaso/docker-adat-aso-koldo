Realizar el siguiente comando para generar y correr un contenedor Docker con el nombre mariadb-adat y la password admin.

```
docker run --name mariadb-adat -e MARIADB_ROOT_PASSWORD=admin -p 3306:3306 -d mariadb
```

Realizar el siguiente comando para ver que contenedores están up.

```
docker ps
```

Parar el contenedor con el siguiente comando, modificando el ID del contenedor por el apropiado.

```
docker stop f1a0353e391e
```

Iniciar nuevamente el contenedor con el comando.

```
docker start mariadb-adat
```

# Ejercicio 2.

## ¿Que es un volumen?

- Es un directorio gestionado por Docker separado del contenedor para guardar datos de forma persistente en caso de que el contenedor se apague o se elimine.


Parar el contenedor con el siguiente comando, modificando el ID del contenedor por el apropiado.

```
docker stop f1a0353e391e 
```

Eliminar el contenedor con el siguiente comando.

```
docker rm mariadb-adat
```

Generar el nuevo contenedor utilizando compose con el siguiente comando.

```
docker compose up -d
```

Realizar el siguiente comando para ver que contenedores están up.

```
docker ps
```

Para Entrar dentro del contenedor desde la terminal.

```
docker exec -it mariadb-adat mariadb -u adat -p
```

```
USE empresa;
```

Generar una tabla para comprobar la persistencia del contenedor.

```
CREATE TABLE prueba_persistencia (
    id INT PRIMARY KEY AUTO_INCREMENT,
    mensaje VARCHAR(255)
);

INSERT INTO prueba_persistencia (mensaje)
VALUES ('persistencia funciona');
```