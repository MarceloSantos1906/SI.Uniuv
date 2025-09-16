package br.com.api.br.com.api.marcelo

import br.com.api.br.com.api.marcelo.database.Database
import br.com.api.configureDatabases
import br.com.api.configureSerialization
import io.ktor.serialization.kotlinx.json.json
import io.ktor.server.application.*
import io.ktor.server.netty.EngineMain
import io.ktor.server.plugins.contentnegotiation.*
import kotlinx.serialization.json.Json

fun main(args: Array<String>) {
    EngineMain.main(args)
}

fun Application.configureSerialization() {
    install (ContentNegotiation) {
        json( Json {
            prettyPrint = true
            isLenient = true
            ignoreUnknownKeys = true
            encodeDefaults = true
            explicitNulls = true
        })
    }
}

fun Application.module() {
    Database
    configureSerialization()
    configureRouting()
}
