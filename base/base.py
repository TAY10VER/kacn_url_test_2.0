import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    # 初始化 定义构造函数
    def __init__(self, driver):
        self.driver = driver

    # 查找方法封装
    def base_find(self, loc,timeout=30,poll=0.5):
        """
        :param loc: 格式为列表或元组， 内容：元素定位信息，使用By类
        :param timeout:查找元素超时时间，默认3秒
        :param poll:查找元素频率，默认0.5
        :return: 元素
        """
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x:x.find_element(*loc))

    # 查找一组元素
    def base_find_items(self, loc, timeout=30, poll=0.5):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_elements(*loc))

    # 判断元素是否存在 方法封装
    def base_element_is_exist(self, loc):
        try:
            self.base_find(loc, timeout=2)
            return True  # 代表元素存在
        except:
            return False  # 代表元素不存在


    # 输入方法封装
    def base_input(self, loc, value):
        """
        :param loc:元素定位信息
        :param value:要输入的值
        """
        # 1.获取元素
        e1 = self.base_find(loc)
        # 2.清空操作
        e1.clear()
        # 3.输入操作
        e1.send_keys(value)

    # 点击方法封装
    def base_click(self, loc):
        """
        :param loc: 元素定位信息
        """
        # 获取元素并点击
        self.base_find(loc).click()

    # 获取元素文本
    def base_get_text(self, loc):
        """
        :param loc: 元素定位信息
        :return: 返回元素文本值
        """
        return self.base_find(loc).text

    # 获取元素href
    def base_get_href(self, ele):
        return ele.get_attribute('href')

    # 截图方法封装
    def base_get_image(self):
        self.driver.get_screenshot_as_file("../image/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S")))

    # 滚动页面至元素可见
    def base_scroll(self, loc):
        ele = self.base_find(loc)
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)

    # 滑块拖动方法封装
    def base_move_slider(self, loc):
        self.hover=self.base_find(loc)
        self.move = webdriver.ActionChains(self.driver)
        self.move.click_and_hold(self.hover)
        self.move.move_by_offset(300,0)
        time.sleep(2)
        self.move.release()
        self.move.perform()

    # 切换窗口方法封装
    def base_switch_to_window(self, current_handle):
        """
        :param current_handle: 当前窗口的handles
        :return:
        """
        # 遍历当前页面所有的handles
        for handle in self.driver.window_handles:
            # 判断handle不等于当前handle时
            if handle != current_handle:
                # 切换窗口
                self.driver.switch_to.window(handle)

