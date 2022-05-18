from page.page_10_mlanding_pg import Page_10
from tools.get_driver import GetDriver
from tools.read_txt import read_txt


def get_url():
    arrs = []
    for data in read_txt("m_urls.txt"):
        arrs.append(data.strip())
    return arrs[5]

class Test_10():
    # 初始化
    def setup_class(self):
        url = get_url()
        self.driver = GetDriver().get_mobile_driver(url)
        self.mlanding_pg = Page_10(self.driver)

    # 结束
    def teardown_class(self):
        # 关闭driver
        self.driver.quit()

    def test_mlanding_pg(self):
        """测试mobile landing 苹果商品"""
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

        # 获取所有商品
        goods_values = self.mlanding_pg.page_mlanding_pg(self.driver)
        print("商品信息：", goods_values)