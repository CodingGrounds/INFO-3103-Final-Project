DELIMITER //

DROP PROCEDURE IF EXISTS add_user;

CREATE PROCEDURE add_user(
    IN in_uuid VARCHAR(36),
    IN in_login_name VARCHAR(255),
    IN in_root_folder_id VARCHAR(36)
)
BEGIN
    INSERT INTO users (login_name, root_folder_id)
    VALUES (in_login_name, in_root_folder_id);
END//

DROP PROCEDURE IF EXISTS get_user_by_id;
CREATE PROCEDURE get_user_by_id(IN in_id VARCHAR(36))
BEGIN
    SELECT * FROM users WHERE uuid = in_id;
end //

DROP PROCEDURE IF EXISTS delete_user;
CREATE PROCEDURE delete_user(IN in_user_id VARCHAR(36))
BEGIN
    UPDATE users SET active = FALSE WHERE uuid = in_user_id;
end //

DELIMITER ;
