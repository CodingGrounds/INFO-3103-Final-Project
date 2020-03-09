 CREATE INDEX idx_files_folder_id           ON files (folder_id);
 CREATE INDEX idx_files_owner_id            ON files (owner_id);
 CREATE INDEX idx_folders_owner_id          ON folders (owner_id);
 CREATE INDEX idx_users_root_folder_id      ON users (root_folder_id);
