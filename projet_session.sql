-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1
-- Généré le : mer. 24 avr. 2024 à 02:52
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
  `prix` int(200) NOT NULL,
  `images` varchar(100) NOT NULL,
  `description` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Déchargement des données de la table `events`
--

INSERT INTO `events` (`id`, `nom`, `date`, `emplacement`, `prix`, `images`, `description`) VALUES
(1, 'Festival dété de Québec', '2024-07-04', 'Plaines dAbraham', 150, 'static/images/feq.jpg', 'Le Festival dété de Québec est lévénement musical en plein air par excellence, offrant deux semaines de musique live éclectique. Des sons rock et hip-hop à la musique électronique et folk, sa programm'),
(2, 'Coachella Valley Music and Arts Festival', '2024-04-12', 'Empire Polo Club, Indio, Calif', 399, 'static/images/coachella.jpg', 'Coachella est lun des plus grands festivals de musique et darts aux États-Unis, mettant en vedette des artistes de renommée mondiale dans une variété de genres musicaux.'),
(3, 'Lollapalooza', '2024-07-31', 'Grant Park, Chicago, Illinois', 350, 'static/images/lollapalooza.jpg', 'Lollapalooza est un festival de musique emblématique qui se déroule chaque année à Chicago, offrant une expérience immersive avec des performances live, de lart visuel et des installations interactive'),
(4, 'Austin City Limits Music Festival', '2024-10-04', 'Zilker Park, Austin, Texas', 300, 'static/images/aclfest.jpg', 'ACL Festival est un festival de musique de deux week-ends qui présente une programmation diversifiée de musique live, allant du rock et du hip-hop à la musique électronique et au folk.'),
(5, 'Bonnaroo Music and Arts Festival', '2024-06-13', 'Great Stage Park, Manchester, ', 319, 'static/images/bonnaroo.jpg', 'Bonnaroo est un festival de musique emblématique du Tennessee, célèbre pour ses performances en direct, son camping communautaire et son ambiance conviviale.'),
(6, 'Electric Daisy Carnival (EDC) Las Vegas', '2024-05-17', 'Las Vegas Motor Speedway, Las ', 399, 'static/images/edclasvegas.jpg', 'EDC est lun des plus grands festivals de musique électronique au monde, offrant une expérience immersive avec des scènes thématiques, des manèges et des performances de DJs renommés.'),
(8, 'Magic Michel', '2024-06-05', 'Grand Théâtre de Québec', 120, 'static/images/MagicMichel.png', 'Rejoignez-nous pour une soirée enchantée avec Magic Michel, le maître de l\'illusion, qui vous transportera dans un univers où le possible côtoie l’impossible. Célèbre pour ses performances captivantes'),
(9, 'Steven Bibeurre', '2024-07-11', 'Le Centre Videotron', 180, 'static/images/bibeurre.jpg', 'Venez vivre une soirée mémorable avec le talentueux Steven Bibeurre ! Reconnu pour sa voix unique et ses performances dynamiques, Steven vous promet un concert électrisant qui captivera votre cœur et '),
(10, 'Max McBoots', '2024-08-21', 'Colisée Pepsi', 85, 'static/images/Maxnboots.jpg', 'Montez en selle et rejoignez Max McBoots pour une soirée exceptionnelle de musique country authentique. Avec son charme rustique et sa voix qui capture l’essence du Far West, Max vous emmènera dans un');

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
(4, 'John Doe', '514-622-5356', 'JD123@hotmail.com', '4321 4321 4321 4321'),
(5, 'test user', '514-588-8778', 'test@test.com', '5555 5555 5555 5555');

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
(1, 'Michel', 1, 'confirmé', 'Festival d\'été de Québec'),
(5, 'John Doe', 10, 'en attente', 'Coachella'),
(6, 'Michel', 2, 'en-attente', 'Festival d\'été de Québec'),
(7, 'test user', 20, 'en-attente', 'Steven Bibeurre'),
(8, 'test user', 18, 'en-attente', 'Max McBoots'),
(9, 'test user', 100, 'en-attente', 'Magic Michel');

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
(4, 'admin', 'admin', '$2b$12$UgB2HPyR8cztGOhjTiFrsuw9TlLqncZ/R.6sGWANuspEWwr40lVau', 'admin@ticketmain.com', 'admin'),
(6, 'Michel ', 'michel', '$2b$12$.oV7VfRgB7RWurAapKVE6O8k5BXbd8aY1d8KNoNbXjnVz7knlgjK6', 'michel@hotmail.com', 'client'),
(7, 'John Doe', 'JD123', '$2b$12$vOJf/LthgZ8AJEKIkja1BOfFEfOm2KlYW8/7aelN85SInK/DxHrvG', 'JD123@hotmail.com', 'client'),
(11, 'test user', 'test', '$2b$12$boB5P.9RCZVbApxQZY2ApeE3aK2dsiMl1mwBt0TKWVblED5X44Nrq', 'test@test.com', 'client');

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
  MODIFY `id` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT pour la table `paiement`
--
ALTER TABLE `paiement`
  MODIFY `id` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT pour la table `reservations`
--
ALTER TABLE `reservations`
  MODIFY `id` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT pour la table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(200) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
