CREATE TABLE `collection` (
  `collection_id` bigint PRIMARY KEY AUTO_INCREMENT,
  `collection_name` varchar(100) UNIQUE NOT NULL,
  `language` varchar(100) NOT NULL,
  `category` varchar(100)
);

CREATE TABLE `word` (
  `word_id` bigint PRIMARY KEY AUTO_INCREMENT,
  `word` varchar(100) NOT NULL,
  `translation` Text NOT NULL,
  `last_try` enum('Sei','N Sei','N Feito') DEFAULT 'N Feito'
  `collection_id` bigint NOT NULL,
  FOREIGN KEY (`collection_id`) REFERENCES `collection`(`collection_id`) ON DELETE CASCADE
);