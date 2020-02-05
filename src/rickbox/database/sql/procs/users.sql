DELIMITER //

DROP PROCEDURE IF EXISTS add_user;
CREATE PROCEDURE add_user(IN in_login_name varchar(255), IN in_root_folder_id int)
BEGIN
    INSERT INTO users (login_name, root_folder_id)
    VALUES (in_login_name, in_root_folder_id);
END//

DROP PROCEDURE IF EXISTS get_user_by_id;
CREATE PROCEDURE get_user_by_id(IN in_id int)
BEGIN
    SELECT * FROM users WHERE id = in_id;
end //

DROP PROCEDURE IF EXISTS user_set_active;
CREATE PROCEDURE user_set_active(IN in_user_id int, IN in_active_state bool)
BEGIN
    UPDATE users SET active = in_active_state WHERE id = in_user_id;
end //

DELIMITER ;
