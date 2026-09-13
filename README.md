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