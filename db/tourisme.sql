-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Aug 28, 2025 at 07:22 AM
-- Server version: 9.1.0
-- PHP Version: 8.3.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tourisme`
--
CREATE DATABASE IF NOT EXISTS `tourisme` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `tourisme`;

-- --------------------------------------------------------

--
-- Table structure for table `groupe`
--

DROP TABLE IF EXISTS `groupe`;
CREATE TABLE IF NOT EXISTS `groupe` (
  `Code` int NOT NULL AUTO_INCREMENT,
  `NomG` varchar(25) NOT NULL,
  PRIMARY KEY (`Code`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `groupe`
--

INSERT INTO `groupe` (`Code`, `NomG`) VALUES
(1, 'Sifaka'),
(2, 'Ravinala');

-- --------------------------------------------------------

--
-- Table structure for table `touriste`
--

DROP TABLE IF EXISTS `touriste`;
CREATE TABLE IF NOT EXISTS `touriste` (
  `Numero` int NOT NULL AUTO_INCREMENT,
  `Nom` varchar(25) NOT NULL,
  `CodeG` int DEFAULT NULL,
  PRIMARY KEY (`Numero`),
  KEY `FK_TOURISTE_GROUPE` (`CodeG`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `touriste`
--

INSERT INTO `touriste` (`Numero`, `Nom`, `CodeG`) VALUES
(6, 'Rakoto', 2),
(7, 'Rasoa', 1),
(8, 'Njaka', 2),
(9, 'Martial', 1);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
