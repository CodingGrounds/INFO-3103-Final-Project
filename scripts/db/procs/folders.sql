DROP PROCEDURE IF EXISTS add_folder;
DROP PROCEDURE IF EXISTS delete_folder;

DELIMITER //

CREATE PROCEDURE add_folder(
    IN in_uuid VARCHAR(36),
    IN in_owner_id VARCHAR(36),
    IN in_parent_folder_id VARCHAR(36),
    IN in_name VARCHAR(255),
    IN in_path VARCHAR(4096)
)
BEGIN
    INSERT INTO folders (uuid, owner_id, parent_folder_id, name, path)
    VALUES (in_uuid, in_owner_id, in_parent_folder_id, in_name, in_path);
END//

CREATE PROCEDURE delete_folder(IN in_id VARCHAR(36))
BEGIN
  DELETE FROM folders WHERE uuid = in_id;
END//


DROP PROCEDURE IF EXISTS delete_folder_by_owner;
CREATE PROCEDURE delete_folder_by_owner(IN in_owner_id VARCHAR(36))
BEGIN
    DELETE FROM folders WHERE owner_id = in_owner_id;
END//
DELIMITER ;
