DROP PROCEDURE IF EXISTS add_user;
DROP PROCEDURE IF EXISTS get_user;
DROP PROCEDURE IF EXISTS get_user_by_username;

DELIMITER //

CREATE PROCEDURE add_user(
    IN in_username VARCHAR(255),
    IN in_name VARCHAR(255),
    IN in_email VARCHAR(255)
)
BEGIN
    INSERT INTO users (username, name, email)
    VALUES (in_username, in_name, in_email);
    SELECT LAST_INSERT_ID();
END //

CREATE PROCEDURE get_user(IN in_identifier VARCHAR(255))
BEGIN
    SELECT * FROM users WHERE CONCAT(id, '') = in_identifier OR username = in_identifier;
END //

CREATE PROCEDURE get_user_by_username(IN in_username VARCHAR(255))
BEGIN
    SELECT * FROM users WHERE username = in_username;
END //

DELIMITER ;
