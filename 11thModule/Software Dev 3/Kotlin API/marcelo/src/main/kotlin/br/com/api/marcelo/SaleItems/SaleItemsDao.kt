package br.com.api.br.com.api.marcelo.SaleItems

import br.com.api.br.com.api.marcelo.database.Database

class SaleItemsDao {
    fun findAll(): List<SaleItem> {
        val query = "SELECT id, sale_id, product_id, quantity, unit_price, total_item FROM sale_items ORDER BY id"
        Database.getConnection().use { conn ->
            val statement = conn.prepareStatement(query)
            val resultSet = statement.executeQuery()

            val saleItems = mutableListOf<SaleItem>()
            while (resultSet.next()) {
                saleItems.add(resultSet.toSaleItem())
            }
            return saleItems
        }
    }

    fun findById(id: Int): SaleItem? {
        val query = "SELECT id, sale_id, product_id, quantity, unit_price, total_item FROM sale_items WHERE id = ?"
        Database.getConnection().use { conn ->
            val statement = conn.prepareStatement(query)
            statement.setInt(1, id)
            val resultSet = statement.executeQuery()

            return if (resultSet.next()) {
                resultSet.toSaleItem()
            } else null
        }
    }

    fun findBySaleId(saleId: Int): List<SaleItem> {
        val query = "SELECT id, sale_id, product_id, quantity, unit_price, total_item FROM sale_items WHERE sale_id = ?"
        Database.getConnection().use { conn ->
            val statement = conn.prepareStatement(query)
            statement.setInt(1, saleId)
            val resultSet = statement.executeQuery()

            val saleItems = mutableListOf<SaleItem>()
            while (resultSet.next()) {
                saleItems.add(resultSet.toSaleItem())
            }
            return saleItems
        }
    }

    fun insert(saleItem: SaleItem): SaleItem {
        val query = """
            INSERT INTO sale_items (sale_id, product_id, quantity, unit_price, total_item) 
            VALUES (?, ?, ?, ?, ?) RETURNING id
        """.trimIndent()
        Database.getConnection().use { conn ->
            val statement = conn.prepareStatement(query)
            statement.setInt(1, saleItem.saleId)
            statement.setInt(2, saleItem.productId)
            statement.setInt(3, saleItem.quantity)
            statement.setDouble(4, saleItem.unitPrice)
            statement.setDouble(5, saleItem.totalItem)

            val resultSet = statement.executeQuery()
            resultSet.next()
            val generatedId = resultSet.getInt("id")

            return saleItem.copy(id = generatedId)
        }
    }

    fun update(id: Int, saleItem: SaleItem): SaleItem? {
        val query = """
            UPDATE sale_items 
            SET sale_id = ?, product_id = ?, quantity = ?, unit_price = ?, total_item = ?
            WHERE id = ?
        """.trimIndent()
        Database.getConnection().use { conn ->
            val statement = conn.prepareStatement(query)
            statement.setInt(1, saleItem.saleId)
            statement.setInt(2, saleItem.productId)
            statement.setInt(3, saleItem.quantity)
            statement.setDouble(4, saleItem.unitPrice)
            statement.setDouble(5, saleItem.totalItem)
            statement.setInt(6, id)

            val affectedRows = statement.executeUpdate()
            return if (affectedRows > 0) {
                saleItem.copy(id = id)
            } else null
        }
    }

    fun delete(id: Int): Boolean {
        val query = "DELETE FROM sale_items WHERE id = ?"
        Database.getConnection().use { conn ->
            val statement = conn.prepareStatement(query)
            statement.setInt(1, id)

            return statement.executeUpdate() > 0
        }
    }
}