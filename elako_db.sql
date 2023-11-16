-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3308
-- Generation Time: Nov 15, 2023 at 10:04 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `elako_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `comments_tbl`
--

CREATE TABLE `comments_tbl` (
  `comments_id` int(11) NOT NULL,
  `commentor_name` varchar(30) NOT NULL,
  `commentor_feedback` varchar(400) NOT NULL,
  `position` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `comments_tbl`
--

INSERT INTO `comments_tbl` (`comments_id`, `commentor_name`, `commentor_feedback`, `position`) VALUES
(1, 'Henry M. Daniel', 'I am incredibly impressed with the quality of the product. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. This has exceeded my expectations!', 'Satisfied Customer'),
(2, 'Michael R. Brown', 'Exceptional support and quick response times! Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Thank you for making my experience so seamless.', 'Grateful Client'),
(3, 'Sarah K. Johnson', 'Outstanding service! Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. The team went above and beyond to meet my needs.', 'Happy User');

-- --------------------------------------------------------

--
-- Table structure for table `contactus_tbl`
--

CREATE TABLE `contactus_tbl` (
  `contactus_id` int(10) NOT NULL,
  `email_address` varchar(40) NOT NULL,
  `office_address` varchar(40) NOT NULL,
  `phone_number` varchar(40) NOT NULL,
  `google_map` varchar(1500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `contactus_tbl`
--

INSERT INTO `contactus_tbl` (`contactus_id`, `email_address`, `office_address`, `phone_number`, `google_map`) VALUES
(1, 'juandelacruz@gmail.com ', 'La Trinidad, Benguet', '+0123-456789', '<iframe src=\"https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d9334.271551495209!2d-73.97198251485975!3d40.668170674982946!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c25b0456b5a2e7%3A0x68bdf865dda0b669!2sBrooklyn%20Botanic%20Garden%20Shop!5e0!3m2!1sen!2sbd!4v1590597267201!5m2!1sen!2sbd\" width=\"100%\" height=\"100%\" frameborder=\"0\" allowfullscreen=\"\" aria-hidden=\"false\" tabindex=\"0\"></iframe>');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_admin_users`
--

CREATE TABLE `tbl_admin_users` (
  `user_id` varchar(20) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `role` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_admin_users`
--

INSERT INTO `tbl_admin_users` (`user_id`, `username`, `password`, `email`, `role`) VALUES
('ADMIN-65851567', 'admin@gmail.com', 'admin', 'admin@gmail.com', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `tbl_bidding`
--

CREATE TABLE `tbl_bidding` (
  `bidding_id` varchar(20) NOT NULL,
  `product_id` varchar(20) NOT NULL,
  `minimum_bid` int(255) NOT NULL,
  `bidding_start` datetime NOT NULL,
  `bidding_end` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_farmer_users`
--

CREATE TABLE `tbl_farmer_users` (
  `user_id` varchar(20) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `full_name` varchar(255) NOT NULL,
  `gender` enum('male','female') NOT NULL,
  `phone_number` varchar(20) DEFAULT NULL,
  `alternative_phone` varchar(20) DEFAULT NULL,
  `address` text DEFAULT NULL,
  `date_of_birth` date NOT NULL,
  `profile_picture` varchar(255) DEFAULT NULL,
  `role` varchar(50) NOT NULL,
  `facebook` varchar(100) DEFAULT NULL,
  `twitter` varchar(100) DEFAULT NULL,
  `instagram` varchar(100) DEFAULT NULL,
  `status` enum('active','inactive') DEFAULT 'active',
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_farmer_users`
--

INSERT INTO `tbl_farmer_users` (`user_id`, `username`, `password`, `email`, `full_name`, `gender`, `phone_number`, `alternative_phone`, `address`, `date_of_birth`, `profile_picture`, `role`, `facebook`, `twitter`, `instagram`, `status`, `created_at`, `updated_at`) VALUES
('FARMER-69146423', 'melanieclara@gmail.com', '7210109c46', 'melanieclara@gmail.com', 'Melanie Clara', 'male', '09546465789', '09456798123', 'Latrinidad Benguet', '2023-10-30', 'avatar-9.jpg', 'farmer', 'facebook.com', 'twitter.com', 'instagram.com', 'active', '2023-11-15 02:29:02', '2023-11-15 04:05:05'),
('FARMER-70441192', 'qwerty@gmail.com', '985f4b4458', 'qwerty@gmail.com', 'Juan Dela Cruz', 'male', '09789546123', '', 'sdf', '2023-11-09', 'avatar-10.jpg', 'farmer', 'None', 'None', 'None', 'active', '2023-11-15 03:48:16', '2023-11-15 06:16:31'),
('FARMER-84345042', 'cardodalisay@gmail.com', 'c75c9ff116', 'cardodalisay@gmail.com', 'Cardo Dalisay', 'male', '09546465789', NULL, 'Baguio City Benguet', '2023-11-17', 'avatar-3.jpg', 'farmer', NULL, NULL, NULL, 'active', '2023-11-15 02:42:42', '2023-11-15 02:42:42'),
('FARMER-89598202', 'juandelacruz@gmail.com', 'e16921bf00', 'juandelacruz@gmail.com', 'Dos Dela Cruz', 'male', '09546465789adfs', '', 'Baguio City Benguet', '2023-11-16', 'avatar-5.jpg', 'farmer', '', '', '', 'active', '2023-11-15 00:13:34', '2023-11-15 06:16:50');

--
-- Triggers `tbl_farmer_users`
--
DELIMITER $$
CREATE TRIGGER `before_farmer_generateuserpass` BEFORE INSERT ON `tbl_farmer_users` FOR EACH ROW BEGIN
    IF NEW.role = 'none' THEN
		SET New.role = 'farmer';
        SET NEW.username = NEW.email;
        SET NEW.password = CONCAT(SUBSTRING(MD5(RAND()) FROM 1 FOR 4), 
                                   SUBSTRING(MD5(RAND()) FROM 1 FOR 4), 
                                   LPAD(FLOOR(RAND() * 100), 2, '0')); -- Generating a 10-character password with numbers and letters
    END IF;
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `user_id_auto_generate` BEFORE INSERT ON `tbl_farmer_users` FOR EACH ROW BEGIN
    DECLARE unique_id VARCHAR(20);
    SET unique_id = CONCAT('FARMER-', LPAD(FLOOR(RAND() * 100000000), 8, '0'));

    -- Ensure the generated ID is unique
    WHILE (SELECT COUNT(*) FROM tbl_farmer_users WHERE user_id = unique_id) > 0 DO
        SET unique_id = CONCAT('USERS-', LPAD(FLOOR(RAND() * 100000000), 8, '0'));
    END WHILE;

    SET NEW.user_id = unique_id;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_products`
--

CREATE TABLE `tbl_products` (
  `product_id` varchar(20) NOT NULL,
  `product_cat_id` varchar(20) NOT NULL,
  `user_id` varchar(20) NOT NULL,
  `product_name` varchar(20) NOT NULL,
  `product_description` varchar(250) NOT NULL,
  `product_photo` varchar(20) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_at` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_products`
--

INSERT INTO `tbl_products` (`product_id`, `product_cat_id`, `user_id`, `product_name`, `product_description`, `product_photo`, `created_at`, `updated_at`) VALUES
('PRCT-41265910', 'PRCAT-44992941', 'FARMER-89598202', 'Onions', 'Fresh, aromatic onions sourced directly from our farm. Adds flavor to various dishes like soups, salads, and stir-fries.', '14.png', '2023-11-15 04:02:38', '2023-11-15 05:09:21'),
('PRCT-49315910', 'PRCAT-71813648', 'FARMER-89598202', 'Papaya', 'Sweet and juicy papayas grown with care. Perfect for smoothies or fruit salads.', '2.png', '2023-11-15 04:02:38', '2023-11-15 05:09:12'),
('PRCT-49365789', 'PRCAT-03757841', 'FARMER-84345042', 'Brocoli to', 'resh broccoli packed with nutrients. Ideal for steaming or stir-frying.\"', '12.png', '2023-11-15 04:02:38', '2023-11-15 05:10:54'),
('PRCT-49365910', 'PRCAT-71813648', 'FARMER-84345042', 'Avocado', 'Delicious, ripe avocados. Ideal for guacamole or a healthy snack.', '4.png', '2023-11-15 04:02:38', '2023-11-15 05:10:27'),
('PRCT-49365970', 'PRCAT-06411980', 'FARMER-69146423', 'Cabbage', 'Fresh, organic cabbage harvested from our farm. Perfect for salads and coleslaw.', '15.png', '2023-11-15 04:02:38', '2023-11-15 04:39:53'),
('PRCT-78365910', 'PRCAT-71404969', 'FARMER-69146423', 'Mushroom', 'High-quality mushrooms suitable for various dishes. Great for soups and stir-fries', '8.png', '2023-11-15 04:02:38', '2023-11-15 05:13:04'),
('PRDT-02589212', 'PRCAT-98983374', 'FARMER-89598202', 'Baguio Strawberry', 'Delightfully sweet Baguio strawberries. Enjoy them fresh or in desserts.', '3.png', '2023-11-15 05:04:25', '2023-11-15 05:09:05'),
('PRDT-24510392', 'PRCAT-69558258', 'FARMER-84345042', 'Baguio Sayote', 'Fresh From Baguio', '6.png', '2023-11-15 05:52:31', '2023-11-15 05:52:47');

--
-- Triggers `tbl_products`
--
DELIMITER $$
CREATE TRIGGER `products_id_auto_generate` BEFORE INSERT ON `tbl_products` FOR EACH ROW BEGIN
    DECLARE unique_id VARCHAR(20);
    SET unique_id = CONCAT('PRDT-', LPAD(FLOOR(RAND() * 100000000), 8, '0'));

    -- Ensure the generated ID is unique
    WHILE (SELECT COUNT(*) FROM tbl_products WHERE product_id = unique_id) > 0 DO
        SET unique_id = CONCAT('USERS-', LPAD(FLOOR(RAND() * 100000000), 8, '0'));
    END WHILE;

    SET NEW.product_id = unique_id;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_product_categories`
--

CREATE TABLE `tbl_product_categories` (
  `product_cat_id` varchar(20) NOT NULL,
  `product_cat_name` varchar(50) NOT NULL,
  `product_cat_description` varchar(250) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_product_categories`
--

INSERT INTO `tbl_product_categories` (`product_cat_id`, `product_cat_name`, `product_cat_description`) VALUES
('PRCAT-03757841', 'Cruciferous Vegetables', 'Vegetables from the Brassicaceae family, often with cross-shaped flowers.'),
('PRCAT-06411980', 'Leafy Greens', 'Vegetables with edible leaves, rich in vitamins and minerals.'),
('PRCAT-13691189', 'Legumes', 'Protein and fiber-rich vegetables like beans, peas, and lentils.'),
('PRCAT-23186576', 'Rdible Tubers', 'Swollen underground stems like sweet potatoes, yams, and cassava. sf'),
('PRCAT-24598755', 'Root Vegetables', 'Vegetables with starchy or fibrous roots that grow underground.'),
('PRCAT-26312054', 'Gourds', 'Fleshy fruits often used as vegetables, such as zucchini, pumpkins, and cucumbers.'),
('PRCAT-33477123', 'Nightshades', 'Vegetables from the Solanaceae family, including tomatoes, bell peppers, eggplants, and potatoes.'),
('PRCAT-44992941', 'Allium Vegetables', 'Vegetables in the Allium genus, known for strong flavor and aroma.'),
('PRCAT-48883208', 'Peppers', 'Bell peppers, chili peppers, and sweet peppers used in various cuisines.'),
('PRCAT-69153715', 'Microgreens', 'Young, edible plants harvested at an early stage and often used as garnishes.'),
('PRCAT-69558258', 'Squashes', 'Summer and winter squashes like yellow squash, zucchini, butternut, and acorn squash.'),
('PRCAT-71404969', 'Fungi', 'The meaty richness of Portobello mushrooms to the earthy delicacy of truffles, our fungi selection offers a diverse array of flavors and textures, perfect for elevating culinary experiences'),
('PRCAT-71813648', 'Fruits', 'From the tropical sweetness of mangoes and the crisp versatility of apples to the juicy succulence of peaches and citrusy burst of oranges, our handpicked fruit selection offers a diverse array of flavors and nutrients to elevate your culinary experi'),
('PRCAT-94677588', 'Leafy Herbs', 'Herbs that are also used as vegetables, such as parsley, cilantro, and basil.'),
('PRCAT-98983374', 'Berries', 'From sweet strawberries and tart raspberries to antioxidant-rich blueberries and versatile blackberries, our selection offers a range of vibrant, flavorful berries perfect for diverse culinary creations.');

--
-- Triggers `tbl_product_categories`
--
DELIMITER $$
CREATE TRIGGER `product_categoriesid_auto_generate` BEFORE INSERT ON `tbl_product_categories` FOR EACH ROW BEGIN
    DECLARE unique_id VARCHAR(20);
    SET unique_id = CONCAT('PRCAT-', LPAD(FLOOR(RAND() * 100000000), 8, '0'));

    -- Ensure the generated ID is unique
    WHILE (SELECT COUNT(*) FROM tbl_product_categories WHERE product_cat_id = unique_id) > 0 DO
        SET unique_id = CONCAT('USERS-', LPAD(FLOOR(RAND() * 100000000), 8, '0'));
    END WHILE;

    SET NEW.product_cat_id = unique_id;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `tbl_product_size`
--

CREATE TABLE `tbl_product_size` (
  `products_size_id` varchar(50) NOT NULL,
  `products_size` varchar(15) NOT NULL,
  `products_size_short` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `tbl_product_size`
--

INSERT INTO `tbl_product_size` (`products_size_id`, `products_size`, `products_size_short`) VALUES
('2', 'Medium', 'M'),
('3', 'Large', 'L'),
('4', 'Extra Larg', 'XL'),
('SIZE-', 'Small', 'S');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `comments_tbl`
--
ALTER TABLE `comments_tbl`
  ADD PRIMARY KEY (`comments_id`);

--
-- Indexes for table `contactus_tbl`
--
ALTER TABLE `contactus_tbl`
  ADD PRIMARY KEY (`contactus_id`);

--
-- Indexes for table `tbl_admin_users`
--
ALTER TABLE `tbl_admin_users`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `tbl_farmer_users`
--
ALTER TABLE `tbl_farmer_users`
  ADD PRIMARY KEY (`user_id`),
  ADD UNIQUE KEY `user_id_3` (`user_id`);
ALTER TABLE `tbl_farmer_users` ADD FULLTEXT KEY `user_id` (`user_id`);
ALTER TABLE `tbl_farmer_users` ADD FULLTEXT KEY `user_id_2` (`user_id`);

--
-- Indexes for table `tbl_products`
--
ALTER TABLE `tbl_products`
  ADD PRIMARY KEY (`product_id`);

--
-- Indexes for table `tbl_product_categories`
--
ALTER TABLE `tbl_product_categories`
  ADD PRIMARY KEY (`product_cat_id`);

--
-- Indexes for table `tbl_product_size`
--
ALTER TABLE `tbl_product_size`
  ADD PRIMARY KEY (`products_size_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `comments_tbl`
--
ALTER TABLE `comments_tbl`
  MODIFY `comments_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `contactus_tbl`
--
ALTER TABLE `contactus_tbl`
  MODIFY `contactus_id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
