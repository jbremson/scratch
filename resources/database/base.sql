--
-- Table structure for table `Cities`
--

DROP TABLE IF EXISTS `cities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cities` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` varchar(256) NOT NULL,
  `region` varchar(256) NOT NULL,
  `creation_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Trips`
--

DROP TABLE IF EXISTS `trips`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `trips` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `origin` bigint(20) NOT NULL,
  `destination` bigint(20) NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `time` bigint(20) NOT NULL,
  `text_time` varchar(256) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Trips_fk1` (`origin`),
  KEY `Trips_fk2` (`destination`),
  CONSTRAINT `Trips_fk2` FOREIGN KEY (`destination`) REFERENCES `cities` (`id`),
  CONSTRAINT `Trips_fk1` FOREIGN KEY (`origin`) REFERENCES `cities` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;