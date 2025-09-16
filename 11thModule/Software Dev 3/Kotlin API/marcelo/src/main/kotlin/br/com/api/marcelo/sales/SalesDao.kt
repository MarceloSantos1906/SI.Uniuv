package br.com.api.br.com.api.marcelo.sales

import br.com.api.br.com.api.marcelo.database.Database

class SalesDao {
    fun findAll(): List<Sale> {
        val query = "SELECT id, date, customer_id, total_sale FROM sales ORDER BY id"
        Database.getConnection().use { conn ->
            val statement = conn.prepareStatement(query)
            val resultSet = statement.executeQuery()

            val sales = mutableListOf<Sale>()
            while (resultSet.next()) {
                sales.add(resultSet.toSale())
            }
            return sales
        }
    }

    fun findById(id: Int): Sale? {
        val query = "SELECT id, date, customer_id, total_sale FROM sales WHERE id = ?"
        Database.getConnection().use { conn ->
            val statement = conn.prepareStatement(query)
            statement.setInt(1, id)
            val resultSet = statement.executeQuery()

            return if (resultSet.next()) {
                resultSet.toSale()
            } else null
        }
    }

    fun insert(sale: Sale): Sale {
        val query = "INSERT INTO sales (date, customer_id, total_sale) VALUES (?, ?, ?) RETURNING id"
        Database.getConnection().use { conn ->
            val statement = conn.prepareStatement(query)
            statement.setString(1, sale.date)
            statement.setInt(2, sale.customerId)
            statement.setDouble(3, sale.totalSale)

            val resultSet = statement.executeQuery()
            resultSet.next()
            val generatedId = resultSet.getInt("id")

            return sale.copy(id = generatedId)
        }
    }

    fun update(id: Int, sale: Sale): Sale? {
        val query = "UPDATE sales SET date = ?, customer_id = ?, total_sale = ? WHERE id = ?"
        Database.getConnection().use { conn ->
            val statement = conn.prepareStatement(query)
            statement.setString(1, sale.date)
            statement.setInt(2, sale.customerId)
            statement.setDouble(3, sale.totalSale)
            statement.setInt(4, id)

            val affectedRows = statement.executeUpdate()
            return if (affectedRows > 0) {
                sale.copy(id = id)
            } else null
        }
    }

    fun delete(id: Int): Boolean {
        val query = "DELETE FROM sales WHERE id = ?"
        Database.getConnection().use { conn ->
            val statement = conn.prepareStatement(query)
            statement.setInt(1, id)

            return statement.executeUpdate() > 0
        }
    }
}