ALTER TABLE `files`
  ADD FOREIGN KEY (`folder_id`)
  REFERENCES `folders` (`id`)
  ON DELETE CASCADE;

ALTER TABLE `files`
  ADD FOREIGN KEY (`owner_id`)
  REFERENCES `users` (`id`)
  ON DELETE CASCADE;

ALTER TABLE `folders`
  ADD FOREIGN KEY (`owner_id`)
  REFERENCES `users` (`id`)
  ON DELETE CASCADE;

ALTER TABLE `folders`
  ADD FOREIGN KEY (`parent_folder_id`)
  REFERENCES `folders` (`id`)
  ON DELETE CASCADE;

ALTER TABLE `users`
  ADD FOREIGN KEY (`root_folder_id`)
  REFERENCES `folders` (`id`);
