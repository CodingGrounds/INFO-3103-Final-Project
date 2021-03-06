DROP PROCEDURE IF EXISTS add_file;
DROP PROCEDURE IF EXISTS get_file_by_id;
DROP PROCEDURE IF EXISTS get_file_by_owner_id;
DROP PROCEDURE IF EXISTS delete_file;
DROP PROCEDURE IF EXISTS update_file;

DELIMITER //

CREATE PROCEDURE add_file(
    IN in_owner_id INT UNSIGNED,
    IN in_name VARCHAR(255),
    IN in_path VARCHAR(4096),
    IN in_size INT UNSIGNED
)
BEGIN
    INSERT INTO files (owner_id, name, path, size)
    VALUES (in_owner_id, in_name, in_path, in_size);
    SELECT LAST_INSERT_ID();
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

CREATE PROCEDURE update_file(IN in_id INT UNSIGNED, IN in_name VARCHAR(255), IN in_path VARCHAR(4096))
BEGIN
    UPDATE files
    SET
        name = in_name,
        path = in_path,
        last_modified = CURRENT_TIMESTAMP
    WHERE id = in_id;
END //

DELIMITER ;
