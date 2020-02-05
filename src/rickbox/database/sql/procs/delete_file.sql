DELIMITER //

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
