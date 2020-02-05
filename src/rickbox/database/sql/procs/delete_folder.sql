DELIMITER //

DROP PROCEDURE IF EXISTS delete_folder;
CREATE PROCEDURE delete_folder(IN in_id INT)
BEGIN
  DELETE FROM folders WHERE id = in_id;
END//


DROP PROCEDURE IF EXISTS delete_folder_by_owner;
CREATE PROCEDURE delete_folder_by_owner(IN in_owner_id INT)
BEGIN
    DELETE FROM folders WHERE owner_id = in_owner_id;
END//

DELIMITER ;
