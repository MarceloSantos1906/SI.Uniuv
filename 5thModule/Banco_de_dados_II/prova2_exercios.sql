-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: prova2
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
-- Table structure for table `animais`
--

create database prova2;
use prova2;

DROP TABLE IF EXISTS `animais`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `animais` (
  `id_animal` int NOT NULL AUTO_INCREMENT,
  `nome_animal` varchar(45) NOT NULL,
  `ano_nascimento` year NOT NULL,
  `peso` int NOT NULL,
  `valor_compra` decimal(8,2) NOT NULL,
  `dono` int NOT NULL,
  `especie` int NOT NULL,
  `raca` int NOT NULL,
  PRIMARY KEY (`id_animal`),
  KEY `fk_animais_donos_idx` (`dono`),
  KEY `fk_animais_especies1_idx` (`especie`),
  KEY `fk_animais_racas1_idx` (`raca`),
  CONSTRAINT `fk_animais_donos` FOREIGN KEY (`dono`) REFERENCES `donos` (`id_dono`),
  CONSTRAINT `fk_animais_especies1` FOREIGN KEY (`especie`) REFERENCES `especies` (`id_especie`),
  CONSTRAINT `fk_animais_racas1` FOREIGN KEY (`raca`) REFERENCES `racas` (`id_raca`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `animais`
--

LOCK TABLES `animais` WRITE;
/*!40000 ALTER TABLE `animais` DISABLE KEYS */;
INSERT INTO `animais` VALUES (1,'Thor',2020,54,1000.00,1,1,1),(2,'Bob',2024,10,500.00,2,2,2),(3,'Jubileu',2023,45,1000.00,2,1,2);
/*!40000 ALTER TABLE `animais` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `consultas`
--

DROP TABLE IF EXISTS `consultas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `consultas` (
  `id_consulta` int NOT NULL AUTO_INCREMENT,
  `data_consulta` date NOT NULL,
  `valor_consulta` decimal(8,2) NOT NULL,
  `animal` int NOT NULL,
  `veterinario` int NOT NULL,
  PRIMARY KEY (`id_consulta`),
  KEY `fk_consultas_animais1_idx` (`animal`),
  KEY `fk_consultas_veterinarios1_idx` (`veterinario`),
  CONSTRAINT `fk_consultas_animais1` FOREIGN KEY (`animal`) REFERENCES `animais` (`id_animal`),
  CONSTRAINT `fk_consultas_veterinarios1` FOREIGN KEY (`veterinario`) REFERENCES `veterinarios` (`id_veterinario`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `consultas`
--

LOCK TABLES `consultas` WRITE;
/*!40000 ALTER TABLE `consultas` DISABLE KEYS */;
INSERT INTO `consultas` VALUES (1,'2024-02-04',100.00,1,1),(2,'2024-03-04',500.00,2,2),(3,'2024-04-04',350.00,1,2),(4,'2024-01-04',700.00,1,1);
/*!40000 ALTER TABLE `consultas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `donos`
--

DROP TABLE IF EXISTS `donos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `donos` (
  `id_dono` int NOT NULL AUTO_INCREMENT,
  `nome_dono` varchar(45) NOT NULL,
  `uf_estado` char(2) DEFAULT NULL,
  PRIMARY KEY (`id_dono`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `donos`
--

LOCK TABLES `donos` WRITE;
/*!40000 ALTER TABLE `donos` DISABLE KEYS */;
INSERT INTO `donos` VALUES (1,'Ana','PR'),(2,'Carlos','SC');
/*!40000 ALTER TABLE `donos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `especialidades`
--

DROP TABLE IF EXISTS `especialidades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `especialidades` (
  `id_especialidade` int NOT NULL AUTO_INCREMENT,
  `nome_especialidade` varchar(45) NOT NULL,
  PRIMARY KEY (`id_especialidade`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `especialidades`
--

LOCK TABLES `especialidades` WRITE;
/*!40000 ALTER TABLE `especialidades` DISABLE KEYS */;
INSERT INTO `especialidades` VALUES (1,'Cachorros de grande porte'),(2,'Felinos');
/*!40000 ALTER TABLE `especialidades` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `especialidades_veterinarios`
--

DROP TABLE IF EXISTS `especialidades_veterinarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `especialidades_veterinarios` (
  `id` varchar(45) NOT NULL,
  `veterinario` int NOT NULL,
  `especialidade` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_veterinarios_has_especialidades_especialidades1_idx` (`especialidade`),
  KEY `fk_veterinarios_has_especialidades_veterinarios1_idx` (`veterinario`),
  CONSTRAINT `fk_veterinarios_has_especialidades_especialidades1` FOREIGN KEY (`especialidade`) REFERENCES `especialidades` (`id_especialidade`),
  CONSTRAINT `fk_veterinarios_has_especialidades_veterinarios1` FOREIGN KEY (`veterinario`) REFERENCES `veterinarios` (`id_veterinario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `especialidades_veterinarios`
--

LOCK TABLES `especialidades_veterinarios` WRITE;
/*!40000 ALTER TABLE `especialidades_veterinarios` DISABLE KEYS */;
INSERT INTO `especialidades_veterinarios` VALUES ('1',1,1),('2',2,2);
/*!40000 ALTER TABLE `especialidades_veterinarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `especies`
--

DROP TABLE IF EXISTS `especies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `especies` (
  `id_especie` int NOT NULL AUTO_INCREMENT,
  `nome_especie` varchar(45) NOT NULL,
  PRIMARY KEY (`id_especie`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `especies`
--

LOCK TABLES `especies` WRITE;
/*!40000 ALTER TABLE `especies` DISABLE KEYS */;
INSERT INTO `especies` VALUES (1,'Cachorros'),(2,'Gatos');
/*!40000 ALTER TABLE `especies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `racas`
--

DROP TABLE IF EXISTS `racas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `racas` (
  `id_raca` int NOT NULL AUTO_INCREMENT,
  `nome_raca` varchar(45) NOT NULL,
  PRIMARY KEY (`id_raca`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `racas`
--

LOCK TABLES `racas` WRITE;
/*!40000 ALTER TABLE `racas` DISABLE KEYS */;
INSERT INTO `racas` VALUES (1,'Pastor Alemão'),(2,'Belga');
/*!40000 ALTER TABLE `racas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `veterinarios`
--

DROP TABLE IF EXISTS `veterinarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `veterinarios` (
  `id_veterinario` int NOT NULL AUTO_INCREMENT,
  `nome_veterinario` varchar(45) NOT NULL,
  PRIMARY KEY (`id_veterinario`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `veterinarios`
--

LOCK TABLES `veterinarios` WRITE;
/*!40000 ALTER TABLE `veterinarios` DISABLE KEYS */;
INSERT INTO `veterinarios` VALUES (1,'Paulo'),(2,'Ramon');
/*!40000 ALTER TABLE `veterinarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-05 13:27:54
