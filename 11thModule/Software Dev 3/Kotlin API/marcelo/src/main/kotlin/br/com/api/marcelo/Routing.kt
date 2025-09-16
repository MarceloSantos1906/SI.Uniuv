package br.com.api.br.com.api.marcelo

import br.com.api.br.com.api.marcelo.client.Client
import br.com.api.br.com.api.marcelo.client.ClientDao
import br.com.api.br.com.api.marcelo.product.Product
import br.com.api.br.com.api.marcelo.product.ProductDao
import br.com.api.br.com.api.marcelo.sales.Sale
import br.com.api.br.com.api.marcelo.sales.SalesDao
import br.com.api.br.com.api.marcelo.SaleItems.SaleItem
import br.com.api.br.com.api.marcelo.SaleItems.SaleItemsDao
import io.ktor.http.*
import io.ktor.server.application.*
import io.ktor.server.request.*
import io.ktor.server.response.*
import io.ktor.server.routing.*

fun Application.configureRouting() {
    val productDao = ProductDao()
    val clientDao = ClientDao()
    val salesDao = SalesDao()
    val saleItemsDao = SaleItemsDao()

    routing {
        get("/") {
            call.respondText("Ktor API - CRUD Operations Available")
        }



        route("/products") {
            get {
                val products = productDao.findAll()
                call.respond(HttpStatusCode.OK, products)
            }

            get("/{id}") {
                val id = call.parameters["id"]?.toIntOrNull()
                if (id == null) {
                    call.respond(HttpStatusCode.BadRequest, "Invalid ID")
                    return@get
                }

                val product = productDao.findById(id)
                if (product != null) {
                    call.respond(HttpStatusCode.OK, product)
                } else {
                    call.respond(HttpStatusCode.NotFound, "Product not found")
                }
            }

            post {
                try {
                    val product = call.receive<Product>()
                    val createdProduct = productDao.insert(product)
                    call.respond(HttpStatusCode.Created, createdProduct)
                } catch (e: Exception) {
                    call.respond(HttpStatusCode.BadRequest, "Invalid product data")
                }
            }

            put("/{id}") {
                val id = call.parameters["id"]?.toIntOrNull()
                if (id == null) {
                    call.respond(HttpStatusCode.BadRequest, "Invalid ID")
                    return@put
                }

                try {
                    val product = call.receive<Product>()
                    val updatedProduct = productDao.update(id, product)
                    if (updatedProduct != null) {
                        call.respond(HttpStatusCode.OK, updatedProduct)
                    } else {
                        call.respond(HttpStatusCode.NotFound, "Product not found")
                    }
                } catch (e: Exception) {
                    call.respond(HttpStatusCode.BadRequest, "Invalid product data")
                }
            }

            delete("/{id}") {
                val id = call.parameters["id"]?.toIntOrNull()
                if (id == null) {
                    call.respond(HttpStatusCode.BadRequest, "Invalid ID")
                    return@delete
                }

                val deleted = productDao.delete(id)
                if (deleted) {
                    call.respond(HttpStatusCode.OK, "Product deleted successfully")
                } else {
                    call.respond(HttpStatusCode.NotFound, "Product not found")
                }
            }
        }



        route("/customers") {
            get {
                val customers = clientDao.findAll()
                call.respond(HttpStatusCode.OK, customers)
            }

            get("/{id}") {
                val id = call.parameters["id"]?.toIntOrNull()
                if (id == null) {
                    call.respond(HttpStatusCode.BadRequest, "Invalid ID")
                    return@get
                }

                val customer = clientDao.findById(id)
                if (customer != null) {
                    call.respond(HttpStatusCode.OK, customer)
                } else {
                    call.respond(HttpStatusCode.NotFound, "Customer not found")
                }
            }

            post {
                try {
                    val customer = call.receive<Client>()
                    val createdCustomer = clientDao.insert(customer)
                    call.respond(HttpStatusCode.Created, createdCustomer)
                } catch (e: Exception) {
                    call.respond(HttpStatusCode.BadRequest, "Invalid customer data")
                }
            }

            put("/{id}") {
                val id = call.parameters["id"]?.toIntOrNull()
                if (id == null) {
                    call.respond(HttpStatusCode.BadRequest, "Invalid ID")
                    return@put
                }

                try {
                    val customer = call.receive<Client>()
                    val updatedCustomer = clientDao.update(id, customer)
                    if (updatedCustomer != null) {
                        call.respond(HttpStatusCode.OK, updatedCustomer)
                    } else {
                        call.respond(HttpStatusCode.NotFound, "Customer not found")
                    }
                } catch (e: Exception) {
                    call.respond(HttpStatusCode.BadRequest, "Invalid customer data")
                }
            }

            delete("/{id}") {
                val id = call.parameters["id"]?.toIntOrNull()
                if (id == null) {
                    call.respond(HttpStatusCode.BadRequest, "Invalid ID")
                    return@delete
                }

                val deleted = clientDao.delete(id)
                if (deleted) {
                    call.respond(HttpStatusCode.OK, "Customer deleted successfully")
                } else {
                    call.respond(HttpStatusCode.NotFound, "Customer not found")
                }
            }
        }



        route("/sales") {
            get {
                val sales = salesDao.findAll()
                call.respond(HttpStatusCode.OK, sales)
            }

            get("/{id}") {
                val id = call.parameters["id"]?.toIntOrNull()
                if (id == null) {
                    call.respond(HttpStatusCode.BadRequest, "Invalid ID")
                    return@get
                }

                val sale = salesDao.findById(id)
                if (sale != null) {
                    call.respond(HttpStatusCode.OK, sale)
                } else {
                    call.respond(HttpStatusCode.NotFound, "Sale not found")
                }
            }

            post {
                try {
                    val sale = call.receive<Sale>()
                    val createdSale = salesDao.insert(sale)
                    call.respond(HttpStatusCode.Created, createdSale)
                } catch (e: Exception) {
                    call.respond(HttpStatusCode.BadRequest, "Invalid sale data")
                }
            }

            put("/{id}") {
                val id = call.parameters["id"]?.toIntOrNull()
                if (id == null) {
                    call.respond(HttpStatusCode.BadRequest, "Invalid ID")
                    return@put
                }

                try {
                    val sale = call.receive<Sale>()
                    val updatedSale = salesDao.update(id, sale)
                    if (updatedSale != null) {
                        call.respond(HttpStatusCode.OK, updatedSale)
                    } else {
                        call.respond(HttpStatusCode.NotFound, "Sale not found")
                    }
                } catch (e: Exception) {
                    call.respond(HttpStatusCode.BadRequest, "Invalid sale data")
                }
            }

            delete("/{id}") {
                val id = call.parameters["id"]?.toIntOrNull()
                if (id == null) {
                    call.respond(HttpStatusCode.BadRequest, "Invalid ID")
                    return@delete
                }

                val deleted = salesDao.delete(id)
                if (deleted) {
                    call.respond(HttpStatusCode.OK, "Sale deleted successfully")
                } else {
                    call.respond(HttpStatusCode.NotFound, "Sale not found")
                }
            }
        }



        route("/sale-items") {
            get {
                val saleItems = saleItemsDao.findAll()
                call.respond(HttpStatusCode.OK, saleItems)
            }

            get("/{id}") {
                val id = call.parameters["id"]?.toIntOrNull()
                if (id == null) {
                    call.respond(HttpStatusCode.BadRequest, "Invalid ID")
                    return@get
                }

                val saleItem = saleItemsDao.findById(id)
                if (saleItem != null) {
                    call.respond(HttpStatusCode.OK, saleItem)
                } else {
                    call.respond(HttpStatusCode.NotFound, "Sale item not found")
                }
            }

            get("/by-sale/{saleId}") {
                val saleId = call.parameters["saleId"]?.toIntOrNull()
                if (saleId == null) {
                    call.respond(HttpStatusCode.BadRequest, "Invalid Sale ID")
                    return@get
                }

                val saleItems = saleItemsDao.findBySaleId(saleId)
                call.respond(HttpStatusCode.OK, saleItems)
            }

            post {
                try {
                    val saleItem = call.receive<SaleItem>()
                    val createdSaleItem = saleItemsDao.insert(saleItem)
                    call.respond(HttpStatusCode.Created, createdSaleItem)
                } catch (e: Exception) {
                    call.respond(HttpStatusCode.BadRequest, "Invalid sale item data")
                }
            }

            put("/{id}") {
                val id = call.parameters["id"]?.toIntOrNull()
                if (id == null) {
                    call.respond(HttpStatusCode.BadRequest, "Invalid ID")
                    return@put
                }

                try {
                    val saleItem = call.receive<SaleItem>()
                    val updatedSaleItem = saleItemsDao.update(id, saleItem)
                    if (updatedSaleItem != null) {
                        call.respond(HttpStatusCode.OK, updatedSaleItem)
                    } else {
                        call.respond(HttpStatusCode.NotFound, "Sale item not found")
                    }
                } catch (e: Exception) {
                    call.respond(HttpStatusCode.BadRequest, "Invalid sale item data")
                }
            }

            delete("/{id}") {
                val id = call.parameters["id"]?.toIntOrNull()
                if (id == null) {
                    call.respond(HttpStatusCode.BadRequest, "Invalid ID")
                    return@delete
                }

                val deleted = saleItemsDao.delete(id)
                if (deleted) {
                    call.respond(HttpStatusCode.OK, "Sale item deleted successfully")
                } else {
                    call.respond(HttpStatusCode.NotFound, "Sale item not found")
                }
            }
        }
    }
}
