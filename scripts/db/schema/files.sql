DROP TABLE IF EXISTS files;

CREATE TABLE files (
    id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
    owner_id INT UNSIGNED NOT NULL,
    name VARCHAR(255) NOT NULL,
    path VARCHAR(4096) NOT NULL,
    size INT UNSIGNED DEFAULT 0,
    last_modified TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);