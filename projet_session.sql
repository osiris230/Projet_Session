-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : sam. 20 avr. 2024 à 01:15
-- Version du serveur : 10.4.32-MariaDB
-- Version de PHP : 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `projet_session`
--

-- --------------------------------------------------------

--
-- Structure de la table `events`
--

CREATE TABLE `events` (
  `id` int(100) NOT NULL,
  `nom` varchar(50) NOT NULL,
  `date` date NOT NULL,
  `emplacement` varchar(30) NOT NULL,
  `prix` int(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `events`
--

INSERT INTO `events` (`id`, `nom`, `date`, `emplacement`, `prix`) VALUES
(3, 'Johnny McMax', '2024-05-05', 'Stade Pepis', 130),
(5, 'Magic Michel', '2024-06-20', 'Grand Théâtre de Québec', 100),
(6, 'Steven Bibeurre', '2024-08-10', 'Le Centre Videotron', 200),
(7, 'Festival d\'été de Québec', '2024-07-04', 'Plaines d\'Abraham', 150);

-- --------------------------------------------------------

--
-- Structure de la table `paiement`
--

CREATE TABLE `paiement` (
  `id` int(30) NOT NULL,
  `nom_complet` varchar(30) NOT NULL,
  `telephone` varchar(16) NOT NULL,
  `email` varchar(40) NOT NULL,
  `carte_credit` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `paiement`
--

INSERT INTO `paiement` (`id`, `nom_complet`, `telephone`, `email`, `carte_credit`) VALUES
(1, 'Michel ', '819-155-5252', 'michel@hotmail.com', '1234 1234 1234 1234'),
(4, 'John Doe', '514-622-5356', 'JD123@hotmail.com', '4321 4321 4321 4321');

-- --------------------------------------------------------

--
-- Structure de la table `reservations`
--

CREATE TABLE `reservations` (
  `id` int(200) NOT NULL,
  `nom` varchar(70) NOT NULL,
  `place` int(3) NOT NULL,
  `status` varchar(20) NOT NULL,
  `event` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `reservations`
--

INSERT INTO `reservations` (`id`, `nom`, `place`, `status`, `event`) VALUES
(1, 'Michel', 1, 'confirmé', 'Johnny Rupy'),
(5, 'John Doe', 10, 'en-attente', 'Festival d\'été de Québec');

-- --------------------------------------------------------

--
-- Structure de la table `users`
--

CREATE TABLE `users` (
  `id` int(200) NOT NULL,
  `nom_complet` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(60) NOT NULL,
  `email` varchar(30) NOT NULL,
  `status` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `users`
--

INSERT INTO `users` (`id`, `nom_complet`, `username`, `password`, `email`, `status`) VALUES
(3, 'Bon John Bovie', 'bjb', '123', 'jbj@email.com', 'admin'),
(4, 'admin', 'admin', '$2b$12$UgB2HPyR8cztGOhjTiFrsuw9TlLqncZ/R.6sGWANuspEWwr40lVau', 'admin@ticketmain.com', 'admin'),
(6, 'Michel ', 'michel', '$2b$12$.oV7VfRgB7RWurAapKVE6O8k5BXbd8aY1d8KNoNbXjnVz7knlgjK6', 'michel@hotmail.com', 'client'),
(7, 'John Doe', 'JD123', '$2b$12$vOJf/LthgZ8AJEKIkja1BOfFEfOm2KlYW8/7aelN85SInK/DxHrvG', 'JD123@hotmail.com', 'client');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `events`
--
ALTER TABLE `events`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `paiement`
--
ALTER TABLE `paiement`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `carte_credit` (`carte_credit`);

--
-- Index pour la table `reservations`
--
ALTER TABLE `reservations`
  ADD PRIMARY KEY (`id`);

--
-- Index pour la table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `events`
--
ALTER TABLE `events`
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT pour la table `paiement`
--
ALTER TABLE `paiement`
  MODIFY `id` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT pour la table `reservations`
--
ALTER TABLE `reservations`
  MODIFY `id` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT pour la table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
