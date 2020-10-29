import time
import unittest
from HTMLTestRunner import HTMLTestRunner
import sys
sys.path.append('D:\\.jenkins\\workspace')

from crm_final_sys.base.usebrowser import UseBrowser
from crm_final_sys.unit.excel_opreation import OperationExcel
from crm_final_sys.web_page.customermanager.costemerpage import CustemerPage


class CustomerTest(unittest.TestCase):

    def setUp(self) -> None:
        self.co = CustemerPage()
        self.bo = self.co.lg.bo
        self.op = OperationExcel('../../config/test.xlsx', '添加用例参数')
        self.op_update = OperationExcel('../../config/test.xlsx', '修改用户用例参数')

    def test_customer_add_success(self):
        customer_name = self.op.get_cell(1,2)
        cus_email = self.op.get_cell(1,3)
        cus_bir = self.op.get_cell(1,4)
        create_manager = self.op.get_cell(1,5)
        self.co.create_customer(customer_name=customer_name,cus_email=cus_email,cus_bir=cus_bir,create_manager=create_manager)
        add_tue =self.bo.get_alert_text()
        self.assertEqual(self.op.get_cell(1, 6), add_tue)

    def test_customer_update(self):
        name = self.op_update.get_cell(1, 2)
        customerjob = self.op_update.get_cell(1, 3)
        self.co.update_customer_message(name=name, customerjob=customerjob)
        self.assertEqual(self.bo.get_alert_text(), self.op_update.get_cell(1, 4))

    def tearDown(self) -> None:
        UseBrowser.quit()

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    testcase = unittest.TestLoader().loadTestsFromTestCase(CustomerTest)
    suite.addTests(testcase)
    date_now = time.strftime('%Y-%m-%d', time.localtime())
    with open('../../report/AddCustomer_test_report.html', 'wb+') as file:
        runner = HTMLTestRunner(stream=file, verbosity=2, title='Login_auto_test', description='ui_test')
        runner.run(suite)

