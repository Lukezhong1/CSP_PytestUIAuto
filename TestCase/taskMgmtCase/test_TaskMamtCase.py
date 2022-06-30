import pytest
from TestData.taskMamtData import TaskMamtData

@pytest.mark.TaskMgmtTest
class TestTaskMgmt(object):

    @pytest.mark.parametrize('taskId,expect', TaskMamtData.query_execute_task_success)
    def test_query_execute_task_success(self, login,taskId,expect):
        """测试查询执行task"""
        scalebar_page = login[1]
        taskmgmt_page = login[2]
        scalebar_page.select_menu(menu="Task_Mgmt")
        taskmgmt_page.query_taskListPl_taskId(taskId)
        taskmgmt_page.execute_task()
        hint_text = taskmgmt_page.get_hint_text()
        if  'execute completely' in hint_text:
            execute_status = taskmgmt_page.get_execute_status_text()
            assert expect == execute_status
            print("执行task %s Success" %taskId)
        else:
            print("execute task not completely")

    @pytest.mark.parametrize('functionID,taskId,expect', TaskMamtData.add_query_execute_task_success)
    def test_query_execute_task_success(self, login,functionID,taskId,expect):
        """测试add执行task"""
        scalebar_page = login[1]
        taskmgmt_page = login[2]
        scalebar_page.select_menu(menu="Task_Mgmt")
        taskmgmt_page.add_task(functionID,taskId)
        taskmgmt_page.query_taskListPl_taskId(taskId)
        taskmgmt_page.execute_task()
        hint_text = taskmgmt_page.get_hint_text()
        if  'execute completely' in hint_text:
            execute_status = taskmgmt_page.get_execute_status_text()
            assert expect == execute_status
            print("执行task %s Success" %taskId)
        else:
            print(hint_text)


if __name__ == "__main__":
    pytest.main(['-v', 'test_TaskMamtCase.py'])
