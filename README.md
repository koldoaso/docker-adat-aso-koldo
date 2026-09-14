# Ejercicio 1.

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

# Ejercicio 3.

Crear el environment para Python con el siguiente comando.

```
python -m venv ./python/.venv
```

Nos movemos al directorio de Python.

```
cd python
```

Activamos el environment utilizando el script dependiendo del sistema operativo, en nuestro caso, Windows 10.

```
.\.venv\Scripts\Activate.ps1 
```

Instalamos los paquetes requeridos para mariadb y para utilizar .env.

```
pip install mariadb python-dotenv
```

Generamos los requerimientos.

```
pip freeze > requirements.txt
```

## Ejecución del programa

Entramos dentro del environment tal como se describió en los pasos anteriores y añadimos el siguiente comando desde la carpeta python para iniciar el script.

```
py .\clientes.py
```

# Ejercicio 4

Se utiliza el driver oficial de MariaDB:

```
<dependency>
    <groupId>org.mariadb.jdbc</groupId>
    <artifactId>mariadb-java-client</artifactId>
    <version>3.5.6</version>
</dependency>
```

El pom.xml está configurado con:

```
<maven.compiler.source>21</maven.compiler.source>
<maven.compiler.target>21</maven.compiler.target>
```

## Versión de Java

El proyecto utiliza Java 21.

Para comprobar la versión instalada:

```
java -version
mvn -version
```

## Variables de entorno

La configuración de conexión se obtiene mediante variables de entorno:

DB_URL=jdbc:mariadb://localhost:3306/empresa
DB_USER=adat
DB_PASSWORD=admin

En PowerShell se pueden configurar mediante:

```
$env:DB_URL="jdbc:mariadb://localhost:3306/empresa"
$env:DB_USER="adat"
$env:DB_PASSWORD="admin"
```

## Compilación

Desde la carpeta java-jdbc/:

```
mvn clean compile
```

## Ejecucion

```
mvn exec:java "-Dexec.mainClass=org.example.Main"
```

## PreparedStatement

consultas que utilizan valores proporcionados por el programa utilizan PreparedStatement y parámetros

Por ejemplo:

```
PreparedStatement ps = conexion.prepareStatement(
    "INSERT INTO clientes(nombre) VALUES (?)"
);

ps.setString(1, nombre);
```

Con ello los valores no se concatenan directamente en las sentencias SQL. Los parámetros se establecen mediante métodos como setString() y setInt()

Esto separa la sentencia SQL de los datos, reduciendo el riesgo de ataques mediante inyecciones SQL.

## Try-with-resources

Esto sirve para que la conexion, los PreparedStatement y los ResultSet se gestionen mediante try-with-resources.

Por ejemplo:

```
try (PreparedStatement ps = conexion.prepareStatement(sql);
     ResultSet rs = ps.executeQuery()) {

    // Procesamiento de resultados
}
```

Con esto, los recursos se cierran automáticamente al finalizar el bloque, incluso cuando se produce una excepción. Con ello evitamos problemas de dejar leaks de recursos que pueden llevar a errores como que el programa se quede sin canales de comunicación y lance excepciones como SQLException o IOException