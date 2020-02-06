CREATE TABLE files (
  id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
  folder_id int DEFAULT NULL,
  owner_id int NOT NULL,
  name varchar(255) NOT NULL,
  path TEXT NOT NULL,
  extension varchar(255) DEFAULT NULL,
  hash varchar(255) DEFAULT NULL,
  size int unsigned DEFAULT NULL,
  created_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  modified_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
);
