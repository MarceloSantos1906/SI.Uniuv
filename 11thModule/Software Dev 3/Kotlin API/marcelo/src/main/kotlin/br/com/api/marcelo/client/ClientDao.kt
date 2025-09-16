package br.com.api.br.com.api.marcelo.client

import br.com.api.br.com.api.marcelo.database.Database

class ClientDao {
    fun findAll(): List<Client> {
        val query = "SELECT id, cpf, name, street, neighborhood, city, state, uf, phone, email FROM customers ORDER BY id"
        Database.getConnection().use { conn ->
            val statement = conn.prepareStatement(query)
            val resultSet = statement.executeQuery()

            val clients = mutableListOf<Client>()
            while (resultSet.next()) {
                clients.add(resultSet.toClient())
            }
            return clients
        }
    }

    fun findById(id: Int): Client? {
        val query = "SELECT id, cpf, name, street, neighborhood, city, state, uf, phone, email FROM customers WHERE id = ?"
        Database.getConnection().use { conn ->
            val statement = conn.prepareStatement(query)
            statement.setInt(1, id)
            val resultSet = statement.executeQuery()

            return if (resultSet.next()) {
                resultSet.toClient()
            } else null
        }
    }

    fun insert(client: Client): Client {
        val query = """
            INSERT INTO customers (cpf, name, street, neighborhood, city, state, uf, phone, email) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?) RETURNING id
        """.trimIndent()
        Database.getConnection().use { conn ->
            val statement = conn.prepareStatement(query)
            statement.setString(1, client.cpf)
            statement.setString(2, client.name)
            statement.setString(3, client.street)
            statement.setString(4, client.neighborhood)
            statement.setString(5, client.city)
            statement.setString(6, client.state)
            statement.setString(7, client.uf)
            statement.setString(8, client.phone)
            statement.setString(9, client.email)

            val resultSet = statement.executeQuery()
            resultSet.next()
            val generatedId = resultSet.getInt("id")

            return client.copy(id = generatedId)
        }
    }

    fun update(id: Int, client: Client): Client? {
        val query = """
            UPDATE customers 
            SET cpf = ?, name = ?, street = ?, neighborhood = ?, city = ?, state = ?, uf = ?, phone = ?, email = ?
            WHERE id = ?
        """.trimIndent()
        Database.getConnection().use { conn ->
            val statement = conn.prepareStatement(query)
            statement.setString(1, client.cpf)
            statement.setString(2, client.name)
            statement.setString(3, client.street)
            statement.setString(4, client.neighborhood)
            statement.setString(5, client.city)
            statement.setString(6, client.state)
            statement.setString(7, client.uf)
            statement.setString(8, client.phone)
            statement.setString(9, client.email)
            statement.setInt(10, id)

            val affectedRows = statement.executeUpdate()
            return if (affectedRows > 0) {
                client.copy(id = id)
            } else null
        }
    }

    fun delete(id: Int): Boolean {
        val query = "DELETE FROM customers WHERE id = ?"
        Database.getConnection().use { conn ->
            val statement = conn.prepareStatement(query)
            statement.setInt(1, id)

            return statement.executeUpdate() > 0
        }
    }
}