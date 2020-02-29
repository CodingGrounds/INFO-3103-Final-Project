DROP PROCEDURE IF EXISTS add_file;
DROP PROCEDURE IF EXISTS get_file_by_id;
DROP PROCEDURE IF EXISTS get_file_by_owner_id;
DROP PROCEDURE IF EXISTS delete_file;

DELIMITER //

CREATE PROCEDURE add_file(
    IN in_owner_id INT UNSIGNED,
    IN in_name VARCHAR(255),
    IN in_path VARCHAR(4096)
)
BEGIN
    INSERT INTO files (owner_id, name, path)
    VALUES (in_owner_id, in_name, in_path);
END //

CREATE PROCEDURE get_file_by_id(IN in_id INT UNSIGNED)
BEGIN
    SELECT * FROM files WHERE id = in_id;
END //

CREATE PROCEDURE get_file_by_owner_id(IN in_owner_id INT UNSIGNED)
BEGIN
    SELECT * FROM files WHERE owner_id = in_owner_id;
END //

CREATE PROCEDURE delete_file(IN in_id INT UNSIGNED)
BEGIN
    DELETE FROM files WHERE id = in_id;
END //

DELIMITER ;
