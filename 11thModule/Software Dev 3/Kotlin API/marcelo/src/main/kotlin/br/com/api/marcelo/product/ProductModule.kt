package br.com.api.br.com.api.marcelo.product

import kotlinx.serialization.Serializable
import java.sql.ResultSet

@Serializable
data class Product(
    val id: Int,
    val name: String,
    val unit: String,
    val quantity: Int,
    val price: Double
)

fun ResultSet.toProduct(): Product {
    return Product(
        id = getInt("id"),
        name = getString("name"),
        unit = getString("unit"),
        quantity = getInt("quantity"),
        price = getDouble("price")
    )
}
