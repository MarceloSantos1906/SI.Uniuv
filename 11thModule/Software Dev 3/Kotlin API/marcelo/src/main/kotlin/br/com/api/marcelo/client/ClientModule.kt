package br.com.api.br.com.api.marcelo.client

import kotlinx.serialization.Serializable
import java.sql.ResultSet

@Serializable
data class Client(
    val id: Int,
    val cpf: String,
    val name: String,
    val street: String,
    val neighborhood: String,
    val city: String,
    val state: String,
    val uf: String,
    val phone: String,
    val email: String
)

fun ResultSet.toClient(): Client {
    return Client(
        id = getInt("id"),
        cpf = getString("cpf"),
        name = getString("name"),
        street = getString("street"),
        neighborhood = getString("neighborhood"),
        city = getString("city"),
        state = getString("state"),
        uf = getString("uf"),
        phone = getString("phone"),
        email = getString("email")
    )
}