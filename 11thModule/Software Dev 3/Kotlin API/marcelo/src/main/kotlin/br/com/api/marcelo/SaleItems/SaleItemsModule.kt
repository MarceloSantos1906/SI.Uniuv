package br.com.api.br.com.api.marcelo.SaleItems

import kotlinx.serialization.Serializable
import java.sql.ResultSet

@Serializable
data class SaleItem(
    val id: Int,
    val saleId: Int,
    val productId: Int,
    val quantity: Int,
    val unitPrice: Double,
    val totalItem: Double
)

fun ResultSet.toSaleItem(): SaleItem {
    return SaleItem(
        id = getInt("id"),
        saleId = getInt("sale_id"),
        productId = getInt("product_id"),
        quantity = getInt("quantity"),
        unitPrice = getDouble("unit_price"),
        totalItem = getDouble("total_item")
    )
}
