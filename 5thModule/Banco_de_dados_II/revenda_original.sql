-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: revenda
-- ------------------------------------------------------
-- Server version	8.0.35

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `carros`
--

create database revenda;
use revenda;

DROP TABLE IF EXISTS `carros`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `carros` (
  `id_carro` int NOT NULL AUTO_INCREMENT,
  `ano` year DEFAULT NULL,
  `valor` decimal(8,2) DEFAULT NULL,
  `modelo` int NOT NULL,
  PRIMARY KEY (`id_carro`),
  KEY `fk_carros_modelos1_idx` (`modelo`),
  CONSTRAINT `fk_carros_modelos1` FOREIGN KEY (`modelo`) REFERENCES `modelos` (`id_modelo`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carros`
--

LOCK TABLES `carros` WRITE;
/*!40000 ALTER TABLE `carros` DISABLE KEYS */;
INSERT INTO `carros` VALUES (1,2009,20000.00,1),(2,2005,4000.00,2),(3,2024,78000.00,3);
/*!40000 ALTER TABLE `carros` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cidades`
--

DROP TABLE IF EXISTS `cidades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cidades` (
  `id_cidade` int NOT NULL AUTO_INCREMENT,
  `nome_cidade` varchar(45) NOT NULL,
  `estado` char(2) NOT NULL,
  PRIMARY KEY (`id_cidade`),
  KEY `fk_cidades_estados1_idx` (`estado`),
  CONSTRAINT `fk_cidades_estados1` FOREIGN KEY (`estado`) REFERENCES `estados` (`uf_estado`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cidades`
--

LOCK TABLES `cidades` WRITE;
/*!40000 ALTER TABLE `cidades` DISABLE KEYS */;
INSERT INTO `cidades` VALUES (1,'Porto Alegre','RS'),(2,'Florianópolis','SC'),(3,'Curitiba','PR');
/*!40000 ALTER TABLE `cidades` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes` (
  `id_cliente` int NOT NULL AUTO_INCREMENT,
  `nome_cliente` varchar(45) NOT NULL,
  `cidades_id_cidade` int NOT NULL,
  PRIMARY KEY (`id_cliente`),
  KEY `fk_clientes_cidades1_idx` (`cidades_id_cidade`),
  CONSTRAINT `fk_clientes_cidades1` FOREIGN KEY (`cidades_id_cidade`) REFERENCES `cidades` (`id_cidade`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES (1,'Fran',1),(2,'Marcelo',2),(3,'Anderson',3);
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estados`
--

DROP TABLE IF EXISTS `estados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estados` (
  `uf_estado` char(2) NOT NULL,
  `nome_estado` varchar(45) NOT NULL,
  PRIMARY KEY (`uf_estado`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estados`
--

LOCK TABLES `estados` WRITE;
/*!40000 ALTER TABLE `estados` DISABLE KEYS */;
INSERT INTO `estados` VALUES ('PR','Paraná'),('RS','Rio Grande do Sul'),('SC','Santa Catarina');
/*!40000 ALTER TABLE `estados` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `marcas`
--

DROP TABLE IF EXISTS `marcas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `marcas` (
  `id_marca` int NOT NULL AUTO_INCREMENT,
  `nome_marca` varchar(45) NOT NULL,
  PRIMARY KEY (`id_marca`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `marcas`
--

LOCK TABLES `marcas` WRITE;
/*!40000 ALTER TABLE `marcas` DISABLE KEYS */;
INSERT INTO `marcas` VALUES (1,'Fiat'),(2,'Ford'),(3,'Kia');
/*!40000 ALTER TABLE `marcas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `modelos`
--

DROP TABLE IF EXISTS `modelos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `modelos` (
  `id_modelo` int NOT NULL AUTO_INCREMENT,
  `nome_modelo` varchar(45) NOT NULL,
  `marca` int NOT NULL,
  PRIMARY KEY (`id_modelo`),
  KEY `fk_modelos_marcas_idx` (`marca`),
  CONSTRAINT `fk_modelos_marcas` FOREIGN KEY (`marca`) REFERENCES `marcas` (`id_marca`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `modelos`
--

LOCK TABLES `modelos` WRITE;
/*!40000 ALTER TABLE `modelos` DISABLE KEYS */;
INSERT INTO `modelos` VALUES (1,'Ká',2),(2,'Uno',1),(3,'Kiro',3);
/*!40000 ALTER TABLE `modelos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vendas`
--

DROP TABLE IF EXISTS `vendas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vendas` (
  `id_venda` int NOT NULL AUTO_INCREMENT,
  `data_venda` date NOT NULL,
  `carro` int NOT NULL,
  `cliente` int NOT NULL,
  `vendedor` int NOT NULL,
  PRIMARY KEY (`id_venda`),
  KEY `fk_vendas_carros1_idx` (`carro`),
  KEY `fk_vendas_clientes1_idx` (`cliente`),
  KEY `fk_vendas_vendedores1_idx` (`vendedor`),
  CONSTRAINT `fk_vendas_carros1` FOREIGN KEY (`carro`) REFERENCES `carros` (`id_carro`),
  CONSTRAINT `fk_vendas_clientes1` FOREIGN KEY (`cliente`) REFERENCES `clientes` (`id_cliente`),
  CONSTRAINT `fk_vendas_vendedores1` FOREIGN KEY (`vendedor`) REFERENCES `vendedores` (`id_vendedor`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vendas`
--

LOCK TABLES `vendas` WRITE;
/*!40000 ALTER TABLE `vendas` DISABLE KEYS */;
INSERT INTO `vendas` VALUES (1,'2024-04-10',1,1,1),(2,'2024-03-10',2,1,2),(3,'2024-04-10',3,2,2);
/*!40000 ALTER TABLE `vendas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vendedores`
--

DROP TABLE IF EXISTS `vendedores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vendedores` (
  `id_vendedor` int NOT NULL AUTO_INCREMENT,
  `nome_vendedor` varchar(45) NOT NULL,
  PRIMARY KEY (`id_vendedor`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vendedores`
--

LOCK TABLES `vendedores` WRITE;
/*!40000 ALTER TABLE `vendedores` DISABLE KEYS */;
INSERT INTO `vendedores` VALUES (1,'Marcos'),(2,'Pedro');
/*!40000 ALTER TABLE `vendedores` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-08 11:41:14
