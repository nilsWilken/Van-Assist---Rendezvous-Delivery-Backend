-- MySQL dump 10.16  Distrib 10.1.44-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: vanassist
-- ------------------------------------------------------
-- Server version	10.1.44-MariaDB-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `courier`
--

DROP TABLE IF EXISTS `courier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `courier` (
  `id` varchar(100) NOT NULL,
  `first_name` varchar(200) NOT NULL,
  `last_name` varchar(200) NOT NULL,
  `user_name` varchar(100) NOT NULL,
  `phone_number` varchar(100) NOT NULL,
  `dark_mode` tinyint(1) NOT NULL,
  `help_mode` tinyint(1) NOT NULL,
  `ambient_intelligence_mode` tinyint(1) NOT NULL,
  `time_based_dark_mode` tinyint(1) NOT NULL,
  `intelligent_driving_mode` tinyint(1) NOT NULL,
  `gamification_mode` tinyint(1) NOT NULL,
  `size_dependent_waiting_mode` tinyint(1) NOT NULL,
  `dynamic_content_mode` tinyint(1) NOT NULL,
  `language_code` varchar(100) NOT NULL,
  `verification_token` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `courier`
--

LOCK TABLES `courier` WRITE;
/*!40000 ALTER TABLE `courier` DISABLE KEYS */;
INSERT INTO `courier` VALUES ('474ccac0-92d2-4f3f-8d39-b79557a455f5','VanAssist','2019','vanassist19@gmail.com','',0,0,0,0,1,0,0,0,'en_US','6b763c99-cfed-4735-afa8-168b25fa393b'),('9f32d526-b4df-4c8f-a569-f855b016237d','Elon','Musk','elon.musk@tesla.com','',0,0,0,0,0,0,0,0,'de_DE','f85f8629-1edd-4f02-9fd2-eb45b9346336'),('bit','Max','Mustermann','vanassist@bridging-it.de','',1,0,0,0,0,0,0,0,'de_DE','1fa52436-9f16-4197-a9dc-f1848026e2b7'),('uni-mannheim','Christian','Kristoff','vanassist@uni-mannheim.de','',0,0,0,1,1,1,1,1,'de_DE','f0cbac32-c179-4965-8b6c-80df0c4e9285'),('vanassist','Axel','Herbstreith','axel.herbstreith@web.de','+491728477740',0,1,1,1,0,1,0,1,'en_US','0d1b3393-1327-4aaf-921e-28ad2a1fbf81');
/*!40000 ALTER TABLE `courier` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `delivery`
--

DROP TABLE IF EXISTS `delivery`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `delivery` (
  `courier_id` varchar(100) NOT NULL,
  `parcel_id` varchar(100) NOT NULL,
  `van_id` varchar(100) NOT NULL,
  `parcel_delivery_position` int(11) NOT NULL,
  PRIMARY KEY (`parcel_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `delivery`
--

LOCK TABLES `delivery` WRITE;
/*!40000 ALTER TABLE `delivery` DISABLE KEYS */;
INSERT INTO `delivery` VALUES ('474ccac0-92d2-4f3f-8d39-b79557a455f5','03043f0f-739f-423e-9ed4-99394d8d6506','0725f499-0719-4b70-abb2-64b963122ead',12),('474ccac0-92d2-4f3f-8d39-b79557a455f5','0cea96bd-e725-402b-b094-ab594620be28','0725f499-0719-4b70-abb2-64b963122ead',7),('474ccac0-92d2-4f3f-8d39-b79557a455f5','185eb79f-2e05-448f-b6b4-20758cdf3bb1','0725f499-0719-4b70-abb2-64b963122ead',5),('474ccac0-92d2-4f3f-8d39-b79557a455f5','351128b4-3e1a-441b-9ba9-698c0e504bb2 	','0725f499-0719-4b70-abb2-64b963122ead',25),('474ccac0-92d2-4f3f-8d39-b79557a455f5','35bdac06-740a-4734-bd42-6a3a94996212','0725f499-0719-4b70-abb2-64b963122ead',14),('474ccac0-92d2-4f3f-8d39-b79557a455f5','37a96e73-345a-49c7-a064-a996f99d31ab','0725f499-0719-4b70-abb2-64b963122ead',2),('474ccac0-92d2-4f3f-8d39-b79557a455f5','3843e2e1-d99f-4376-8bbb-08f257509a34','0725f499-0719-4b70-abb2-64b963122ead',15),('474ccac0-92d2-4f3f-8d39-b79557a455f5','393c2dc0-0cd5-439c-a28d-f33ca2827bfb','0725f499-0719-4b70-abb2-64b963122ead',19),('bcecabec-cc9d-4f9f-946f-9b183d0007b4','441fb071-7fe2-4a4b-9ad6-57127aa5a063','0725f499-0719-4b70-abb2-64b963122ead',6),('bcecabec-cc9d-4f9f-946f-9b183d0007b4','47472ac8-a49a-4ddf-85e3-f6f66ee7cbf6','0725f499-0719-4b70-abb2-64b963122ead',4),('bcecabec-cc9d-4f9f-946f-9b183d0007b4','49477c14-b25b-4b20-8fd4-4433654b19b7','0725f499-0719-4b70-abb2-64b963122ead',2),('474ccac0-92d2-4f3f-8d39-b79557a455f5','4d8e1933-8a24-43ca-a41d-9e2ad476e1c2','0725f499-0719-4b70-abb2-64b963122ead',6),('474ccac0-92d2-4f3f-8d39-b79557a455f5','61aad1d6-ca30-40e2-96cf-9b36e2a1c5dc','0725f499-0719-4b70-abb2-64b963122ead',18),('474ccac0-92d2-4f3f-8d39-b79557a455f5','6ae59be0-b622-4567-8e39-25b3b3462ac4','0725f499-0719-4b70-abb2-64b963122ead',1),('474ccac0-92d2-4f3f-8d39-b79557a455f5','6bdf58b8-8000-414c-9f4a-c827c9c0431b','0725f499-0719-4b70-abb2-64b963122ead',17),('bcecabec-cc9d-4f9f-946f-9b183d0007b4','6c776159-df44-49d9-bdac-d66282f51a58','0725f499-0719-4b70-abb2-64b963122ead',1),('bcecabec-cc9d-4f9f-946f-9b183d0007b4','76e0fd17-4aca-41a6-b806-58e21bf94b26','0725f499-0719-4b70-abb2-64b963122ead',5),('474ccac0-92d2-4f3f-8d39-b79557a455f5','77134d4c-473c-4345-97a8-0ac1d558b7c7','0725f499-0719-4b70-abb2-64b963122ead',4),('474ccac0-92d2-4f3f-8d39-b79557a455f5','7c7a06a1-71a3-48d0-a120-64715260ed02','0725f499-0719-4b70-abb2-64b963122ead',21),('474ccac0-92d2-4f3f-8d39-b79557a455f5','7da644d1-6e33-4f5f-a80c-81b23f5b6207','0725f499-0719-4b70-abb2-64b963122ead',3),('bit','bit1','bit_van',1),('bit','bit2','bit_van',2),('bit','bit3','bit_van',3),('bit','bit4','bit_van',4),('bit','bit5','bit_van',5),('bit','bit6','bit_van',6),('bit','bit7','bit_van',7),('bit','bit8','bit_van',8),('bit','bit9','bit_van',9),('474ccac0-92d2-4f3f-8d39-b79557a455f5','c7db74b4-e544-4197-9b53-2724e99342f3','0725f499-0719-4b70-abb2-64b963122ead',10),('474ccac0-92d2-4f3f-8d39-b79557a455f5','c923d6f5-d6fe-4cd6-b889-df33d550ceed','0725f499-0719-4b70-abb2-64b963122ead',9),('bcecabec-cc9d-4f9f-946f-9b183d0007b4','c9425184-461e-4d7b-8e87-07e838e8ce3f','0725f499-0719-4b70-abb2-64b963122ead',3),('474ccac0-92d2-4f3f-8d39-b79557a455f5','d3f03418-193a-4348-99b0-a9d9bb071b09','0725f499-0719-4b70-abb2-64b963122ead',8),('474ccac0-92d2-4f3f-8d39-b79557a455f5','d54ae8f1-c332-45f0-bcdb-a81427a7fd62','0725f499-0719-4b70-abb2-64b963122ead',22),('474ccac0-92d2-4f3f-8d39-b79557a455f5','d5e8e9c5-20a4-493c-b7af-a8eb5ec2410b','0725f499-0719-4b70-abb2-64b963122ead',20),('474ccac0-92d2-4f3f-8d39-b79557a455f5','eb8650dd-bc9d-407a-9cd0-e4632ef0bbbf','0725f499-0719-4b70-abb2-64b963122ead',11),('474ccac0-92d2-4f3f-8d39-b79557a455f5','ebe594e3-456e-45b6-b21e-d8aa986627e1','0725f499-0719-4b70-abb2-64b963122ead',24),('474ccac0-92d2-4f3f-8d39-b79557a455f5','f8efa930-f424-4154-969d-8e8fdc26893d','0725f499-0719-4b70-abb2-64b963122ead',23),('474ccac0-92d2-4f3f-8d39-b79557a455f5','fbc7dfa1-3c4f-4e20-8001-d0f62e5b442b','0725f499-0719-4b70-abb2-64b963122ead',16),('474ccac0-92d2-4f3f-8d39-b79557a455f5','fcc06b00-4f61-47cf-a7f7-9cb95b4a2287','0725f499-0719-4b70-abb2-64b963122ead',13),('uni-mannheim','uma1','519ba706-42bd-4e49-8886-0892e69eed61',5),('uni-mannheim','uma10','519ba706-42bd-4e49-8886-0892e69eed61',14),('uni-mannheim','uma11','519ba706-42bd-4e49-8886-0892e69eed61',3),('uni-mannheim','uma12','519ba706-42bd-4e49-8886-0892e69eed61',10),('uni-mannheim','uma13','519ba706-42bd-4e49-8886-0892e69eed61',17),('uni-mannheim','uma14','519ba706-42bd-4e49-8886-0892e69eed61',12),('uni-mannheim','uma15','519ba706-42bd-4e49-8886-0892e69eed61',4),('uni-mannheim','uma16','519ba706-42bd-4e49-8886-0892e69eed61',20),('uni-mannheim','uma17','519ba706-42bd-4e49-8886-0892e69eed61',21),('uni-mannheim','uma18','519ba706-42bd-4e49-8886-0892e69eed61',9),('uni-mannheim','uma19','519ba706-42bd-4e49-8886-0892e69eed61',8),('uni-mannheim','uma2','519ba706-42bd-4e49-8886-0892e69eed61',11),('uni-mannheim','uma20','519ba706-42bd-4e49-8886-0892e69eed61',15),('uni-mannheim','uma21','519ba706-42bd-4e49-8886-0892e69eed61',16),('uni-mannheim','uma3','519ba706-42bd-4e49-8886-0892e69eed61',2),('uni-mannheim','uma4','519ba706-42bd-4e49-8886-0892e69eed61',18),('uni-mannheim','uma5','519ba706-42bd-4e49-8886-0892e69eed61',6),('uni-mannheim','uma6','519ba706-42bd-4e49-8886-0892e69eed61',13),('uni-mannheim','uma7','519ba706-42bd-4e49-8886-0892e69eed61',19),('uni-mannheim','uma8','519ba706-42bd-4e49-8886-0892e69eed61',1),('uni-mannheim','uma9','519ba706-42bd-4e49-8886-0892e69eed61',7);
/*!40000 ALTER TABLE `delivery` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `parcel`
--

DROP TABLE IF EXISTS `parcel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `parcel` (
  `id` varchar(100) NOT NULL,
  `state` int(11) NOT NULL,
  `name_of_recipient` varchar(200) NOT NULL,
  `phone_number` varchar(100) DEFAULT NULL,
  `additional_recipient_information` varchar(200) DEFAULT NULL,
  `latitude` varchar(100) NOT NULL,
  `longitude` varchar(100) NOT NULL,
  `floor` int(11) DEFAULT '0',
  `city` varchar(200) NOT NULL,
  `address` varchar(200) NOT NULL,
  `additional_address_information` varchar(200) DEFAULT NULL,
  `package_count` int(11) DEFAULT '0',
  `weight` double(11,2) DEFAULT '0.00',
  `width` double(11,2) DEFAULT '0.00',
  `height` double(11,2) DEFAULT '0.00',
  `length` double(11,2) DEFAULT '0.00',
  `parkingArea` varchar(100) DEFAULT NULL,
  `verification_token` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parcel`
--

LOCK TABLES `parcel` WRITE;
/*!40000 ALTER TABLE `parcel` DISABLE KEYS */;
INSERT INTO `parcel` VALUES ('id',0,'name_of_recipient','phone_number','additional_recipient_information','latitude','longitude',0,'city','address','additional_address_information',0,0.00,0.00,0.00,0.00,NULL,'verification_token\r'),('bit1',0,'Haltepunkt A',NULL,NULL,'49.417.843','8.675.079',0,'69120 Heidelberg','Berliner Straße 41',NULL,0,0.00,0.00,0.00,0.00,'bit_stop_1','5f914318-b770-4084-a9e5-828649e80cd6'),('bit2',0,'Pro & Fi GmbH','+49 6221 12345678',NULL,'49.418.131','8.675.421',4,'69120 Heidelberg','Berliner Straße 41',NULL,1,2.00,10.00,3.00,25.00,'bit_stop_1','\r'),('bit3',0,'Start-Up & Go-Pro GmbH','+49 6221 12345679','RETOURE','49.418.096','8.675.537',4,'69120 Heidelberg','Berliner Straße 41',NULL,1,10.00,25.00,5.00,25.00,'bit_stop_1','\r'),('bit4',0,'FantIdea GmbH & Co. KG','+49 6221 12345680',NULL,'49.418.121','8.675.813',4,'69120 Heidelberg','Berliner Straße 41','ASG_HARDCODED_ID_LATLON',1,25.00,35.00,10.00,35.00,'bit_stop_1','\r'),('bit5',0,'FantIdea GmbH & Co. KG (ASG LATLON)','+49 6221 12345680',NULL,'49.418.057','8.675.824',4,'69120 Heidelberg','Berliner Straße 41',NULL,1,25.00,35.00,10.00,35.00,'bit_stop_1','\r'),('bit6',0,'Su-Personal GmbH','+49 6221 12345681',NULL,'49.418.174','8.675.248',4,'69120 Heidelberg','Berliner Straße 41','ASG_HARDCODED_ID',1,28.00,20.00,20.00,70.00,'bit_stop_1','\r'),('bit7',0,'Schall & Rauch GmbH (ASG)','+49 6221 12345682','PICKUP','49.418.506','8.675.246',4,'69120 Heidelberg','Berliner Straße 41',NULL,1,30.00,35.00,35.00,150.00,'bit_stop_1','\r'),('bit8',0,'Easy2Reach GmbH','+49 6221 12345683',NULL,'49.418.538','8.675.247',4,'69120 Heidelberg','Berliner Straße 41',NULL,1,31.50,30.00,30.00,175.00,'bit_stop_1','\r'),('bit9',0,'Haltepunkt B',NULL,NULL,'49.418.622','8.675.089',0,'69120 Heidelberg','Berliner Straße 43',NULL,0,0.00,0.00,0.00,0.00,'bit_stop_1','\r'),('uma1',0,'Heike Windisch','4.92E+11',NULL,'49.4155739','8.679868385',0,'69120 Heidelberg','Schröderstraße 101',NULL,0,0.00,10.00,15.00,20.00,NULL,'cb1665d8-162d-4b7b-8718-e5031917e576'),('03043f0f-739f-423e-9ed4-99394d8d6506',0,'Tillmann Kestenbaum',NULL,NULL,'49.4138959','8.684764',0,'69120 Heidelberg','Wilhelm-Blumstra?e 12',NULL,0,74.00,34.00,21.00,14.00,NULL,'2d22273b-1895-4f64-b193-a8f0164d27ee\r'),('0cea96bd-e725-402b-b094-ab594620be28',0,'Matthias Krehl',NULL,NULL,'49.41345865','8.683155677',0,'69120 Heidelberg','Quinckestra?e 10',NULL,0,1478.00,37.00,84.00,21.00,NULL,'75c5c7e7-b84a-4e5c-864f-ab11cbb971ed\r'),('uma2',0,'Heinz Schirmer',NULL,NULL,'49.41794','8.68166',0,'69120 Heidelberg','Wielandstraße 33',NULL,0,350.00,20.00,40.00,50.00,NULL,'03a2adbb-688b-40d0-82fb-61259d708051\r'),('185eb79f-2e05-448f-b6b4-20758cdf3bb1',0,'Eggert Schaell',NULL,NULL,'49.4133053','8.682748188',0,'69120 Heidelberg','Quinckestra?e 9 ',NULL,0,478.00,64.00,34.00,27.00,NULL,'8f3f596e-9d5d-40d5-93ed-2d27d8ec704c\r'),('uma3',0,'Stefan Schaber','01726-355045','2.Stock ','49.417184','8.678468',0,'69120 Heidelberg','Mönchhofstraße 60',NULL,0,200.00,40.00,23.00,5.00,NULL,'f53eac03-4a5e-4895-9bff-e804763cc8b3'),('198047dc-dc19-4666-8fea-1e777d3b4331',0,'Adam Warlock',NULL,NULL,'49.417184','8.678468',0,'69120 Heidelberg','Mönchhofstraße 60',NULL,0,200.00,40.00,23.00,5.00,NULL,'ab82b671-451e-4abf-9b52-036d6b53b3d2\r'),('uma4',0,'Tilmann Hellmuth',NULL,NULL,'49.4191955','8.6834687',0,'69120 Heidelberg','Moltkestraße 34',NULL,0,348.00,48.00,24.00,34.00,NULL,'dba118d7-f1cd-4ecc-a5a8-ee54e7baee4e\r'),('uma5',0,'Margit Heumann',NULL,NULL,'49.41653','8.680588',0,'69120 Heidelberg','Wilckensstraße 16',NULL,0,450.00,45.00,23.00,10.00,NULL,'bfa459ea-7e9c-410f-914f-1771fec4738b\r'),('351128b4-3e1a-441b-9ba9-698c0e504bb2',0,'Berend Scheffler','0621-1953009',NULL,'49.4143029','8.679865966',0,'69120 Heidelberg','Gerhart-Hauptmannstra?e 15',NULL,0,555.00,74.00,24.00,34.00,NULL,'9cb29e42-bcd3-4031-b1d9-6435f1305170\r'),('35bdac06-740a-4734-bd42-6a3a94996212',0,'Helge Reinhard',NULL,NULL,'49.4140159','8.6845536',0,'69120 Heidelberg','Ladenburgerstra?e 80',NULL,0,687.00,114.00,84.00,24.00,NULL,'026c6f1b-eed4-420d-b66e-f6d389483d85\r'),('37a96e73-345a-49c7-a064-a996f99d31ab',0,'Wanja Adorf',NULL,NULL,'49.41253355','8.6790184',0,'69120 Heidelberg','Posseltstra?e 9',NULL,0,248.00,14.00,27.00,78.00,NULL,'da7b7feb-9551-40d5-8205-15d62fefeec7\r'),('3843e2e1-d99f-4376-8bbb-08f257509a34',0,'Ruprecht Slesinger',NULL,NULL,'49.41408215','8.683851217',0,'69120 Heidelberg','Ladenburgerstra?e 88',NULL,0,333.00,14.00,75.00,24.00,NULL,'5209cb85-f349-4763-9fe1-35c301b48840\r'),('dummy1',0,'Tilmann Schauerte',NULL,NULL,'49.41382645','8.683616031',0,'69120 Heidelberg','Ladenburgerstra?e 91',NULL,0,4444.00,345.00,47.00,17.00,NULL,'09d06f5e-bfb1-433f-9671-708cb0d3d62c\r'),('441fb071-7fe2-4a4b-9ad6-57127aa5a063',0,'Tony Stark','4.92E+11','Iron Man','49.42027','8.684518',0,'69120 Heidelberg','Keplerstra?e 87','MCU',0,45.00,34.00,23.00,78.00,NULL,'bdd5c493-2170-4959-8531-c92ed4a5acd6\r'),('uma8',0,'Baron Wolfgang von Strucker',NULL,NULL,'49.417358','8.679864',0,'69120 Heidelberg','Moenchhofstrasse 48',NULL,0,50.00,24.00,4.00,2.00,NULL,'d03448c6-ceee-4c95-b46a-1958a051d171'),('49477c14-b25b-4b20-8fd4-4433654b19b7',0,'Dr. Doom',NULL,NULL,'49.418438','8.68304',0,'69120 Heidelberg','Seitzstrasse 1',NULL,0,355.00,34.00,12.00,65.00,NULL,'dc6bf333-b85a-477b-bd39-73381553a65f\r'),('4d8e1933-8a24-43ca-a41d-9e2ad476e1c2',0,'Wolfram Eichler',NULL,NULL,'49.41265645','8.682656594',0,'69120 Heidelberg','Uferstrasse 64a',NULL,0,789.00,45.00,24.00,37.00,NULL,'65b09fef-af7c-4768-af4b-bf848adf19cb\r'),('uma6',0,'Berndt Bachmayer',NULL,NULL,'49.4180148','8.6797599',0,'69120 Heidelberg','Seitzstrasse 12',NULL,0,355.00,34.00,12.00,65.00,NULL,'3f408e15-9a24-4151-87b8-9311aa99e001\r'),('uma7',0,'Theodor Schwegler',NULL,NULL,'49.4193935','8.684680816',0,'69120 Heidelberg','Moltkestrasse 22',NULL,0,1.00,1.00,1.00,1.00,NULL,'e5fa7962-037e-4a7f-a636-f266ec8b64c5\r'),('61aad1d6-ca30-40e2-96cf-9b36e2a1c5dc',0,'Franziska Lichtenberger','4.92E+11',NULL,'49.4126989','8.6784738',0,'69120 Heidelberg','Jahnstrasse 5A',NULL,0,578.00,34.00,17.00,39.00,NULL,'560a3cc4-43d7-4629-9a0d-0af8d68f4e86\r'),('6ae59be0-b622-4567-8e39-25b3b3462ac4',0,'Trude Krieger','4.92E+11',NULL,'49.4125365','8.67874315',0,'69120 Heidelberg','Jahnstrasse 23',NULL,0,148.00,24.00,27.00,78.00,NULL,'f19a9dce-ea2b-4506-8658-e4eab27ecb29\r'),('6bdf58b8-8000-414c-9f4a-c827c9c0431b',0,'Monica Juergens','4.92E+11',NULL,'49.4139521','8.6823604',0,'69120 Heidelberg','Jahnstrasse 8',NULL,0,478.00,15.00,48.00,34.00,NULL,'ef39dbc0-de3d-4351-81cf-ca52cb64d4c9\r'),('6c776159-df44-49d9-bdac-d66282f51a58',0,'Adam Warlock',NULL,NULL,'49.417184','8.678468',0,'69120 Heidelberg','Moenchhofstrasse 60',NULL,0,200.00,40.00,23.00,5.00,NULL,'d8e1ea0d-92e6-4278-9cb1-69c787e3755a\r'),('76e0fd17-4aca-41a6-b806-58e21bf94b26',0,'Graf Dracula',NULL,NULL,'49.419126','8.684828',0,'69120 Heidelberg','Keplerstrasse 81',NULL,0,50.00,23.00,43.00,56.00,NULL,'7665ab18-cf29-4eb2-977b-9c2d74a74126\r'),('77134d4c-473c-4345-97a8-0ac1d558b7c7',0,'Marwin Nadelmann','4.92E+11',NULL,'49.41246505','8.681089089',0,'69120 Heidelberg','Posseltstrasse 1',NULL,0,147.00,87.00,25.00,41.00,NULL,'26cf8949-4ddf-424b-afda-867ecd444efc\r'),('7c7a06a1-71a3-48d0-a120-64715260ed02',0,'Mara Henschel','4.92E+11',NULL,'49.4141939','8.68156415',0,'69120 Heidelberg','Wielandstraße 33',NULL,0,789.00,24.00,37.00,95.00,NULL,'ee286990-927c-43fa-8e3e-c26e0b545c97\r'),('7da644d1-6e33-4f5f-a80c-81b23f5b6207',0,'Wendelin Goldenberg','4.92E+11',NULL,'49.4126491','8.6812778',0,'69120 Heidelberg','Posseltstrasse 6A',NULL,0,148.00,57.00,55.00,18.00,NULL,'89a8eec9-6c13-4523-9e17-e27ad41130c4\r'),('uma9',0,'Herbert Schwender',NULL,NULL,'49.416681','8.680098',0,'69120 Heidelberg','Wilckensstrasse 23',NULL,0,250.00,20.00,35.00,40.00,NULL,'d350bef3-fb31-4ecc-8828-40e61179fcbc\r'),('uma10',0,'Augustin Unger',NULL,NULL,'49.41864405','8.681118612',0,'69120 Heidelberg','Wielandstraße 33',NULL,0,120.00,15.00,24.00,28.00,NULL,'46655003-e41c-40c9-a93a-1846352c312c\r'),('uma11',0,'Willi Beck',NULL,NULL,'49.4169944','8.6799905',0,'69120 Heidelberg','Moechhofstrasse 51',NULL,0,800.00,80.00,15.00,60.00,NULL,'56a010fe-4322-41db-b2ec-93bac9348c0f\r'),('uma12',0,'Woldemar Schuster',NULL,NULL,'49.41684','8.68171',0,'69120 Heidelberg','Wielandstraße 33',NULL,0,578.00,23.00,24.00,48.00,NULL,'710b78a6-6cb0-477b-8012-a7df089adeb8\r'),('uma13',0,'Nora Fleming','4.92E+11','','49.4149632','8.6836662',0,'69120 Heidelberg','Quinckestrasse 115',NULL,0,180.00,18.00,34.00,27.00,NULL,'19e7e8cb-340d-4270-8fe5-56db12f8aa07\r'),('uma14',0,'Dr. Xaver Lafrenz',NULL,NULL,'49.41829465','8.680817028',0,'69120 Heidelberg','Seitzstrasse 14',NULL,0,456.00,24.00,57.00,30.00,NULL,'52bfa087-101f-4c3a-a3fd-9fc5b749bc27\r'),('uma15',0,'Dr. rer. nat Elise Hauser',NULL,NULL,'49.4193774','8.67876385',0,'69120 Heidelberg','Blumenthalstrasse 54',NULL,0,124.00,27.00,45.00,67.00,NULL,'7e7d0a66-5182-4f90-a21c-ad911d3d0877'),('c7db74b4-e544-4197-9b53-2724e99342f3',0,'Silvia Mengelberg',NULL,NULL,'49.4150699','8.68385155',0,'69120 Heidelberg','Happelstrasse 18',NULL,0,347.00,17.00,28.00,24.00,NULL,'a48ac94f-fc68-4f04-a644-1666dce73bb6\r'),('c923d6f5-d6fe-4cd6-b889-df33d550ceed',0,'Wilhelmine Goebel',NULL,NULL,'49.414761','8.683343793',0,'69120 Heidelberg','Quinckestrasse 23',NULL,0,478.00,54.00,27.00,14.00,NULL,'1ee5a671-180b-40ed-8adf-bc9a84596d86\r'),('c9425184-461e-4d7b-8e87-07e838e8ce3f',0,'Ant-Man',NULL,NULL,'49.418972','8.683818',0,'69120 Heidelberg','Moltkestrasse 39',NULL,0,1.00,1.00,1.00,1.00,NULL,'00713c02-8d12-4fd0-9fc4-327f9ea4d187\r'),('d3f03418-193a-4348-99b0-a9d9bb071b09',0,'Dr. Elke Kuehne',NULL,NULL,'49.41425195','8.68346553',0,'69120 Heidelberg','Quinckestrasse 18',NULL,0,578.00,14.00,27.00,24.00,NULL,'deb8a7ce-9a77-4089-a6a4-aa5c1a7fbb3f\r'),('d5e8e9c5-20a4-493c-b7af-a8eb5ec2410b',0,'Gertrudis Boettger',NULL,NULL,'49.41367825','8.681341032',0,'69120 Heidelberg','Wielandstraße 33',NULL,0,178.00,34.00,21.00,78.00,NULL,'89d9b1ff-f804-4441-bd53-b266a82c75db\r'),('uma16',0,'Laurin Boeckmann',NULL,NULL,'49.419126','8.684828',0,'69120 Heidelberg','Keplerstrasse 81',NULL,0,50.00,23.00,43.00,56.00,NULL,'3f5d7ce4-2522-48cd-b4c6-79926ebb8faf\r'),('uma17',0,'Kim Liebermann','4.92E+11','Iron Man','49.42027','8.684518',0,'69120 Heidelberg','Keplerstrasse 87','MCU',0,45.00,34.00,23.00,78.00,NULL,'bc53f866-e0ba-4a38-876d-2a4246531f9c\r'),('uma18',0,'Wibke Boehnisch',NULL,NULL,'49.4159547','8.681723266',0,'69120 Heidelberg','Wielandstraße 33',NULL,0,356.00,56.00,25.00,30.00,NULL,'781021da-3325-4f13-bb81-b25bc80d6ae4\r'),('eb8650dd-bc9d-407a-9cd0-e4632ef0bbbf',0,'Helga Pichler',NULL,NULL,'49.4147477','8.684340198',0,'69120 Heidelberg','Happelstrasse 11',NULL,0,247.00,39.00,17.00,17.00,NULL,'3f2edbc6-af41-4a68-9853-72020a430ad0\r'),('ebe594e3-456e-45b6-b21e-d8aa986627e1',0,'Olaf Bechtel','4.92E+11',NULL,'49.41519805','8.676870241',0,'69120 Heidelberg','Berliner Strasse 14',NULL,0,748.00,54.00,21.00,19.00,NULL,'b525ddcf-a2bd-420b-864d-8bc5c6ced2fb\r'),('uma19',0,'Hannelore Dellinger',NULL,NULL,'49.41560375','8.681146317',0,'69120 Heidelberg','Schroederstrasse 93',NULL,0,478.00,78.00,20.00,15.00,NULL,'f1474a19-2f5f-460f-90b2-b7a9bf9c5be6\r'),('uma20',0,'Tristan Kohnstamm',NULL,NULL,'49.4191549','8.680540387',0,'69120 Heidelberg','Im Gabelacker 4',NULL,0,450.00,23.00,48.00,62.00,NULL,'0e499fa3-a638-4feb-b51e-10d5fe1b3155\r'),('f8efa930-f424-4154-969d-8e8fdc26893d',0,'Karsten Lindwurm','0621-8471933',NULL,'49.4144812','8.6787531',0,'69120 Heidelberg','Gerhart-Hauptmannstrasse 32',NULL,0,547.00,51.00,27.00,51.00,NULL,'66263903-8621-4a0c-917a-251a7f7fe43f\r'),('uma21',0,'Wilhelmina Strauch',NULL,NULL,'49.4193774','8.67876385',0,'69120 Heidelberg','Wilckensstrasse 41',NULL,0,248.00,26.00,24.00,57.00,NULL,'f5bea034-7a05-4b0a-b986-31499173ccf0\r'),('fbc7dfa1-3c4f-4e20-8001-d0f62e5b442b',0,'Patricia Hohenstein',NULL,NULL,'49.4134017','8.681585',0,'69120 Heidelberg','Jahnstrasse 9',NULL,0,148.00,34.00,24.00,17.00,NULL,'f9ddf887-9dc8-42ae-a672-b803ec318fa0\r'),('fcc06b00-4f61-47cf-a7f7-9cb95b4a2287',0,'Dr. Ruediger Preiszner','4.92E+11',NULL,'49.414492','8.684591544',0,'69120 Heidelberg','Wilhelm-Blumstrasse 5',NULL,0,147.00,57.00,51.00,10.00,NULL,'c363eab8-174e-4be3-8e53-106c04e0f17c\r');
/*!40000 ALTER TABLE `parcel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `parcel_old`
--

DROP TABLE IF EXISTS `parcel_old`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `parcel_old` (
  `id` varchar(100) NOT NULL,
  `state` int(11) NOT NULL,
  `name_of_recipient` varchar(200) NOT NULL,
  `phone_number` varchar(100) DEFAULT NULL,
  `additional_recipient_information` varchar(200) DEFAULT NULL,
  `latitude` varchar(100) NOT NULL,
  `longitude` varchar(100) NOT NULL,
  `address` varchar(200) NOT NULL,
  `city` varchar(200) NOT NULL,
  `additional_address_information` varchar(200) DEFAULT NULL,
  `weight` int(11) NOT NULL,
  `width` int(11) NOT NULL,
  `height` int(11) NOT NULL,
  `length` int(11) NOT NULL,
  `verification_token` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parcel_old`
--

LOCK TABLES `parcel_old` WRITE;
/*!40000 ALTER TABLE `parcel_old` DISABLE KEYS */;
INSERT INTO `parcel_old` VALUES ('022503f5-df23-40a5-9275-48666ab2564d',0,'Heike Windisch','+491728477740',NULL,'49.4155739','8.67986838465678','Schröderstraße 101','69120 Heidelberg',NULL,148,10,15,20,'d5760f5c-126e-4463-8ea7-0c384db0a0a6'),('03043f0f-739f-423e-9ed4-99394d8d6506',0,'Tillmann Kestenbaum',NULL,NULL,'49.4138959','8.684764','Wilhelm-Blumstraße 12','69120 Heidelberg',NULL,74,34,21,14,'2d22273b-1895-4f64-b193-a8f0164d27ee'),('0cea96bd-e725-402b-b094-ab594620be28',0,'Matthias Krehl',NULL,NULL,'49.41345865','8.68315567675452','Quinckestraße 10','69120 Heidelberg',NULL,1478,37,84,21,'75c5c7e7-b84a-4e5c-864f-ab11cbb971ed'),('15d4ffd9-2b0c-4177-8082-0cc33ccfd99a',0,'Heinz Schirmer',NULL,NULL,'49.41794','8.68166','Wielandtstraße 33','69120 Heidelberg',NULL,350,20,40,50,'03a2adbb-688b-40d0-82fb-61259d708051'),('185eb79f-2e05-448f-b6b4-20758cdf3bb1',0,'Eggert Schöll',NULL,NULL,'49.4133053','8.68274818784194','Quinckestraße 9 ','69120 Heidelberg',NULL,478,64,34,27,'8f3f596e-9d5d-40d5-93ed-2d27d8ec704c'),('197bf760-cbce-4b72-a89b-c3871647bd35',1,'Stefan Schaber','01726-355045','2.Stock ','49.417184','8.678468','Mönchhofstraße 60','69120 Heidelberg',NULL,200,40,23,5,'79980d6f-bf27-444c-815f-2fc4a29baf1e'),('198047dc-dc19-4666-8fea-1e777d3b4331',0,'Adam Warlock',NULL,NULL,'49.417184','8.678468','Mönchhofstraße 60','69120 Heidelberg',NULL,200,40,23,5,'ab82b671-451e-4abf-9b52-036d6b53b3d2'),('1bd7092b-8423-4503-9079-4ded48e95ade',0,'Tilmann Hellmuth',NULL,NULL,'49.4191955','8.6834687','Moltkestraße 34 ','69120 Heidelberg',NULL,348,48,24,34,'dba118d7-f1cd-4ecc-a5a8-ee54e7baee4e'),('252b5956-1b66-453c-8896-f9a8b5a7f64e',0,'Margit Heumann',NULL,NULL,'49.416530','8.680588','Wilckensstraße 16','69120 Heidelberg',NULL,450,45,23,10,'bfa459ea-7e9c-410f-914f-1771fec4738b'),('351128b4-3e1a-441b-9ba9-698c0e504bb2',0,'Berend Scheffler','0621-1953009',NULL,'49.4143029','8.6798659657867','Gerhart-Hauptmannstraße 15','69120 Heidelberg',NULL,555,74,24,34,'9cb29e42-bcd3-4031-b1d9-6435f1305170'),('35bdac06-740a-4734-bd42-6a3a94996212',0,'Helge Reinhard',NULL,NULL,'49.4140159','8.6845536','Ladenburgerstraße 80','69120 Heidelberg',NULL,687,114,84,24,'026c6f1b-eed4-420d-b66e-f6d389483d85'),('37a96e73-345a-49c7-a064-a996f99d31ab',0,'Wanja Adorf',NULL,NULL,'49.41253355','8.6790184','Posseltstraße 9','69120 Heidelberg',NULL,248,14,27,78,'da7b7feb-9551-40d5-8205-15d62fefeec7'),('3843e2e1-d99f-4376-8bbb-08f257509a34',0,'Ruprecht Slesinger',NULL,NULL,'49.41408215','8.68385121672024','Ladenburgerstraße 88','69120 Heidelberg',NULL,333,14,75,24,'5209cb85-f349-4763-9fe1-35c301b48840'),('393c2dc0-0cd5-439c-a28d-f33ca2827bfb',0,'Tilmann Schauerte',NULL,NULL,'49.41382645','8.68361603057497','Ladenburgerstraße 91','69120 Heidelberg',NULL,4444,345,47,17,'09d06f5e-bfb1-433f-9671-708cb0d3d62c'),('441fb071-7fe2-4a4b-9ad6-57127aa5a063',0,'Tony Stark','+491728477740','Iron Man','49.420270','8.684518','Keplerstraße 87','69120 Heidelberg','MCU',45,34,23,78,'bdd5c493-2170-4959-8531-c92ed4a5acd6'),('47472ac8-a49a-4ddf-85e3-f6f66ee7cbf6',0,'Baron Wolfgang von Strucker',NULL,NULL,'49.417358','8.679864','Mönchhofstraße 48','69120 Heidelberg',NULL,50,24,4,2,'6e67786e-c39e-4237-acf5-bcb88a6eb56b'),('49477c14-b25b-4b20-8fd4-4433654b19b7',0,'Dr. Doom',NULL,NULL,'49.418438','8.683040','Seitzstraße 1','69120 Heidelberg',NULL,355,34,12,65,'dc6bf333-b85a-477b-bd39-73381553a65f'),('4d8e1933-8a24-43ca-a41d-9e2ad476e1c2',0,'Wolfram Eichler',NULL,NULL,'49.41265645','8.6826565942110','Uferstraße 64a','69120 Heidelberg',NULL,789,45,24,37,'65b09fef-af7c-4768-af4b-bf848adf19cb'),('4f2c0d83-cbaf-414b-b58a-108579a9e313',0,'Berndt Bachmayer',NULL,NULL,'49.4180148','8.6797599','Seitzstraße 12','69120 Heidelberg',NULL,355,34,12,65,'3f408e15-9a24-4151-87b8-9311aa99e001'),('55fa163c-b4dc-48da-b0a9-28ab51a16cb2',0,'Theodor Schwegler',NULL,NULL,'49.4193935','8.68468081585366','Moltkestraße 22','69120 Heidelberg',NULL,1,1,1,1,'e5fa7962-037e-4a7f-a636-f266ec8b64c5'),('61aad1d6-ca30-40e2-96cf-9b36e2a1c5dc',0,'Franziska Lichtenberger','+491728477740',NULL,'49.4126989','8.6784738','Jahnstraße 5A','69120 Heidelberg',NULL,578,34,17,39,'560a3cc4-43d7-4629-9a0d-0af8d68f4e86'),('6ae59be0-b622-4567-8e39-25b3b3462ac4',0,'Trude Krieger','+491728477740',NULL,'49.4125365','8.67874315','Jahnstraße 23','69120 Heidelberg',NULL,148,24,27,78,'f19a9dce-ea2b-4506-8658-e4eab27ecb29'),('6bdf58b8-8000-414c-9f4a-c827c9c0431b',0,'Monica Jürgens','+491728477740',NULL,'49.4139521','8.6823604','Jahnstraße 8','69120 Heidelberg',NULL,478,15,48,34,'ef39dbc0-de3d-4351-81cf-ca52cb64d4c9'),('6c776159-df44-49d9-bdac-d66282f51a58',0,'Adam Warlock',NULL,NULL,'49.417184','8.678468','Mönchhofstraße 60','69120 Heidelberg',NULL,200,40,23,5,'d8e1ea0d-92e6-4278-9cb1-69c787e3755a'),('76e0fd17-4aca-41a6-b806-58e21bf94b26',0,'Graf Dracula',NULL,NULL,'49.419126','8.684828','Keplerstraße 81','69120 Heidelberg',NULL,50,23,43,56,'7665ab18-cf29-4eb2-977b-9c2d74a74126'),('77134d4c-473c-4345-97a8-0ac1d558b7c7',0,'Marwin Nadelmann','+491728477740',NULL,'49.41246505','8.68108908936064','Posseltstraße 1','69120 Heidelberg',NULL,147,87,25,41,'26cf8949-4ddf-424b-afda-867ecd444efc'),('7c7a06a1-71a3-48d0-a120-64715260ed02',0,'Mara Henschel','+491728477740',NULL,'49.4141939','8.68156415','Wielandtstraße 6','69120 Heidelberg',NULL,789,24,37,95,'ee286990-927c-43fa-8e3e-c26e0b545c97'),('7da644d1-6e33-4f5f-a80c-81b23f5b6207',0,'Wendelin Goldenberg','+491728477740',NULL,'49.4126491','8.6812778','Posseltstraße 6A','69120 Heidelberg',NULL,148,57,55,18,'89a8eec9-6c13-4523-9e17-e27ad41130c4'),('7e9c5f9d-4f44-4f2a-bec5-282bd5ae4d59',1,'Dr. Wolfgang von Strucker','+1728477740',NULL,'49.417358','8.679864','Mönchhofstraße 48','69120 Heidelberg',NULL,50,24,4,2,'6d232d34-a021-4a23-8b2a-9184c33109a1'),('817e7994-8443-40e9-9dc2-cf62600376ea',0,'Herbert Schwender',NULL,NULL,'49.416681','8.680098','Wilckensstraße 23','69120 Heidelberg',NULL,250,20,35,40,'d350bef3-fb31-4ecc-8828-40e61179fcbc'),('89f8bc87-9f25-462e-9775-298745c34cc1',0,'Augustin Unger',NULL,NULL,'49.41864405','8.68111861241593','Wielandtstraße 43','69120 Heidelberg',NULL,120,15,24,28,'46655003-e41c-40c9-a93a-1846352c312c'),('93bf5071-994e-4359-830f-6e24cafafcb1',1,'Willi Beck',NULL,NULL,'49.4169944','8.6799905','Möchhofstraße 51','69120 Heidelberg',NULL,800,80,15,60,'56a010fe-4322-41db-b2ec-93bac9348c0f'),('96b63756-1e53-49ce-9ba0-e3d531365f8e',0,'Woldemar Schuster',NULL,NULL,'49.41684','8.68171','Wielandtstraße 29','69120 Heidelberg',NULL,578,23,24,48,'710b78a6-6cb0-477b-8012-a7df089adeb8'),('a71d334f-e237-489d-9b08-c9089e7e6797',0,'Nora Fleming','+491728477740','','49.4149632','8.6836662','Quinckestraße 115','69120 Heidelberg',NULL,180,18,34,27,'19e7e8cb-340d-4270-8fe5-56db12f8aa07'),('aea751ad-eae7-4e24-8e3d-ea10ca5714ee',0,'Dr. Xaver Lafrenz',NULL,NULL,'49.41829465','8.68081702848837','Seitzstraße 14','69120 Heidelberg',NULL,456,24,57,30,'52bfa087-101f-4c3a-a3fd-9fc5b749bc27'),('bd544217-4ec3-4636-9297-2d0908e3bc81',0,'Dr. rer. nat Elise Hauser',NULL,NULL,'49.4193774','8.67876385','Blumenthalstraße 54','69120 Heidelberg',NULL,124,27,45,67,'12ee61c1-795e-44c1-aec7-f10c54c6fa37'),('c7db74b4-e544-4197-9b53-2724e99342f3',0,'Silvia Mengelberg',NULL,NULL,'49.4150699','8.68385155','Happelstraße 18','69120 Heidelberg',NULL,347,17,28,24,'a48ac94f-fc68-4f04-a644-1666dce73bb6'),('c923d6f5-d6fe-4cd6-b889-df33d550ceed',0,'Wilhelmine Goebel',NULL,NULL,'49.414761','8.68334379288703','Quinckestraße 23','69120 Heidelberg',NULL,478,54,27,14,'1ee5a671-180b-40ed-8adf-bc9a84596d86'),('c9425184-461e-4d7b-8e87-07e838e8ce3f',0,'Ant-Man',NULL,NULL,'49.418972','8.683818','Moltkestraße 39','69120 Heidelberg',NULL,1,1,1,1,'00713c02-8d12-4fd0-9fc4-327f9ea4d187'),('d3f03418-193a-4348-99b0-a9d9bb071b09',0,'Dr. Elke Kühne',NULL,NULL,'49.41425195','8.68346552954545','Quinckestraße 18','69120 Heidelberg',NULL,578,14,27,24,'deb8a7ce-9a77-4089-a6a4-aa5c1a7fbb3f'),('d54ae8f1-c332-45f0-bcdb-a81427a7fd62',0,'Wibke Wachtler','0621-3624332',NULL,'','','Gerhart-Hauptmannstraße 18','69120 Heidelberg',NULL,974,14,37,58,'ebba5b11-d453-47f7-a5a0-ede20431e0b1'),('d5e8e9c5-20a4-493c-b7af-a8eb5ec2410b',0,'Gertrudis Böttger',NULL,NULL,'49.41367825','8.68134103236079','Wielandtstraße 2','69120 Heidelberg',NULL,178,34,21,78,'89d9b1ff-f804-4441-bd53-b266a82c75db'),('d6571f57-da6b-4d7f-973e-4512c853ed40',0,'Laurin Boeckmann',NULL,NULL,'49.419126','8.684828','Keplerstraße 81','69120 Heidelberg',NULL,50,23,43,56,'3f5d7ce4-2522-48cd-b4c6-79926ebb8faf'),('dae4529e-2c4b-4ae3-8f31-8687d67064fa',0,'Kim Liebermann','+491728477740','Iron Man','49.420270','8.684518','Keplerstraße 87','69120 Heidelberg','MCU',45,34,23,78,'bc53f866-e0ba-4a38-876d-2a4246531f9c'),('e3dfa685-0654-42ed-9206-4fb43f2049af',0,'Wibke Böhnisch',NULL,NULL,'49.4159547','8.68172326649792','Wielandtstraße 20','69120 Heidelberg',NULL,356,56,25,30,'781021da-3325-4f13-bb81-b25bc80d6ae4'),('eb8650dd-bc9d-407a-9cd0-e4632ef0bbbf',0,'Helga Pichler',NULL,NULL,'49.4147477','8.68434019829205','Happelstraße 11','69120 Heidelberg',NULL,247,39,17,17,'3f2edbc6-af41-4a68-9853-72020a430ad0'),('ebe594e3-456e-45b6-b21e-d8aa986627e1',0,'Olaf Bechtel','+491728477740',NULL,'49.41519805','8.67687024088837','Berliner Straße 14','69120 Heidelberg',NULL,748,54,21,19,'b525ddcf-a2bd-420b-864d-8bc5c6ced2fb'),('f156daa0-88f7-448b-b75f-e5f8435a602b',0,'Hannelore Dellinger',NULL,NULL,'49.41560375','8.68114631682606','Schröderstraße 93','69120 Heidelberg',NULL,478,78,20,15,'f1474a19-2f5f-460f-90b2-b7a9bf9c5be6'),('f33230de-218b-4bc6-b8ef-48a846e61496',0,'Tristan Kohnstamm',NULL,NULL,'49.4191549','8.68054038718913','Im Gabelacker 4','69120 Heidelberg',NULL,450,23,48,62,'0e499fa3-a638-4feb-b51e-10d5fe1b3155'),('f8efa930-f424-4154-969d-8e8fdc26893d',0,'Karsten Lindwurm','0621-8471933',NULL,'49.4144812','8.6787531','Gerhart-Hauptmannstraße 32','69120 Heidelberg',NULL,547,51,27,51,'66263903-8621-4a0c-917a-251a7f7fe43f'),('fa50f027-c807-4470-aa13-7ee7b4d25485',0,'Wilhelmina Strauch',NULL,NULL,'49.4193774','8.67876385','Wilckensstraße 41','69120 Heidelberg',NULL,248,26,24,57,'f5bea034-7a05-4b0a-b986-31499173ccf0'),('fbc7dfa1-3c4f-4e20-8001-d0f62e5b442b',0,'Patricia Hohenstein',NULL,NULL,'49.4134017','8.681585','Jahnstraße 9','69120 Heidelberg',NULL,148,34,24,17,'f9ddf887-9dc8-42ae-a672-b803ec318fa0'),('fcc06b00-4f61-47cf-a7f7-9cb95b4a2287',0,'Dr. Rüdiger Preiszner','+491728477740',NULL,'49.414492','8.68459154419707','Wilhelm-Blumstraße 5','69120 Heidelberg',NULL,147,57,51,10,'c363eab8-174e-4be3-8e53-106c04e0f17c');
/*!40000 ALTER TABLE `parcel_old` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `parkingAreas`
--

DROP TABLE IF EXISTS `parkingAreas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `parkingAreas` (
  `id` varchar(100) NOT NULL,
  `address` varchar(200) DEFAULT NULL,
  `city` varchar(200) DEFAULT NULL,
  `latitude` varchar(100) NOT NULL,
  `longitude` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `parkingAreas`
--

LOCK TABLES `parkingAreas` WRITE;
/*!40000 ALTER TABLE `parkingAreas` DISABLE KEYS */;
INSERT INTO `parkingAreas` VALUES ('bit_stop_1','Berliner Straße 41','69120 Heidelberg','49.417.843','8.675.079'),('bit_stop_2','Berliner Straße 43','69120 Heidelberg','49.418.622','8.675.089'),('hd_0','','','49.41202114552766','8.680437667527157'),('hd_1','','','49.41674791042533','8.681695030748935'),('hd_10','','','49.41723582179759','8.680596037475366'),('hd_11','','','49.416990268249265','8.678328945006244'),('hd_12','','','49.4137178490854','8.682064526106533'),('hd_13','','','49.41387821660203','8.682651246979031'),('hd_14','','','49.4208511682358','8.685533131874228'),('hd_15','','','49.420230539093495','8.681870090918558'),('hd_16','','','49.4126917633771','8.679742877465975'),('hd_17','','','49.412754342330004','8.681083167803033'),('hd_18','','','49.419164046555125','8.683971003304586'),('hd_19','','','49.41932599792972','8.685531636868477'),('hd_2','','','49.41842195640231','8.682485400395251'),('hd_20','','','49.416968656734866','8.685447440017375'),('hd_21','','','49.419144747751716','8.685030693528471'),('hd_22','','','49.419754080852044','8.684914297288547'),('hd_23','','','49.415882823126594','8.683777926479362'),('hd_24','','','49.41506843271077','8.683715054746308'),('hd_25','','','49.414459058864054','8.683426484646612'),('hd_26','','','49.41348429955474','8.682935357739712'),('hd_27','','','49.412167805311356','8.680914352868124'),('hd_28','','','49.41431767704239','8.68138136204616'),('hd_29','','','49.41506117686902','8.681497194557856'),('hd_3','','','49.41778475114188','8.678357042997268'),('hd_30','','','49.41608848036344','8.681531753870635'),('hd_31','','','49.41842992687077','8.682351476423568'),('hd_32','','','49.41818891529124','8.680816126209043'),('hd_33','','','49.41664524450084','8.680339245845953'),('hd_34','','','49.41600037962678','8.68053094157239'),('hd_35','','','49.417589876102284','8.67999910893014'),('hd_36','','','49.418581427982076','8.679462861444227'),('hd_4','','','49.41873021256333','8.678939101236237'),('hd_5','','','49.418985571458165','8.680578947016183'),('hd_6','','','49.41774887847805','8.679871778500774'),('hd_7','','','49.413198938822575','8.680252968511498'),('hd_8','','','49.41736499224555','8.684126542241865'),('hd_9','','','49.41735762390579','8.685865328627585');
/*!40000 ALTER TABLE `parkingAreas` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-07-14  9:50:44
