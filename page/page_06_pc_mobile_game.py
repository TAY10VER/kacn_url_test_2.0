from base.base import Base
import page
from selenium.webdriver.common.by import By
from time import sleep


class Page_06(Base):
    def page_get_all_goods(self, driver):
        all_goods = []
        all_filter = self.base_find_items(page.pc_mobile_game_filter)
        for i in range(len(all_filter)):
            if i > 0:
                all_goods.append(all_filter[i].text)
                all_filter[i].click()
                goods_name = driver.find_element(By.XPATH, value="//div[@data-key='{}']/div[@class='game_main']".format(all_filter[i].text)).text
                all_goods.append(goods_name.replace("\n", " "))
                sleep(1)
        return all_goods
