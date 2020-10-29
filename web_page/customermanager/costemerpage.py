import time

from crm_final_sys.unit.dboperation import MysqlConnection
from crm_final_sys.unit.excel_opreation import OperationExcel
from crm_final_sys.unit.log_crm import Auto_log
from crm_final_sys.unit.yaml_operation import YamlOperation
from crm_final_sys.web_page.usermanager.loginpage import LoginPage


class CustemerPage:

    def __init__(self):
        self.op = OperationExcel('../../config/test.xlsx', '登录用例参数')
        self.lg = LoginPage()
        self.log = Auto_log()
        self.db = MysqlConnection()
        self.yp = YamlOperation('../../config/locator.yaml')
        self.lg.login(self.op.get_cell(5,2),self.op.get_cell(5,3))
        time.sleep(3)

    def select_customer_message(self):
        self.log.set_message('change frame', 'info')
        self.lg.bo.change_frame(self.lg.yp.get_locator('SelectCustomer','topframe'))
        self.log.set_message('click button:客户信息', 'info')
        self.lg.bo.click_element(self.lg.yp.get_locator('SelectCustomer', 'click_button'))
        self.log.set_message('select_customer_message finish', 'info')

    def create_customer(self, **kwargs):
        # self.db.delete_operation('delete from customer_info where customer_name=="李四"')
        self.select_customer_message()
        self.log.set_message('change frame', 'info')
        self.lg.bo.change_frame(self.lg.yp.get_locator('CreateCustomer','mainframe'))
        self.log.set_message('click element', 'info')
        self.lg.bo.click_element(self.lg.yp.get_locator('CreateCustomer', 'add_button'))
        self.log.set_message('input customer_name:' + kwargs.get('customer_name', ''), 'info')
        self.lg.bo.send_keys(self.lg.yp.get_locator('CreateCustomer', 'customer_name'), kwargs.get('customer_name', ''))
        self.log.set_message('input customer_email:' + kwargs.get('cus_email', ''), 'info')
        self.lg.bo.send_keys(self.lg.yp.get_locator('CreateCustomer', 'customer_email'), kwargs.get('cus_email', ''))
        self.log.set_message('change readOnly', 'info')
        self.lg.bo.delete_readonly(self.lg.yp.get_locator('CreateCustomer', 'close_readonly'))
        self.log.set_message('input custome_birthday:' + kwargs.get('cus_bir', ''), 'info')
        self.lg.bo.send_keys(self.lg.yp.get_locator('CreateCustomer', 'customer_birthday'), kwargs.get('cus_bir', ''))
        self.log.set_message('input option_manager:' + kwargs.get('create_manager', ''), 'info')
        self.lg.bo.send_keys(self.lg.yp.get_locator('CreateCustomer', 'create_manager'),
                              kwargs.get
                              ('create_manager', ''))
        self.log.set_message('click element', 'info')
        self.lg.bo.click_element(self.lg.yp.get_locator('CreateCustomer', 'sure_button'))
        self.log.set_message('create_customer finish', 'info')
        time.sleep(2)

    def update_customer_message(self, **kwargs):
        self.select_customer_message()
        self.log.set_message('change frame', 'info')
        self.lg.bo.change_frame(self.lg.yp.get_locator('UpdateCustomer', 'mainframe'))
        self.log.set_message('click update', 'info')
        self.lg.bo.send_keys(self.lg.yp.get_locator('UpdateCustomer','select_customer'),kwargs.get('name',''))
        self.lg.bo.click_element(self.lg.yp.get_locator('UpdateCustomer', 'select_customer_submit'))

        self.lg.bo.click_element(self.lg.yp.get_locator('UpdateCustomer', 'update_Button'))
        if kwargs.get('mobilephone') != None:
            self.lg.bo.send_keys(self.lg.yp.get_locator('UpdateCustomer', 'mobilephone'), kwargs.get('mobilephone', ''))
        if kwargs.get('email') != None:
            self.lg.bo.send_keysself(self.lg.yp.get_locator('UpdateCustomer', 'email'), kwargs.get('email', ''))
        if kwargs.get('customerjob') != None:
            self.lg.bo.send_keys(self.lg.yp.get_locator('UpdateCustomer', 'customerjob'), kwargs.get('customerjob'))
        if kwargs.get('updatemanager') != None:
            self.lg.bo.send_keys(self.lg.yp.get_locator('UpdateCustomer', 'updatemanager'), kwargs.get('updatemanager', ''))
        self.lg.bo.click_element(self.lg.yp.get_locator('UpdateCustomer', 'submit_button'))


    def get_add_success_text(self):
        self.lg.bo.change_window('添加记录成功')
        customer_add_text = self.lg.bo.get_text('/html/body/center')
        return customer_add_text


    def customer_modify(self):
        pass

if __name__ == '__main__':
    cp = CustemerPage()
    cp.customer_add(id='1001',name='zhangsan',phone='101554354')