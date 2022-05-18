import random
from time import sleep
from base.base import Base
import page
from selenium.webdriver.common.by import By


class Page_04(Base):

    # 获取商品名称、充值类型、面值
    def page_get_pg_values(self, driver):
        list = []
        # 获取商品名称
        pg_name = self.base_get_text(page.pc_pg_name)
        self.base_click(page.pc_pg_name)
        list.append("商品名称：{}".format(pg_name))
        # 获取充值类型、面值
        items = self.base_find_items(page.pc_pg_show_mode)
        for i in range(len(items)):
            list.append(items[i].text)
            items[i].click()
            sleep(1)
            values = driver.find_element(By.XPATH, value="//div[@id='show{}']".format(i + 1)).text
            list.append(values.replace("\n", " "))
        return list

    # 点击立即购买按钮
    def page_click_buy_btn(self):
        self.base_click(page.pc_buy_btn)

    # 组合业务方法
    def page_pc_landing_pg(self, driver):
        # 获取商品信息
        value_list = self.page_get_pg_values(driver)
        # 点击购买按钮
        if self.base_element_is_exist(page.pc_buy_btn):
            self.page_click_buy_btn()
            print("购买按钮存在，可正常点击")
        else:
            print("出错啦！未识别到购买按钮")
        return value_list

