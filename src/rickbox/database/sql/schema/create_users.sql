DROP TABLE IF EXISTS users;

CREATE TABLE `users` (
  `id` int NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `root_folder_id` int NOT NULL,
  `username` varchar(255) NOT NULL,
  `name` varchar(255),
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
);

