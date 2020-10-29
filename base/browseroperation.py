
class BrowserOperation:

    def __init__(self,driver):
        self.driver = driver


    def open_url(self,url):
        try:
            self.driver.get(url)
        except Exception as e:
            print(e,'地址出错')
    def send_keys(self,xpath,content):
        try:
            self.driver.find_element_by_xpath(xpath).send_keys(content)
        except Exception as e:
            print(e,'元素未找到')
    def click_element(self,xpath):
        try:
            self.driver.find_element_by_xpath(xpath).click()
        except Exception as e:
            print(e, '元素未找到')

    def get_text(self,xpath):
        try:
            text = self.driver.find_element_by_xpath(xpath).text
        except Exception as e:
            print(e,'元素未找到')
        return text

    def get_alert_text(self):
        try:
            alert_text = self.driver.switch_to.alert.text
        except Exception as e:
            print(e,'元素未找到')
            return None
        else:
            return alert_text

    def get_title_text(self):
        try:
           title_text = self.driver.title
        except Exception as e:
            print(e,'元素未找到')
        return title_text


    def change_frame(self,framename):
        try:
            if '/' in framename:
                self.driver.switch_to.parent_frame()
                self.driver.switch_to.frame(self.driver.find_element_by_xpath(framename))
            else:
                self.driver.switch_to.parent_frame()
                self.driver.switch_to.frame(framename)
        except Exception as e:
            print(e)

    def change_window(self,window_name):
        windows = self.driver.window_handles
        for windows_id in windows:
            self.driver.switch_to.window(windows_id)
            if self.driver.title == window_name:
                print('添加用户成功')
                break

    def delete_readonly(self, id):
        self.driver.execute_script("document.getElementById('{}').readOnly=false".format(id))



