from page.page_12_m_mobile_game import Page_12
from tools.get_driver import GetDriver
from tools.read_txt import read_txt


def get_url():
    arrs = []
    for data in read_txt("m_urls.txt"):
        arrs.append(data.strip())
    return arrs[7]


class Test_12():
    # 初始化
    def setup_class(self):
        url = get_url()
        self.driver = GetDriver().get_mobile_driver(url)
        self.m_mobile_game = Page_12(self.driver)

    # 结束
    def teardown_class(self):
        # 关闭driver
        self.driver.quit()

    def test_m_mobile_game(self):
        """测试mobile 手游专题页"""
        url = get_url()
        print("测试URL：", url)

        # 判断页面是否跳转
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

        # 获取所有商品名称
        all_goods_names = self.m_mobile_game.page_get_all_goods()
        print("所有商品：", all_goods_names)