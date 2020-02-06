DELIMITER //

DROP PROCEDURE IF EXISTS get_columns_for_table;
CREATE PROCEDURE get_columns_for_table(IN in_table_name varchar(255))
BEGIN
    SELECT column_name
        FROM information_schema.columns
        WHERE table_name = in_table_name;
END //

DROP PROCEDURE IF EXISTS get_row_by_column;
CREATE PROCEDURE get_row_by_column(IN in_table_name varchar(255), IN in_column_name varchar(255), IN in_column_value INT)
BEGIN
    SET @table_name = in_table_name;
    SET @column_value = in_column_value;
    SET @column_name = in_column_name;

    SET @query = concat('SELECT * FROM ', @table_name, ' WHERE ', @column_name, ' = ', @column_value);
    PREPARE stmt FROM @query;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END //
DELIMITER ;
