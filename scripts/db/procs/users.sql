DROP PROCEDURE IF EXISTS add_user;
DROP PROCEDURE IF EXISTS get_user_by_id;
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
END //

CREATE PROCEDURE get_user_by_id(IN in_id INT UNSIGNED)
BEGIN
    SELECT * FROM users WHERE id = in_id;
END //

CREATE PROCEDURE get_user_by_username(IN in_username VARCHAR(255))
BEGIN
    SELECT * FROM users WHERE username = in_username;
END //

DELIMITER ;
