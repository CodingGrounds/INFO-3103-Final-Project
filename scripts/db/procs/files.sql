DROP PROCEDURE IF EXISTS add_file;
DROP PROCEDURE IF EXISTS delete_file;
DROP PROCEDURE IF EXISTS delete_file_by_owner;

DELIMITER //

CREATE PROCEDURE add_file(
    IN in_uuid VARCHAR(36),
    IN in_folder_id VARCHAR(36),
    IN in_owner_id VARCHAR(36),
    IN in_name VARCHAR(255),
    IN in_path VARCHAR(4096)
)
BEGIN
    INSERT INTO files (uuid, folder_id, owner_id, name, path)
    VALUES (in_uuid, in_folder_id, in_owner_id, in_name, in_path);
END//

CREATE PROCEDURE delete_file(IN in_id VARCHAR(36))
BEGIN
    DELETE FROM files WHERE uuid = in_id;
END//

CREATE PROCEDURE delete_file_by_owner(IN in_owner_id VARCHAR(36))
BEGIN
    DELETE FROM files WHERE owner_id = in_owner_id;
END//

DELIMITER ;
