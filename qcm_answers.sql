-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Feb 13, 2022 at 07:39 AM
-- Server version: 8.0.20
-- PHP Version: 7.4.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `qcm_answers`
--

-- --------------------------------------------------------

--
-- Table structure for table `answers`
--

CREATE TABLE `answers` (
  `id` int NOT NULL,
  `qcm_id` int NOT NULL,
  `nom_prenom` varchar(255) NOT NULL,
  `date_rep` datetime NOT NULL,
  `ip_addr` varchar(128) NOT NULL,
  `reponse` varchar(2048) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `answers`
--

INSERT INTO `answers` (`id`, `qcm_id`, `nom_prenom`, `date_rep`, `ip_addr`, `reponse`) VALUES
(1, 1, 'Mohamed Anis MANI', '2022-02-12 18:39:22', '127.0.0.1', '1A2B3B4C5D6D7C8C9D10A'),
(2, 1, 'Mohamed Anis MANI', '2022-02-13 06:27:57', '127.0.0.1', '1C2B3C4A5A6A7C8D9C10B'),
(3, 1, 'Mohamed Anis MANI', '2022-02-13 06:28:27', '127.0.0.1', '1D2D3B4D5C6A7B8A9B10A'),
(4, 1, 'Mohamed Anis MANI', '2022-02-13 07:19:10', '127.0.0.1', '1A2C3C4D5A6A7D8B9D10A'),
(5, 1, 'Abdouda MANI', '2022-02-13 07:33:33', '127.0.0.1', '1C2A3A4D5A6A7B8B9A10C'),
(6, 1, 'Mohamed Anis MANI', '2022-02-13 07:35:58', '127.0.0.1', '1A2A3C4C5B6C7D8B9D10C');

-- --------------------------------------------------------

--
-- Table structure for table `qcms`
--

CREATE TABLE `qcms` (
  `id` int NOT NULL,
  `classe` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `titre` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `description` varchar(1024) COLLATE utf8mb4_general_ci NOT NULL,
  `nbr_questions` int NOT NULL,
  `reponses` varchar(1024) COLLATE utf8mb4_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `qcms`
--

INSERT INTO `qcms` (`id`, `classe`, `titre`, `description`, `nbr_questions`, `reponses`) VALUES
(1, '2TI', 'Structures itératives', 'QCM Structures itératives', 10, '1A2A3C4C5B6C7D8B9D10C');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `answers`
--
ALTER TABLE `answers`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `qcms`
--
ALTER TABLE `qcms`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `answers`
--
ALTER TABLE `answers`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `qcms`
--
ALTER TABLE `qcms`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
