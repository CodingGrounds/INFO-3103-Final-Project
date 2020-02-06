DELIMITER //

DROP PROCEDURE IF EXISTS add_file;

CREATE PROCEDURE add_file(
  IN in_name varchar(255),
  IN in_path TEXT,
  IN in_folder_id INT,
  IN in_owner_id INT
)
BEGIN
  INSERT INTO files (name, path, folder_id, owner_id)
  VALUES (in_name, in_path, in_owner_id, in_folder_id);
END//

DROP PROCEDURE IF EXISTS delete_file;
CREATE PROCEDURE delete_file(IN in_id INT)
BEGIN
  DELETE FROM files WHERE id = in_id;
END//

DROP PROCEDURE IF EXISTS delete_file_by_owner;
CREATE PROCEDURE delete_file_by_owner(IN in_owner_id INT)
BEGIN
    DELETE FROM files WHERE owner_id = in_owner_id;
END//

DELIMITER ;
