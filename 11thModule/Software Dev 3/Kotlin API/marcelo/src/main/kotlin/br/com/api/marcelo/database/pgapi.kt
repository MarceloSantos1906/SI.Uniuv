package br.com.api.br.com.api.marcelo.database

import com.zaxxer.hikari.HikariConfig
import  com.zaxxer.hikari.HikariDataSource
import java.sql.Connection
import javax.sql.DataSource

object Database {
    private val dataSource: DataSource

    init {
        val config = HikariConfig().apply {
            driverClassName = "org.postgresql.Driver"
            jdbcUrl = System.getenv("DATABASE_URL") ?: "jdbc:postgresql://localhost:5432/basektor"
            username = System.getenv("DB_USER") ?: "postgres"
            password = System.getenv("DB_PASSWORD") ?: "root"
            maximumPoolSize = 50
            minimumIdle = 2
            connectionTimeout = 30000
            idleTimeout = 600000
            maxLifetime = 1800000
        }
        dataSource = HikariDataSource(config)
    }

    fun getConnection(): Connection = dataSource.connection
}