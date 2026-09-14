package org.example;

import java.sql.*;

public class Main {

    private static final String URL = getEnv("DB_URL");
    private static final String USER = getEnv("DB_USER");
    private static final String PASSWORD = getEnv("DB_PASSWORD");
    
    
    public static void main(String[] args) {

        try (Connection conexion = DriverManager.getConnection(URL, USER, PASSWORD)) {

            System.out.println("Conexión a MariaDB realizada correctamente.");
            System.out.println("Base de datos:" + getEnv("DB_URL"));
            System.out.println();

            int idCliente = insertarCliente(conexion, "Cliente en Java");

            System.out.println("Despues del INSERT:");
            mostrarClientes(conexion);

            modificarCliente(conexion, idCliente, "Cliente en Java Modificado");

            System.out.println("Despues del UPDATE:");
            mostrarClientes(conexion);

            eliminarCliente(conexion, idCliente);

            System.out.println("Despues del DELETE:");
            mostrarClientes(conexion);

            System.out.println("Operaciones CRUD completadas correctamente.");

        } catch (SQLException e) {
            System.err.println("Error de base de datos: " + e.getMessage());
            System.err.println("Código SQL: " + e.getErrorCode());
            System.err.println("Estado SQL: " + e.getSQLState());
        }
    }

    private static int insertarCliente(Connection conexion, String nombre)
            throws SQLException {

        String sql = "INSERT INTO clientes(nombre) VALUES (?)";

        try (PreparedStatement ps = conexion.prepareStatement(
                sql,
                Statement.RETURN_GENERATED_KEYS)) {

            ps.setString(1, nombre);

            int filas = ps.executeUpdate();

            System.out.println("INSERT ejecutado. Filas afectadas: " + filas);

            try (ResultSet rs = ps.getGeneratedKeys()) {

                if (rs.next()) {
                    int id = rs.getInt(1);
                    System.out.println("Cliente insertado con ID: " + id);
                    return id;
                }
            }
        }

        throw new SQLException("No se pudo obtener el ID del cliente insertado.");
    }

    private static void mostrarClientes(Connection conexion)
            throws SQLException {

        String sql = "SELECT id, nombre FROM clientes ORDER BY id";

        try (PreparedStatement ps = conexion.prepareStatement(sql);
             ResultSet rs = ps.executeQuery()) {

            while (rs.next()) {
                int id = rs.getInt("id");
                String nombre = rs.getString("nombre");

                System.out.println("ID: " + id + " | Nombre: " + nombre);
            }
        }

        System.out.println();
    }

    private static void modificarCliente(
            Connection conexion,
            int id,
            String nuevoNombre) throws SQLException {

        String sql = "UPDATE clientes SET nombre = ? WHERE id = ?";

        try (PreparedStatement ps = conexion.prepareStatement(sql)) {

            ps.setString(1, nuevoNombre);
            ps.setInt(2, id);

            int filas = ps.executeUpdate();

            System.out.println(
                    "UPDATE ejecutado. Filas afectadas: " + filas
            );
        }
    }

    private static void eliminarCliente(
            Connection conexion,
            int id) throws SQLException {

        String sql = "DELETE FROM clientes WHERE id = ?";

        try (PreparedStatement ps = conexion.prepareStatement(sql)) {

            ps.setInt(1, id);

            int filas = ps.executeUpdate();

            System.out.println(
                    "DELETE ejecutado. Filas afectadas: " + filas
            );
        }
    }
    
    private static String getEnv(String name) {
        String value = System.getenv(name);

        if (value == null || value.isBlank()) {
            throw new IllegalStateException(
                    "Falta la variable de entorno obligatoria: " + name
            );
        }

        return value;
    }
}