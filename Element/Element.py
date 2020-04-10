from selenium.common.exceptions import WebDriverException, NoSuchElementException
from Element.Waitor import Waitor
from Element.Find import Find
from Utilitys.WaitUtils import WaitUtils


class Element(Find):

    def __init__(self, driver):
        Find.__init__(self)
        self.driver = driver
        self.interval = 0.5
        self.timeout = 20

    def wait_for(self):
        return Waitor(self, self.interval, self.timeout)

    def get_interval(self):
        return self.interval

    def get_timeout(self):
        return self.timeout

    def set_interval(self, interval):
        self.interval = interval

    def set_timeout(self, timeout):
        self.timeout = timeout

    def find_element_click(self, by, value):
        try:
            self.driver.find_element(by, value).click()
        except Exception as handleRetry:
            try:
                WaitUtils.wait_for_element_clickable(self.driver, by, value)
                self.driver.find_element(by, value).click()
            except Exception as e:
                raise e

    def find_element_sendkeys(self, by, value, keys):
        try:
            self.driver.find_element(by, value).send_keys(keys)
        except Exception as handleRetry:
            try:
                WaitUtils.wait_for_element_visible(self.driver, by, value)
                self.driver.find_element(by, value).send_keys(keys)
            except Exception as e:
                raise e

    def find_element_set_value(self, by, value, keys):
        try:
            self.driver.find_element(by, value).set_value(keys)
        except Exception as handleRetry:
            try:
                WaitUtils.wait_for_element_visible(self.driver, by, value)
                self.driver.find_element(by, value).set_value(keys)

            except Exception as e:
                raise e

    def drag_and_drop(self, origin_el, destination_el):
        pass

    def element_exist(self, by, value):
        try:
            self.driver.find_element(by, value)
            return True
        except Exception as handleRetry:
            try:
                WaitUtils.wait_for_element_present(self.driver, by, value)
                self.driver.find_element(by, value)
            except Exception as e:
                raise e

    def visible(self,by, value):
        try:
            return self.driver().find_element(by, value).is_displayed()
        except Exception as handleRetry:
            try:
                self._refresh()
                return self.driver().find_element(by, value).is_displayed()
            except Exception as e:
                return False

    def clear(self, by, value):
        try:
            self.driver().find_element(by, value).clear()
        except Exception as handleRetry:
            try:
                self.wait_for().visible()
                self.driver().find_element(by, value).clear()
            except Exception as e:
                raise NoSuchElementException

    def find_elements(self, by, value, number=1):
        try:
            if len(self.driver.find_elements(by, value)) >= number:
                return self.driver.find_elements(by, value)
            else:
                raise Exception
        except Exception as handleRetry:
            self._refresh()
            WaitUtils.wait_for_elements_number_right(self.driver, by, value, number)
            return self.driver.find_elements(by, value)

    # TODO: We need to wrap more method here.
