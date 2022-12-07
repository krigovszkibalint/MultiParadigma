-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Gép: 127.0.0.1
-- Létrehozás ideje: 2022. Dec 07. 14:16
-- Kiszolgáló verziója: 10.4.24-MariaDB
-- PHP verzió: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Adatbázis: `multiparadigma`
--

-- --------------------------------------------------------

--
-- Tábla szerkezet ehhez a táblához `dolgozok`
--

CREATE TABLE `dolgozok` (
  `id` int(11) NOT NULL,
  `vezeteknev` varchar(64) COLLATE utf8mb4_hungarian_ci NOT NULL,
  `keresztnev` varchar(64) COLLATE utf8mb4_hungarian_ci NOT NULL,
  `eletkor` int(2) NOT NULL,
  `varos` varchar(64) COLLATE utf8mb4_hungarian_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_hungarian_ci;

--
-- A tábla adatainak kiíratása `dolgozok`
--

INSERT INTO `dolgozok` (`id`, `vezeteknev`, `keresztnev`, `eletkor`, `varos`) VALUES
(1, 'Krigovszki', 'Bálint', 24, 'Gyöngyös'),
(2, 'Teszt', 'Elek', 25, 'Eger'),
(3, 'Asd', 'Dsa', 32, 'Debrecen'),
(4, 'Hosszúvezetéknév', 'Valami', 40, 'Eger'),
(17, 'Dolgozó', 'Neve', 24, 'Budapest'),
(18, 'Másik Dolgozó', 'Neveee', 26, 'Budapest');

--
-- Indexek a kiírt táblákhoz
--

--
-- A tábla indexei `dolgozok`
--
ALTER TABLE `dolgozok`
  ADD PRIMARY KEY (`id`);

--
-- A kiírt táblák AUTO_INCREMENT értéke
--

--
-- AUTO_INCREMENT a táblához `dolgozok`
--
ALTER TABLE `dolgozok`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
