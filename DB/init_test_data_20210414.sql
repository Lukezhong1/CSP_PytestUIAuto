#清除之前测试数据
DELETE FROM skw_ui_test_data_detail;
DELETE FROM skw_ui_test_data_head;

#使用正确的用户名及密码，登录成功
SET @id=UUID();
SET @project_id=(SELECT p.id FROM project p JOIN `workspace` w ON p.`workspace_id`=w.id WHERE p.`name`='CSP' AND w.`name`='测试工作空间');
SET @Module_name='login_data';
SET @priority='1';
SET @create_user_id='luke.zhong';
SET @update_user_id='luke.zhong';
SET @create_time='20210322140714';
SET @tag='tag';
SET @name='login_success_data';
SET @data_contents='admin->pass9876>Welcome, admin';
SET @description='userid->password->expect';
INSERT INTO `metersphere`.`skw_ui_test_data_head` (`id`, `project_id`, `name`, `description`, `create_user_id`, `update_user_id`, `create_time`, `update_time`, `tags`)
VALUES (@id, @project_id, @Module_name, @Module_name, @create_user_id, @create_user_id, @create_time, @create_time, @tag);
INSERT INTO `metersphere`.`skw_ui_test_data_detail` (`id`, `ui_test_id`, `name`, `priority`, `data_contents`, `description`, `create_user_id`, `update_user_id`, `create_time`, `update_time`)
VALUES (UUID(), @id, @name, @priority, @data_contents, @description, @create_user_id, @create_user_id, @create_time, @create_time);

#密码错误，登录失败
SET @id=UUID();
SET @project_id=(SELECT p.id FROM project p JOIN `workspace` w ON p.`workspace_id`=w.id WHERE p.`name`='CSP' AND w.`name`='测试工作空间');
SET @Module_name='login_data';
SET @priority='1';
SET @create_user_id='luke.zhong';
SET @update_user_id='luke.zhong';
SET @create_time='20210322140714';
SET @tag='tag';
SET @name='login_fail_data';
SET @data_contents='luke.zhong->wrong>Wrong password';
SET @description='userid->password->expect';
INSERT INTO `metersphere`.`skw_ui_test_data_head` (`id`, `project_id`, `name`, `description`, `create_user_id`, `update_user_id`, `create_time`, `update_time`, `tags`)
VALUES (@id, @project_id, @Module_name, @Module_name, @create_user_id, @create_user_id, @create_time, @create_time, @tag);
INSERT INTO `metersphere`.`skw_ui_test_data_detail` (`id`, `ui_test_id`, `name`, `priority`, `data_contents`, `description`, `create_user_id`, `update_user_id`, `create_time`, `update_time`)
VALUES (UUID(), @id, @name, @priority, @data_contents, @description, @create_user_id, @create_user_id, @create_time, @create_time);

#密码为空，登录失败
SET @id=UUID();
SET @project_id=(SELECT p.id FROM project p JOIN `workspace` w ON p.`workspace_id`=w.id WHERE p.`name`='CSP' AND w.`name`='测试工作空间');
SET @Module_name='login_data';
SET @priority='1';
SET @create_user_id='luke.zhong';
SET @update_user_id='luke.zhong';
SET @create_time='20210322140714';
SET @tag='tag';
SET @name='login_fail_data';
SET @data_contents='luke.zhong->->Password is required!';
SET @description='userid->password->expect';
INSERT INTO `metersphere`.`skw_ui_test_data_head` (`id`, `project_id`, `name`, `description`, `create_user_id`, `update_user_id`, `create_time`, `update_time`, `tags`)
VALUES (@id, @project_id, @Module_name, @Module_name, @create_user_id, @create_user_id, @create_time, @create_time, @tag);
INSERT INTO `metersphere`.`skw_ui_test_data_detail` (`id`, `ui_test_id`, `name`, `priority`, `data_contents`, `description`, `create_user_id`, `update_user_id`, `create_time`, `update_time`)
VALUES (UUID(), @id, @name, @priority, @data_contents, @description, @create_user_id, @create_user_id, @create_time, @create_time);

#输入的用户名不存在，登录失败
SET @id=UUID();
SET @project_id=(SELECT p.id FROM project p JOIN `workspace` w ON p.`workspace_id`=w.id WHERE p.`name`='CSP' AND w.`name`='测试工作空间');
SET @Module_name='login_data';
SET @priority='1';
SET @create_user_id='luke.zhong';
SET @update_user_id='luke.zhong';
SET @create_time='20210322140714';
SET @tag='tag';
SET @name='login_fail_data';
SET @data_contents='noexist->pass9876->User not found!';
SET @description='userid->password->expect';
INSERT INTO `metersphere`.`skw_ui_test_data_head` (`id`, `project_id`, `name`, `description`, `create_user_id`, `update_user_id`, `create_time`, `update_time`, `tags`)
VALUES (@id, @project_id, @Module_name, @Module_name, @create_user_id, @create_user_id, @create_time, @create_time, @tag);
INSERT INTO `metersphere`.`skw_ui_test_data_detail` (`id`, `ui_test_id`, `name`, `priority`, `data_contents`, `description`, `create_user_id`, `update_user_id`, `create_time`, `update_time`)
VALUES (UUID(), @id, @name, @priority, @data_contents, @description, @create_user_id, @create_user_id, @create_time, @create_time);

#用户名为空，登录失败
SET @id=UUID();
SET @project_id=(SELECT p.id FROM project p JOIN `workspace` w ON p.`workspace_id`=w.id WHERE p.`name`='CSP' AND w.`name`='测试工作空间');
SET @Module_name='login_data';
SET @priority='1';
SET @create_user_id='luke.zhong';
SET @update_user_id='luke.zhong';
SET @create_time='20210322140714';
SET @tag='tag';
SET @name='login_fail_data';
SET @data_contents='->pass9876->User ID is required!';
SET @description='userid->password->expect';
INSERT INTO `metersphere`.`skw_ui_test_data_head` (`id`, `project_id`, `name`, `description`, `create_user_id`, `update_user_id`, `create_time`, `update_time`, `tags`)
VALUES (@id, @project_id, @Module_name, @Module_name, @create_user_id, @create_user_id, @create_time, @create_time, @tag);
INSERT INTO `metersphere`.`skw_ui_test_data_detail` (`id`, `ui_test_id`, `name`, `priority`, `data_contents`, `description`, `create_user_id`, `update_user_id`, `create_time`, `update_time`)
VALUES (UUID(), @id, @name, @priority, @data_contents, @description, @create_user_id, @create_user_id, @create_time, @create_time);

#密码输入错误次数大于5次，登录失败，锁定用户
SET @id=UUID();
SET @project_id=(SELECT p.id FROM project p JOIN `workspace` w ON p.`workspace_id`=w.id WHERE p.`name`='CSP' AND w.`name`='测试工作空间');
SET @Module_name='login_data';
SET @priority='1';
SET @create_user_id='luke.zhong';
SET @update_user_id='luke.zhong';
SET @create_time='20210322140714';
SET @tag='tag';
SET @name='login_fail_repeat_data';
SET @data_contents='luke.zhong->wrong>Password retry times over, user account locked!';
SET @description='userid->password->expect';
INSERT INTO `metersphere`.`skw_ui_test_data_head` (`id`, `project_id`, `name`, `description`, `create_user_id`, `update_user_id`, `create_time`, `update_time`, `tags`)
VALUES (@id, @project_id, @Module_name, @Module_name, @create_user_id, @create_user_id, @create_time, @create_time, @tag);
INSERT INTO `metersphere`.`skw_ui_test_data_detail` (`id`, `ui_test_id`, `name`, `priority`, `data_contents`, `description`, `create_user_id`, `update_user_id`, `create_time`, `update_time`)
VALUES (UUID(), @id, @name, @priority, @data_contents, @description, @create_user_id, @create_user_id, @create_time, @create_time);

#添加Role Setup成功
SET @id=UUID();
SET @project_id=(SELECT p.id FROM project p JOIN `workspace` w ON p.`workspace_id`=w.id WHERE p.`name`='CSP' AND w.`name`='测试工作空间');
SET @Module_name='role_setup_data';
SET @priority='1';
SET @create_user_id='luke.zhong';
SET @update_user_id='luke.zhong';
SET @create_time='20210322140714';
SET @tag='tag';
SET @name='add_role_setup_success_data';
SET @data_contents='roleId->Operate Successfully';
SET @description='roleId->expect';
INSERT INTO `metersphere`.`skw_ui_test_data_head` (`id`, `project_id`, `name`, `description`, `create_user_id`, `update_user_id`, `create_time`, `update_time`, `tags`)
VALUES (@id, @project_id, @Module_name, @Module_name, @create_user_id, @create_user_id, @create_time, @create_time, @tag);
INSERT INTO `metersphere`.`skw_ui_test_data_detail` (`id`, `ui_test_id`, `name`, `priority`, `data_contents`, `description`, `create_user_id`, `update_user_id`, `create_time`, `update_time`)
VALUES (UUID(), @id, @name, @priority, @data_contents, @description, @create_user_id, @create_user_id, @create_time, @create_time);

#role_id已存在，添加失败
SET @id=UUID();
SET @project_id=(SELECT p.id FROM project p JOIN `workspace` w ON p.`workspace_id`=w.id WHERE p.`name`='CSP' AND w.`name`='测试工作空间');
SET @Module_name='role_setup_data';
SET @priority='1';
SET @create_user_id='luke.zhong';
SET @update_user_id='luke.zhong';
SET @create_time='20210322140714';
SET @tag='tag';
SET @name='add_role_setup_fail_data';
SET @data_contents='admin->Role[admin] already exist!';
SET @description='roleId->expect';
INSERT INTO `metersphere`.`skw_ui_test_data_head` (`id`, `project_id`, `name`, `description`, `create_user_id`, `update_user_id`, `create_time`, `update_time`, `tags`)
VALUES (@id, @project_id, @Module_name, @Module_name, @create_user_id, @create_user_id, @create_time, @create_time, @tag);
INSERT INTO `metersphere`.`skw_ui_test_data_detail` (`id`, `ui_test_id`, `name`, `priority`, `data_contents`, `description`, `create_user_id`, `update_user_id`, `create_time`, `update_time`)
VALUES (UUID(), @id, @name, @priority, @data_contents, @description, @create_user_id, @create_user_id, @create_time, @create_time);

#查询新增的task，执行成功
SET @id=UUID();
SET @project_id=(SELECT p.id FROM project p JOIN `workspace` w ON p.`workspace_id`=w.id WHERE p.`name`='CSP' AND w.`name`='测试工作空间');
SET @Module_name='task_mamt_data';
SET @priority='1';
SET @create_user_id='luke.zhong';
SET @update_user_id='luke.zhong';
SET @create_time='20210322140714';
SET @tag='tag';
SET @name='add_query_execute_task_success_data';
SET @data_contents='MCD_MASTER->MCD_MASTER_taskId->Success';
SET @description='functionID—>taskId->expect';
INSERT INTO `metersphere`.`skw_ui_test_data_head` (`id`, `project_id`, `name`, `description`, `create_user_id`, `update_user_id`, `create_time`, `update_time`, `tags`)
VALUES (@id, @project_id, @Module_name, @Module_name, @create_user_id, @create_user_id, @create_time, @create_time, @tag);
INSERT INTO `metersphere`.`skw_ui_test_data_detail` (`id`, `ui_test_id`, `name`, `priority`, `data_contents`, `description`, `create_user_id`, `update_user_id`, `create_time`, `update_time`)
VALUES (UUID(), @id, @name, @priority, @data_contents, @description, @create_user_id, @create_user_id, @create_time, @create_time);

#查询task，执行成功
SET @id=UUID();
SET @project_id=(SELECT p.id FROM project p JOIN `workspace` w ON p.`workspace_id`=w.id WHERE p.`name`='CSP' AND w.`name`='测试工作空间');
SET @Module_name='task_mamt_data';
SET @priority='1';
SET @create_user_id='luke.zhong';
SET @update_user_id='luke.zhong';
SET @create_time='20210322140714';
SET @tag='tag';
SET @name='query_execute_task_success';
SET @data_contents='MCD_MASTER_taskId->Success';
SET @description='taskId->expect';
INSERT INTO `metersphere`.`skw_ui_test_data_head` (`id`, `project_id`, `name`, `description`, `create_user_id`, `update_user_id`, `create_time`, `update_time`, `tags`)
VALUES (@id, @project_id, @Module_name, @Module_name, @create_user_id, @create_user_id, @create_time, @create_time, @tag);
INSERT INTO `metersphere`.`skw_ui_test_data_detail` (`id`, `ui_test_id`, `name`, `priority`, `data_contents`, `description`, `create_user_id`, `update_user_id`, `create_time`, `update_time`)
VALUES (UUID(), @id, @name, @priority, @data_contents, @description, @create_user_id, @create_user_id, @create_time, @create_time);

#新增Report Func Setup
SET @id=UUID();
SET @project_id=(SELECT p.id FROM project p JOIN `workspace` w ON p.`workspace_id`=w.id WHERE p.`name`='CSP' AND w.`name`='测试工作空间');
SET @Module_name='report_func_setup';
SET @priority='1';
SET @create_user_id='luke.zhong';
SET @update_user_id='luke.zhong';
SET @create_time='20210322140714';
SET @tag='tag';
SET @name='add_report_func_setup_data';
SET @data_contents='functionId->functionName->exportFileName_tr1->exportFileName_tr2->exportFileName_tr3->.csv->1->D:\Export_Import->4->mappingBtn_paramValue1->mappingBtn_paramValue2->mappingBtn_paramValue3->mappingBtn_paramValue4->Operate Successfully';
SET @description='functionId->exportPath->exportFileName_tr1->exportFileName_tr3->expect';
INSERT INTO `metersphere`.`skw_ui_test_data_head` (`id`, `project_id`, `name`, `description`, `create_user_id`, `update_user_id`, `create_time`, `update_time`, `tags`)
VALUES (@id, @project_id, @Module_name, @Module_name, @create_user_id, @create_user_id, @create_time, @create_time, @tag);
INSERT INTO `metersphere`.`skw_ui_test_data_detail` (`id`, `ui_test_id`, `name`, `priority`, `data_contents`, `description`, `create_user_id`, `update_user_id`, `create_time`, `update_time`)
VALUES (UUID(), @id, @name, @priority, @data_contents, @description, @create_user_id, @create_user_id, @create_time, @create_time);

#更新Report Func Setup
SET @id=UUID();
SET @project_id=(SELECT p.id FROM project p JOIN `workspace` w ON p.`workspace_id`=w.id WHERE p.`name`='CSP' AND w.`name`='测试工作空间');
SET @Module_name='report_func_setup';
SET @priority='1';
SET @create_user_id='luke.zhong';
SET @update_user_id='luke.zhong';
SET @create_time='20210322140714';
SET @tag='tag';
SET @name='update_all_report_func_setup_data';
SET @data_contents='MCD_MASTER->D:\\Export_Import->MCD_MASTER->.csv->Operate Successfully';
SET @description='functionId->exportPath->exportFileName_tr1->exportFileName_tr3->expect';
INSERT INTO `metersphere`.`skw_ui_test_data_head` (`id`, `project_id`, `name`, `description`, `create_user_id`, `update_user_id`, `create_time`, `update_time`, `tags`)
VALUES (@id, @project_id, @Module_name, @Module_name, @create_user_id, @create_user_id, @create_time, @create_time, @tag);
INSERT INTO `metersphere`.`skw_ui_test_data_detail` (`id`, `ui_test_id`, `name`, `priority`, `data_contents`, `description`, `create_user_id`, `update_user_id`, `create_time`, `update_time`)
VALUES (UUID(), @id, @name, @priority, @data_contents, @description, @create_user_id, @create_user_id, @create_time, @create_time);

#添加User_Setup成功
SET @id=UUID();
SET @project_id=(SELECT p.id FROM project p JOIN `workspace` w ON p.`workspace_id`=w.id WHERE p.`name`='CSP' AND w.`name`='测试工作空间');
SET @Module_name='user_setup_data';
SET @priority='1';
SET @create_user_id='luke.zhong';
SET @update_user_id='luke.zhong';
SET @create_time='20210322140714';
SET @tag='tag';
SET @name='add_user_setup_success';
SET @data_contents='adduserId->userName->admin@qq.com->Operate Successfully';
SET @description='userId->userName->email->expect';
INSERT INTO `metersphere`.`skw_ui_test_data_head` (`id`, `project_id`, `name`, `description`, `create_user_id`, `update_user_id`, `create_time`, `update_time`, `tags`)
VALUES (@id, @project_id, @Module_name, @Module_name, @create_user_id, @create_user_id, @create_time, @create_time, @tag);
INSERT INTO `metersphere`.`skw_ui_test_data_detail` (`id`, `ui_test_id`, `name`, `priority`, `data_contents`, `description`, `create_user_id`, `update_user_id`, `create_time`, `update_time`)
VALUES (UUID(), @id, @name, @priority, @data_contents, @description, @create_user_id, @create_user_id, @create_time, @create_time);

#查询新增的User_Setup
SET @id=UUID();
SET @project_id=(SELECT p.id FROM project p JOIN `workspace` w ON p.`workspace_id`=w.id WHERE p.`name`='CSP' AND w.`name`='测试工作空间');
SET @Module_name='user_setup_data';
SET @priority='1';
SET @create_user_id='luke.zhong';
SET @update_user_id='luke.zhong';
SET @create_time='20210322140714';
SET @tag='tag';
SET @name='add_user_setup_success';
SET @data_contents='userId->userName->admin@qq.com->Operate Successfully';
SET @description='userId->userName->email->expect';
INSERT INTO `metersphere`.`skw_ui_test_data_head` (`id`, `project_id`, `name`, `description`, `create_user_id`, `update_user_id`, `create_time`, `update_time`, `tags`)
VALUES (@id, @project_id, @Module_name, @Module_name, @create_user_id, @create_user_id, @create_time, @create_time, @tag);
INSERT INTO `metersphere`.`skw_ui_test_data_detail` (`id`, `ui_test_id`, `name`, `priority`, `data_contents`, `description`, `create_user_id`, `update_user_id`, `create_time`, `update_time`)
VALUES (UUID(), @id, @name, @priority, @data_contents, @description, @create_user_id, @create_user_id, @create_time, @create_time);

#User_Setup-userId为空，添加失败
SET @id=UUID();
SET @project_id=(SELECT p.id FROM project p JOIN `workspace` w ON p.`workspace_id`=w.id WHERE p.`name`='CSP' AND w.`name`='测试工作空间');
SET @Module_name='user_setup_data';
SET @priority='1';
SET @create_user_id='luke.zhong';
SET @update_user_id='luke.zhong';
SET @create_time='20210322140714';
SET @tag='tag';
SET @name='add_user_setup_fail_data';
SET @data_contents='->userName->admin@qq.com->Operate Successfully';
SET @description='userId->userName->email->expect';
INSERT INTO `metersphere`.`skw_ui_test_data_head` (`id`, `project_id`, `name`, `description`, `create_user_id`, `update_user_id`, `create_time`, `update_time`, `tags`)
VALUES (@id, @project_id, @Module_name, @Module_name, @create_user_id, @create_user_id, @create_time, @create_time, @tag);
INSERT INTO `metersphere`.`skw_ui_test_data_detail` (`id`, `ui_test_id`, `name`, `priority`, `data_contents`, `description`, `create_user_id`, `update_user_id`, `create_time`, `update_time`)
VALUES (UUID(), @id, @name, @priority, @data_contents, @description, @create_user_id, @create_user_id, @create_time, @create_time);

#userId少于5个字符，添加失败
SET @id=UUID();
SET @project_id=(SELECT p.id FROM project p JOIN `workspace` w ON p.`workspace_id`=w.id WHERE p.`name`='CSP' AND w.`name`='测试工作空间');
SET @Module_name='user_setup_data';
SET @priority='1';
SET @create_user_id='luke.zhong';
SET @update_user_id='luke.zhong';
SET @create_time='20210322140714';
SET @tag='tag';
SET @name='add_user_setup_fail_data';
SET @data_contents='123->userName->admin@qq.com->Operate Successfully';
SET @description='userId->userName->email->expect';
INSERT INTO `metersphere`.`skw_ui_test_data_head` (`id`, `project_id`, `name`, `description`, `create_user_id`, `update_user_id`, `create_time`, `update_time`, `tags`)
VALUES (@id, @project_id, @Module_name, @Module_name, @create_user_id, @create_user_id, @create_time, @create_time, @tag);
INSERT INTO `metersphere`.`skw_ui_test_data_detail` (`id`, `ui_test_id`, `name`, `priority`, `data_contents`, `description`, `create_user_id`, `update_user_id`, `create_time`, `update_time`)
VALUES (UUID(), @id, @name, @priority, @data_contents, @description, @create_user_id, @create_user_id, @create_time, @create_time);

#添加User_Setup,userId重复，添加失败
SET @id=UUID();
SET @project_id=(SELECT p.id FROM project p JOIN `workspace` w ON p.`workspace_id`=w.id WHERE p.`name`='CSP' AND w.`name`='测试工作空间');
SET @Module_name='user_setup_data';
SET @priority='1';
SET @create_user_id='luke.zhong';
SET @update_user_id='luke.zhong';
SET @create_time='20210322140714';
SET @tag='tag';
SET @name='add_user_setup_repeat_data';
SET @data_contents='admin->userName->admin@qq.com->Operate Successfully';
SET @description='userId->userName->email->expect';
INSERT INTO `metersphere`.`skw_ui_test_data_head` (`id`, `project_id`, `name`, `description`, `create_user_id`, `update_user_id`, `create_time`, `update_time`, `tags`)
VALUES (@id, @project_id, @Module_name, @Module_name, @create_user_id, @create_user_id, @create_time, @create_time, @tag);
INSERT INTO `metersphere`.`skw_ui_test_data_detail` (`id`, `ui_test_id`, `name`, `priority`, `data_contents`, `description`, `create_user_id`, `update_user_id`, `create_time`, `update_time`)
VALUES (UUID(), @id, @name, @priority, @data_contents, @description, @create_user_id, @create_user_id, @create_time, @create_time);

#查询function_Setup成功
SET @id=UUID();
SET @project_id=(SELECT p.id FROM project p JOIN `workspace` w ON p.`workspace_id`=w.id WHERE p.`name`='CSP' AND w.`name`='测试工作空间');
SET @Module_name='function_setup_data';
SET @priority='1';
SET @create_user_id='luke.zhong';
SET @update_user_id='luke.zhong';
SET @create_time='20210322140714';
SET @tag='tag';
SET @name='query_function_setup_success_data';
SET @data_contents='System Mgmt->System Mgmt';
SET @description='functionId->expect';
INSERT INTO `metersphere`.`skw_ui_test_data_head` (`id`, `project_id`, `name`, `description`, `create_user_id`, `update_user_id`, `create_time`, `update_time`, `tags`)
VALUES (@id, @project_id, @Module_name, @Module_name, @create_user_id, @create_user_id, @create_time, @create_time, @tag);
INSERT INTO `metersphere`.`skw_ui_test_data_detail` (`id`, `ui_test_id`, `name`, `priority`, `data_contents`, `description`, `create_user_id`, `update_user_id`, `create_time`, `update_time`)
VALUES (UUID(), @id, @name, @priority, @data_contents, @description, @create_user_id, @create_user_id, @create_time, @create_time);

#查询UDC_Setup成功
SET @id=UUID();
SET @project_id=(SELECT p.id FROM project p JOIN `workspace` w ON p.`workspace_id`=w.id WHERE p.`name`='CSP' AND w.`name`='测试工作空间');
SET @Module_name='udcsetup_data';
SET @priority='1';
SET @create_user_id='luke.zhong';
SET @update_user_id='luke.zhong';
SET @create_time='20210322140714';
SET @tag='tag';
SET @name='udc_setup_query_data';
SET @data_contents='system->system';
SET @description='udcGroup->expect';
INSERT INTO `metersphere`.`skw_ui_test_data_head` (`id`, `project_id`, `name`, `description`, `create_user_id`, `update_user_id`, `create_time`, `update_time`, `tags`)
VALUES (@id, @project_id, @Module_name, @Module_name, @create_user_id, @create_user_id, @create_time, @create_time, @tag);
INSERT INTO `metersphere`.`skw_ui_test_data_detail` (`id`, `ui_test_id`, `name`, `priority`, `data_contents`, `description`, `create_user_id`, `update_user_id`, `create_time`, `update_time`)
VALUES (UUID(), @id, @name, @priority, @data_contents, @description, @create_user_id, @create_user_id, @create_time, @create_time);

#新增数据源
SET @id=UUID();
SET @project_id=(SELECT p.id FROM project p JOIN `workspace` w ON p.`workspace_id`=w.id WHERE p.`name`='CSP' AND w.`name`='测试工作空间');
SET @Module_name='Datasource_Mgmt';
SET @priority='1';
SET @create_user_id='luke.zhong';
SET @update_user_id='luke.zhong';
SET @create_time='20210322140714';
SET @tag='tag';
SET @name='add_datasource_data_data';
SET @data_contents='soa_sea_3308->jdbc:mysql://172.18.188.84:3308/soa_sea?characterEncoding=utf8&serverTimezone=GMT%2B8->test->6789test->Operate Successfully';
SET @description='DBName->JdbcURL->UserName->UserPwd->expect';
INSERT INTO `metersphere`.`skw_ui_test_data_head` (`id`, `project_id`, `name`, `description`, `create_user_id`, `update_user_id`, `create_time`, `update_time`, `tags`)
VALUES (@id, @project_id, @Module_name, @Module_name, @create_user_id, @create_user_id, @create_time, @create_time, @tag);
INSERT INTO `metersphere`.`skw_ui_test_data_detail` (`id`, `ui_test_id`, `name`, `priority`, `data_contents`, `description`, `create_user_id`, `update_user_id`, `create_time`, `update_time`)
VALUES (UUID(), @id, @name, @priority, @data_contents, @description, @create_user_id, @create_user_id, @create_time, @create_time);

#查询数据源
SET @id=UUID();
SET @project_id=(SELECT p.id FROM project p JOIN `workspace` w ON p.`workspace_id`=w.id WHERE p.`name`='CSP' AND w.`name`='测试工作空间');
SET @Module_name='Datasource_Mgmt';
SET @priority='1';
SET @create_user_id='luke.zhong';
SET @update_user_id='luke.zhong';
SET @create_time='20210322140714';
SET @tag='tag';
SET @name='search_market_and_datasource_data';
SET @data_contents='HAVI->soa_sea_3308->HAVI->soa_sea_3308';
SET @description='market_id,market_name,expected_Market_Id,expected_data_Source';
INSERT INTO `metersphere`.`skw_ui_test_data_head` (`id`, `project_id`, `name`, `description`, `create_user_id`, `update_user_id`, `create_time`, `update_time`, `tags`)
VALUES (@id, @project_id, @Module_name, @Module_name, @create_user_id, @create_user_id, @create_time, @create_time, @tag);
INSERT INTO `metersphere`.`skw_ui_test_data_detail` (`id`, `ui_test_id`, `name`, `priority`, `data_contents`, `description`, `create_user_id`, `update_user_id`, `create_time`, `update_time`)
VALUES (UUID(), @id, @name, @priority, @data_contents, @description, @create_user_id, @create_user_id, @create_time, @create_time);