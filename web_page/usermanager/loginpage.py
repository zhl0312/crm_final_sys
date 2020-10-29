from crm_final_sys.base.browseroperation import BrowserOperation
from crm_final_sys.base.usebrowser import UseBrowser
from crm_final_sys.config.log_crm import Auto_log
from crm_final_sys.unit.yaml_operation import YamlOperation



class LoginPage:

    def __init__(self):
        self.yp = YamlOperation('../../config/locator.yaml')
        self.log = Auto_log()
        self.ub = UseBrowser()
        self.bo = BrowserOperation(UseBrowser.driver)
        self.bo.open_url('http://172.17.4.217:8080/crm/')

    def login(self,username,password):
        self.log.set_message('---登录功能开始---', 'info')
        self.bo.send_keys(self.yp.get_locator('LoginPage','username'), username)
        self.log.set_message('---输入用户名---' + username, 'info')
        self.bo.send_keys(self.yp.get_locator('LoginPage','password'), password)
        self.log.set_message('---输入密码---' + password, 'info')
        self.bo.click_element(self.yp.get_locator('LoginPage','submit'))
        self.log.set_message('---点击登录---', 'info')
        print()

    def login_correct_text(self,framename,xpath):
        self.bo.change_frame(framename)
        return  self.bo.get_text(xpath)
