package br.com.api.br.com.api.marcelo.sales

import kotlinx.serialization.Serializable
import java.sql.ResultSet

@Serializable
data class Sale(
    val id: Int,
    val date: String,
    val customerId: Int,
    val totalSale: Double
)

fun ResultSet.toSale(): Sale {
    return Sale(
        id = getInt("id"),
        date = getString("date"),
        customerId = getInt("customer_id"),
        totalSale = getDouble("total_sale")
    )
}
