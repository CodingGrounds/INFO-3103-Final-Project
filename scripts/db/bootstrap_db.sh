#!/bin/bash
printf "DB username: "
read -r USERNAME
printf "Database name: "
read -r DB_NAME
printf "Type the password for user %s: " "$USERNAME"
read -rs PASSWORD

# pass the --hard option to this script to drop and re-create the entire database.
if [ $1 ]; then
  if [ $1 = '--hard' ]; then
    echo "Dropping/creating database $DB_NAME..."
    mysql -u $USERNAME --password="$PASSWORD" -e "DROP DATABASE IF EXISTS $DB_NAME;"
    mysql -u $USERNAME --password="$PASSWORD" -e "CREATE DATABASE $DB_NAME;"
  fi
fi

echo "Dropping/creating files table..."
mysql -u $USERNAME --password="$PASSWORD" $DB_NAME < ./schema/files.sql

echo "Dropping/creating users table..."
mysql -u $USERNAME --password="$PASSWORD" $DB_NAME < ./schema/users.sql

echo "Dropping/creating foreign key constraints..."
mysql -u $USERNAME --password="$PASSWORD" $DB_NAME < ./schema/fks.sql

echo "Dropping/creating table indexes..."
mysql -u $USERNAME --password="$PASSWORD" $DB_NAME < ./schema/indexes.sql

echo "Dropping/creating stored procedures for files..."
mysql -u $USERNAME --password="$PASSWORD" $DB_NAME < ./procs/files.sql

echo "Dropping/creating stored procedures for users..."
mysql -u $USERNAME --password="$PASSWORD" $DB_NAME < ./procs/users.sql
