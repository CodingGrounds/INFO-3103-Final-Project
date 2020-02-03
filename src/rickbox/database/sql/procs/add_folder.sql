DELIMITER //

DROP PROCEDURE IF EXISTS add_folder;

CREATE PROCEDURE add_folder(
  IN in_name varchar(255),
  IN in_parent_folder_id INT,
  IN in_owner_id INT
)
BEGIN
  DECLARE folder_path TEXT DEFAULT NULL;
  SELECT CONCAT(
    (SELECT path FROM folders WHERE id = in_parent_folder_id),
    '/',
    in_name
  ) INTO folder_path;

  INSERT INTO folders (name, parent_folder_id, owner_id, path)
  VALUES (in_name, in_parent_folder_id, in_owner_id, folder_path);
END//

DELIMITER ;
