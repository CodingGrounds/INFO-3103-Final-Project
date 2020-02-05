DROP TABLE IF EXISTS users;

CREATE TABLE `users` (
  `id` int NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `active` bool NOT NULL DEFAULT TRUE,
  `root_folder_id` int NOT NULL,
  `login_name` varchar(255) NOT NULL,
  `display_name` varchar(255),
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
);

