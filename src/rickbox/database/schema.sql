CREATE TABLE `users` (
  `id` int NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `rootFolderId` int NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `name` varchar(255),
  `createdAt` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE `files` (
  `id` int NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `folderId` int DEFAULT NULL,
  `ownerId` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `path` varchar(255) NOT NULL,
  `extension` varchar(255) DEFAULT NULL,
  `hash` varchar(255) NOT NULL,
  `size` int unsigned NOT NULL,
  `createdAt` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modifiedAt` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE `folders` (
  `id` int NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `ownerId` int NOT NULL,
  `parentFolderId` int DEFAULT NULL,
  `name` varchar(255) NOT NULL,
  `createdAt` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modifiedAt` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE `files`     ADD FOREIGN KEY (`folderId`)        REFERENCES `folders` (`id`);
ALTER TABLE `files`     ADD FOREIGN KEY (`ownerId`)         REFERENCES `users` (`id`);
ALTER TABLE `folders`   ADD FOREIGN KEY (`ownerId`)         REFERENCES `users` (`id`);
ALTER TABLE `folders`   ADD FOREIGN KEY (`parentFolderId`)  REFERENCES `folders` (`id`);
ALTER TABLE `users`     ADD FOREIGN KEY (`rootFolderId`)    REFERENCES `folders` (`id`);

CREATE INDEX `idx_files_folderId`           ON `files` (`folderId`);
CREATE INDEX `idx_files_ownerId`            ON `files` (`ownerId`);
CREATE INDEX `idx_folders_ownerId`          ON `folders` (`ownerId`);
CREATE INDEX `idx_users_rootFolderId`       ON `users` (`rootFolderId`);

