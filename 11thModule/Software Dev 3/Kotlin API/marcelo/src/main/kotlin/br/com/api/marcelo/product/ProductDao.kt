package br.com.api.br.com.api.marcelo.product

import br.com.api.br.com.api.marcelo.database.Database

class ProductDao {
    fun findAll(): List<Product> {
        val query = "SELECT id, name, unit, quantity, price FROM products ORDER BY id"
        Database.getConnection().use { conn ->
            val statement = conn.prepareStatement(query)
            val resultSet = statement.executeQuery()

            val products = mutableListOf<Product>()
            while (resultSet.next()) {
                products.add(resultSet.toProduct())
            }
            return products
        }
    }

    fun findById(id: Int): Product? {
        val query = "SELECT id, name, unit, quantity, price FROM products WHERE id = ?"
        Database.getConnection().use { conn ->
            val statement = conn.prepareStatement(query)
            statement.setInt(1, id)
            val resultSet = statement.executeQuery()

            return if (resultSet.next()) {
                resultSet.toProduct()
            } else null
        }
    }

    fun insert(product: Product): Product {
        val query = "INSERT INTO products (name, unit, quantity, price) VALUES (?, ?, ?, ?) RETURNING id"
        Database.getConnection().use { conn ->
            val statement = conn.prepareStatement(query)
            statement.setString(1, product.name)
            statement.setString(2, product.unit)
            statement.setInt(3, product.quantity)
            statement.setDouble(4, product.price)

            val resultSet = statement.executeQuery()
            resultSet.next()
            val generatedId = resultSet.getInt("id")

            return product.copy(id = generatedId)
        }
    }

    fun update(id: Int, product: Product): Product? {
        val query = "UPDATE products SET name = ?, unit = ?, quantity = ?, price = ? WHERE id = ?"
        Database.getConnection().use { conn ->
            val statement = conn.prepareStatement(query)
            statement.setString(1, product.name)
            statement.setString(2, product.unit)
            statement.setInt(3, product.quantity)
            statement.setDouble(4, product.price)
            statement.setInt(5, id)

            val affectedRows = statement.executeUpdate()
            return if (affectedRows > 0) {
                product.copy(id = id)
            } else null
        }
    }

    fun delete(id: Int): Boolean {
        val query = "DELETE FROM products WHERE id = ?"
        Database.getConnection().use { conn ->
            val statement = conn.prepareStatement(query)
            statement.setInt(1, id)

            return statement.executeUpdate() > 0
        }
    }
}
