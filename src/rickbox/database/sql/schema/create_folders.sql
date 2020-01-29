DROP TABLE IF EXISTS folders;

CREATE TABLE `folders` (
  `id` int NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `owner_id` int NOT NULL,
  `parent_folder_id` int DEFAULT NULL,
  `name` varchar(255) NOT NULL,
  `path` TEXT NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modified_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
);

