from page.pgae_11_m_guojifu import Page_11
from tools.get_driver import GetDriver
from tools.read_txt import read_txt


def get_url():
    arrs = []
    for data in read_txt("m_urls.txt"):
        arrs.append(data.strip())
    return arrs[6]

class Test_10():
    # 初始化
    def setup_class(self):
        url = get_url()
        self.driver = GetDriver().get_mobile_driver(url)
        self.m_guojifu = Page_11(self.driver)

    # 结束
    def teardown_class(self):
        # 关闭driver
        self.driver.quit()

    def test_m_guojifu(self):
        """测试mobile 国际服"""
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
        goods_names = self.m_guojifu.page_get_all_goods_name()
        print("所有商品：", goods_names)

        # 获取所有商品链接
        links = self.m_guojifu.page_get_all_links()
        # 循环访问所有链接，获取页面元素
        for link in links:
            goods_value = []
            self.driver.get(link)
            goods_value.append(goods_names[links.index(link)])
            goods_value.append(self.m_guojifu.page_get_goods_values_list(self.driver))
            print(goods_value)
