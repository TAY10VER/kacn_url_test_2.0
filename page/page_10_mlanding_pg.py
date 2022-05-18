
from time import sleep
from base.base import Base
import page
from selenium.webdriver.common.by import By


class Page_10(Base):

    # 获取商品名称、账号所属地区，商品面值
    def page_get_goods_values(self, driver):
        items = self.base_find_items(page.mlanding_pg_show_mode)
        list = []
        goods_name = self.base_get_text(page.mlanding_goods_name)
        list.append("商品名称：{}".format(goods_name))
        for i in range(len(items)):
            list.append(items[i].text)
            items[i].click()
            sleep(1)
            values = driver.find_element(By.XPATH, value="//ul[@id='show{}']".format(i + 1)).text
            list.append(values.replace("\n"," "))
        return list

    # 点击立即购买按钮
    def page_click_buy_btn(self):
        self.base_click(page.mlanding_goods_buy_byn)

    # 组合业务方法
    def page_mlanding_pg(self, driver):
        # 获取商品信息
        value_list = self.page_get_goods_values(driver)
        # 判断购买按钮是否存在
        if self.base_element_is_exist(page.mlanding_goods_buy_byn):
            self.page_click_buy_btn()
            print("购买按钮存在，可正常点击")
        else:
            print("出错啦！未识别到购买按钮")
        return value_list





