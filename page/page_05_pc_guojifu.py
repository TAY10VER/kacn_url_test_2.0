from time import sleep
from base.base import Base
import page
from selenium.webdriver.common.by import By


class Page_05(Base):
    # 国际服所有商品名称
    def page_get_all_goods_name(self):
        list = []
        all_goods = self.base_find_items(page.pc_guojifu_names)
        print("商品个数：", len(all_goods))
        for i in range(len(all_goods)):
            list.append(all_goods[i].text)
        return list

    # 获取国际服所有商品href
    def page_get_all_links(self):
        eles = self.base_find_items(page.pc_guojifu_hrefs)
        links = []
        for i in range(len(eles)):
            links.append(self.base_get_href(eles[i]))
        return links

    # 循环点击账号所属地区，分别获取面值
    def page_get_goods_values_list(self, driver):
        items = self.base_find_items(page.pc_guojifu_types)
        list = []
        for i in range(len(items)):
            list.append(items[i].text)
            items[i].click()
            sleep(1)
            values = driver.find_element(By.XPATH, value="//div[@id='show{}']".format(i + 1)).text
            list.append(values.replace("\n", " "))
        return list

