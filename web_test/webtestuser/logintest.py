import time
import unittest
from HTMLTestRunner import HTMLTestRunner
import sys
sys.path.append('D:\\.jenkins\\workspace')
from crm_final_sys.base.browseroperation import BrowserOperation
from crm_final_sys.base.usebrowser import UseBrowser
from crm_final_sys.unit.excel_opreation import OperationExcel
from crm_final_sys.web_page.usermanager.loginpage import LoginPage



class LoginTest(unittest.TestCase):
    def setUp(self) -> None:
        self.login = LoginPage()
        self.bo = BrowserOperation(UseBrowser.driver)
        self.op = OperationExcel('../../config/test.xlsx', '登录用例参数')

    def test_login_username_password_null(self):
        self.login.login(self.op.get_cell(1,2),self.op.get_cell(1,3))
        login_null = self.bo.get_alert_text()
        self.assertEqual(login_null,self.op.get_cell(1,4))

    def test_login_username_null(self):
        self.login.login(self.op.get_cell(2,2),self.op.get_cell(2,3))
        login_username_null = self.bo.get_alert_text()
        self.assertEqual(login_username_null,self.op.get_cell(2,4))

    def test_login_password_null(self):
        self.login.login(self.op.get_cell(3,2),self.op.get_cell(3,3))
        login_password_null = self.bo.get_alert_text()
        self.assertEqual(login_password_null,self.op.get_cell(3,4))

    def test_login_error(self):
        self.login.login(self.op.get_cell(4,2),self.op.get_cell(4,3))
        login_error = self.bo.get_alert_text()
        self.assertEqual(login_error,self.op.get_cell(4,4))

    def test_login_success(self):
        self.login.login(self.op.get_cell(5,2),self.op.get_cell(5,3))
        correct_text = self.bo.get_title_text()
        self.assertEqual(correct_text,self.op.get_cell(5,4))



    def tearDown(self) -> None:
        UseBrowser.quit()




if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    test_case = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    suite.addTests(test_case)
    date_now = time.strftime('%Y-%m-%d', time.localtime())
    with open('../../report/report_login.html', 'wb+') as file:
        runner = HTMLTestRunner(stream=file, verbosity=0, title='UI自动化测试', description='ui自动化测试')
        runner.run(suite)