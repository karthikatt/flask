-- Adminer 4.6.2 MySQL dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

DROP TABLE IF EXISTS `accessControl`;
CREATE TABLE `accessControl` (
  `id` int(11) NOT NULL,
  `acesssID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `auditInfo`;
CREATE TABLE `auditInfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `facultyId` int(11) NOT NULL,
  `processTime` timestamp NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `loginInfo`;
CREATE TABLE `loginInfo` (
  `userName` text NOT NULL,
  `password` text NOT NULL,
  `logInTime` timestamp NOT NULL ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `students`;
CREATE TABLE `students` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(30) NOT NULL,
  `branch` varchar(10) NOT NULL,
  `mode` text NOT NULL,
  `mobileNo` varchar(20) NOT NULL,
  `email` text NOT NULL,
  `currentAdd` text NOT NULL,
  `parmanentAdd` text NOT NULL,
  `fatherName` varchar(30) NOT NULL,
  `fatherMobileNo` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

ALTER TABLE students AUTO_INCREMENT=2020001;

-- 2020-07-21 15:53:29
