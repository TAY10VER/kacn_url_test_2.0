from page.page_06_pc_mobile_game import Page_06
from tools.get_driver import GetDriver
from tools.read_txt import read_txt
import page
from time import sleep


def get_url():
    arrs = []
    for data in read_txt("pc_urls.txt"):
        arrs.append(data.strip())
    return arrs[8]


class Test_05():
    # 初始化
    def setup_class(self):
        url = get_url()
        self.driver = GetDriver().get_web_driver(url)
        self.pc_mobile_game = Page_06(self.driver)

    # 结束
    def teardown_class(self):
        # 关闭driver
        GetDriver().quit_web_driver()

    def test_pc_mpobile_game(self):
        """测试pc 手游专题页"""
        # 判断页面是否跳转
        url = get_url()
        print("测试URL：", url)
        if url == self.driver.current_url:
            print("页面未发生跳转")
        else:
            print("页面发生跳转，跳转后的页面：{}".format(self.driver.current_url))
        # 断言url，如果发生跳转，不继续执行
        assert url == self.driver.current_url

        # 断言 cookie_T
        cookie_T = self.driver.get_cookie("t").get("value")
        print("预期T值：30，实际T值:{}".format(cookie_T))
        assert '30' == cookie_T

        all_goods = self.pc_mobile_game.page_get_all_goods(self.driver)
        print("所有商品：\n", all_goods)
