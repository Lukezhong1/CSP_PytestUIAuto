

CREATE TABLE `skw_ui_test_data_head` (
                                         `id` VARCHAR(50) NOT NULL COMMENT 'Test ID',
                                         `project_id` VARCHAR(50) NOT NULL COMMENT 'Project ID this test belongs to',
                                         `name` VARCHAR(255) NOT NULL COMMENT 'Test data name',
                                         `description` LONGTEXT COMMENT 'Test description',
                                         `create_user_id` VARCHAR(64) DEFAULT NULL COMMENT 'User ID',
                                         `update_user_id` VARCHAR(64) DEFAULT NULL COMMENT 'User ID',
                                         `create_time` BIGINT NOT NULL COMMENT 'Create timestamp',
                                         `update_time` BIGINT NOT NULL COMMENT 'Update timestamp',
                                         `tags` VARCHAR(1000) DEFAULT NULL,
                                         PRIMARY KEY (`id`),
                                         KEY `create_user_id` (`create_user_id`),
                                         KEY `update_user_id` (`update_user_id`)
) ENGINE=INNODB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci


CREATE TABLE `skw_ui_test_data_detail` (
                                           `id` VARCHAR(50) NOT NULL COMMENT 'Test ID',
                                           `name` VARCHAR(255) NOT NULL COMMENT 'Test data name',
                                           `priority` VARCHAR(64) NOT NULL COMMENT 'priority',
                                           `data_contents` LONGTEXT COMMENT 'data_contents (value split by ->)',
                                           `description` LONGTEXT COMMENT 'Test data description',
                                           `create_user_id` VARCHAR(64) DEFAULT NULL COMMENT 'User ID',
                                           `update_user_id` VARCHAR(64) DEFAULT NULL COMMENT 'User ID',
                                           `create_time` BIGINT NOT NULL COMMENT 'Create timestamp',
                                           `update_time` BIGINT NOT NULL COMMENT 'Update timestamp',
                                           PRIMARY KEY (`id`),
                                           KEY `create_user_id` (`create_user_id`),
                                           KEY `update_user_id` (`update_user_id`)
) ENGINE=INNODB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci